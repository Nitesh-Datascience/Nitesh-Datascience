"""Add deployments from public owned repositories and refresh only the catalog block."""
from concurrent.futures import ThreadPoolExecutor
from html import escape, unescape
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlsplit, urlunsplit, quote
import argparse
import base64
import json
import re

from refresh_profile_metrics import ROOT, github_get, public_repositories

START = '<!-- LIVE-PROJECTS:START -->'
END = '<!-- LIVE-PROJECTS:END -->'
CATALOG = ROOT / 'data' / 'live-projects.json'
LABEL = re.compile(r'\b(live|demo|dashboard|deployed|deployment|try\s+(?:it|the\s+app))\b', re.I)
HOSTS = ('streamlit.app', 'vercel.app', 'netlify.app', 'onrender.com', 'hf.space')


def safe_demo_url(value, owner):
    """Only public deployment hosts; never copy credentials, query tokens or local URLs."""
    if not isinstance(value, str) or any(c.isspace() for c in value):
        return None
    try:
        u = urlsplit(unescape(value).rstrip('.,;'))
        host = (u.hostname or '').lower()
        if u.scheme != 'https' or u.username or u.password or u.port not in (None, 443):
            return None
        if u.query or 'https://' in u.path or 'http://' in u.path:
            return None
        allowed = any(host.endswith('.' + h) and host != h for h in HOSTS)
        allowed |= host == owner.lower() + '.github.io' and bool(u.path.strip('/'))
        allowed |= host == 'huggingface.co' and u.path.startswith('/spaces/')
        if not allowed or any(x in host for x in ('example', 'your-app', 'yourapp', 'localhost')):
            return None
        return urlunsplit(('https', host, u.path.rstrip('/') + '/', '', ''))
    except ValueError:
        return None


def readme_candidates(text, owner):
    # Ignore fenced code examples and image badges. A README must label the app link.
    text = re.sub(r'```.*?```|~~~.*?~~~', '', text, flags=re.S)
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)|<img\b[^>]*>', '', text, flags=re.I)
    heading = ''
    candidates = []
    for line in text.splitlines():
        if line.lstrip().startswith('#'):
            heading = line
        if not LABEL.search(line + ' ' + heading):
            continue
        for raw in re.findall(r'https://[^\s<>"\)\]]+', line):
            url = safe_demo_url(raw, owner)
            if url:
                candidates.append(url)
    return candidates


def discover(repos, owner, current):
    known_urls = {p['demo'] for p in current}
    known_repos = {p.get('repository', '').casefold() for p in current}
    additions = []
    for repo in sorted(public_repositories(repos, owner), key=lambda r: r['name'].casefold()):
        full_name = repo.get('full_name', owner + '/' + repo['name'])
        if repo.get('fork') or repo.get('archived') or repo['name'].casefold() in (owner.casefold(), 'portfolio'):
            continue
        if full_name.casefold() in known_repos:
            continue
        homepage = safe_demo_url(repo.get('homepage'), owner)
        candidates = ([homepage] if homepage else []) + readme_candidates(repo.get('readme', ''), owner)
        for url in candidates:
            if url in known_urls:
                continue
            title = re.sub(r'[_-]+', ' ', repo['name']).strip()
            summary = (repo.get('description') or 'Explore the deployed project and its source code.').strip()
            additions.append({'title': title, 'summary': summary[:160], 'demo': url,
                              'repository': full_name, 'origin': 'discovered'})
            known_urls.add(url)
            known_repos.add(full_name.casefold())
            break
    return additions


def load_repositories(owner):
    repos = []
    profile = github_get('/users/' + owner)
    for page in range(1, 101):
        batch = github_get(f'/users/{owner}/repos?type=owner&per_page=100&page={page}')
        repos.extend(batch)
        if len(batch) < 100:
            break
    repos = public_repositories(repos, owner)
    if len(repos) != profile['public_repos']:
        raise RuntimeError('Incomplete public repository list; retaining the catalog.')

    def add_readme(repo):
        try:
            doc = github_get('/repos/' + repo['full_name'] + '/readme')
            repo['readme'] = base64.b64decode(doc.get('content', '')).decode('utf-8', 'replace')
        except HTTPError as exc:
            if exc.code != 404:
                raise
            repo['readme'] = ''
        return repo

    with ThreadPoolExecutor(max_workers=6) as pool:
        return list(pool.map(add_readme, repos))


def cell(text):
    text = escape(str(text)).replace('|', '&#124;').replace('\n', ' ')
    for character, entity in (('[', '&#91;'), (']', '&#93;'), ('`', '&#96;'), ('*', '&#42;')):
        text = text.replace(character, entity)
    return text


def render_catalog(projects, owner):
    lines = ['| Project | Explore | Demo | Source |', '| --- | --- | --- | --- |']
    for p in projects:
        url = safe_demo_url(p['demo'], owner)
        if not url:
            raise ValueError('Invalid deployment URL in catalog: ' + p['title'])
        label = 'Access required ↗' if p.get('access') == 'restricted' else 'Open app ↗'
        source = p.get('repository', '')
        if source and not re.fullmatch(re.escape(owner) + r'/[A-Za-z0-9_.-]+', source, re.I):
            raise ValueError('Catalog source must belong to the profile owner.')
        code = f'[Code ↗](https://github.com/{quote(source, safe="/")})' if source else '—'
        lines.append(f"| **{cell(p['title'])}** | {cell(p['summary'])} | [{label}]({url}) | {code} |")
    return '\n'.join(lines)


def update_readme(text, projects, owner):
    if text.count(START) != 1 or text.count(END) != 1 or text.index(START) > text.index(END):
        raise ValueError('Expected exactly one ordered live-project catalog block.')
    before, rest = text.split(START)
    _, after = rest.split(END)
    return before + START + '\n\n' + render_catalog(projects, owner) + '\n\n' + END + after


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--snapshot', type=Path, help='Use a verified public repository snapshot.')
    parser.add_argument('--render-only', action='store_true', help='Render the curated catalog without discovery.')
    args = parser.parse_args()
    config = json.loads(CATALOG.read_text())
    owner = config['owner']
    projects = config['projects']
    additions = []
    if not args.render_only:
        repos = json.loads(args.snapshot.read_text()) if args.snapshot else load_repositories(owner)
        additions = discover(repos, owner, projects)
        projects += additions
    readme = ROOT / 'README.md'
    updated = update_readme(readme.read_text(), projects, owner)
    if additions:
        CATALOG.write_text(json.dumps(config, ensure_ascii=False, indent=2) + '\n')
    if updated != readme.read_text():
        readme.write_text(updated)
    print(f'Catalog: {len(projects)} projects; {len(additions)} new deployment links.')


if __name__ == '__main__':
    main()
