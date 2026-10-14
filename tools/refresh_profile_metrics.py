"""Refresh the profile panels from public GitHub data, without third-party card services."""
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path
import argparse
import json
import os
import re
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'neon-terminal'


def public_repositories(items, username):
    return [r for r in items if r.get('private') is False
            and r.get('owner', {}).get('login', '').casefold() == username.casefold()]


def github_get(path):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'Public-Profile-Metrics',
               'X-GitHub-Api-Version': '2022-11-28'}
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    with urlopen(Request('https://api.github.com' + path, headers=headers), timeout=30) as response:
        return json.load(response)


def load_live(username):
    profile = github_get('/users/' + username)
    items = []
    for page in range(1, 101):
        batch = github_get(f'/users/{username}/repos?type=owner&per_page=100&page={page}')
        items.extend(batch)
        if len(batch) < 100:
            break
    repos = public_repositories(items, username)
    if len(repos) != profile['public_repos']:
        raise RuntimeError('Public repository response is incomplete; retaining the existing panels.')
    return {'username': username, 'followers': profile['followers'],
            'as_of': datetime.now(timezone.utc).date().isoformat(),
            'repos': [{'name': r['name'], 'language': r.get('language'),
                       'stars': r['stargazers_count'], 'forks': r['forks_count']} for r in repos]}


def build_svg(data, featured):
    repos = data['repos']
    languages = Counter(r['language'] for r in repos if r.get('language'))
    groups = sorted(languages.items(), key=lambda x: (-x[1], x[0]))
    stars = sum(r['stars'] for r in repos)
    date = datetime.fromisoformat(data['as_of']).strftime('%d %b %Y')
    body = '''<defs><linearGradient id="edge"><stop stop-color="#885dff"/><stop offset=".5" stop-color="#35deff"/><stop offset="1" stop-color="#65efbc"/></linearGradient></defs>
<rect width="1000" height="316" rx="16" fill="#071024"/>
<rect x="1" y="1" width="998" height="314" rx="15" fill="none" stroke="#345185"/>
<path d="M18 2H982" stroke="url(#edge)" stroke-width="3"/>
<g font-family="DejaVu Sans Mono, Consolas, monospace">
<text x="26" y="38" fill="#78e7ff" font-size="17" font-weight="700">GITHUB / PUBLIC PROFILE</text>
<path d="M490 22V286" stroke="#283960"/>
<text x="517" y="38" fill="#78e7ff" font-size="17" font-weight="700">PRIMARY REPOSITORY LANGUAGES</text>'''
    metrics = [(len(repos), 'PUBLIC REPOSITORIES'), (stars, 'STARS RECEIVED'),
               (featured, 'FEATURED PROJECTS'), (data['followers'], 'FOLLOWERS')]
    for i, (value, label) in enumerate(metrics):
        x = 27 + (i % 2) * 230
        y = 61 + (i // 2) * 108
        body += f'''<rect x="{x}" y="{y}" width="210" height="91" rx="9" fill="#101b36" stroke="#263d6c"/>
<text x="{x + 18}" y="{y + 47}" fill="#f0f5ff" font-size="34" font-weight="700">{value}</text>
<text x="{x + 18}" y="{y + 73}" fill="#a9b8d9" font-size="11">{label}</text>'''
    colors = ['#41d7ff', '#a483ff', '#66e9bd', '#ffcf68', '#e982cf', '#96acff']
    max_count = max(languages.values(), default=1)
    for i, (language, count) in enumerate(groups[:6]):
        y = 64 + i * 35
        body += f'''<text x="517" y="{y + 13}" fill="#cfdbf4" font-size="13">{escape(language)}</text>
<rect x="695" y="{y + 3}" width="220" height="10" rx="5" fill="#1a2847"/>
<rect x="695" y="{y + 3}" width="{round(220 * count / max_count, 2)}" height="10" rx="5" fill="{colors[i]}"/>
<text x="961" y="{y + 13}" text-anchor="end" fill="#edf3ff" font-size="14">{count}</text>'''
    unspecified = sum(r.get('language') is None for r in repos)
    body += f'''<text x="517" y="{min(278, 76 + len(groups[:6]) * 35)}" fill="#899abf" font-size="11">Repository counts · Unspecified: {unspecified}</text>
<text x="27" y="295" fill="#8fa4c9" font-size="11">Public data · Updated {date}</text></g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="316" viewBox="0 0 1000 316" role="img" aria-labelledby="title desc">
<title id="title">{escape(data['username'])} — public GitHub statistics</title>
<desc id="desc">{len(repos)} public repositories, {stars} received stars, {featured} featured projects and {data['followers']} followers. Primary languages are counts of public repositories, not skill ratings. Updated {date}.</desc>{body}</svg>'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-json', type=Path, help='Use an already-verified public data snapshot.')
    parser.add_argument('--user', default=os.environ.get('GITHUB_REPOSITORY_OWNER', 'Nitesh-Datascience'))
    args = parser.parse_args()
    data = json.loads(args.data_json.read_text()) if args.data_json else load_live(args.user)
    data['repos'] = sorted(data['repos'], key=lambda r: r['name'].casefold())
    featured = len(re.findall(r'<h3>[^<]+</h3>', (ROOT / 'README.md').read_text()))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'metrics.svg').write_text(build_svg(data, featured))
    (OUT / 'metrics-data.json').write_text(json.dumps(data, indent=2) + '\n')
    print(f"Updated public metrics: {len(data['repos'])} repositories, {sum(r['stars'] for r in data['repos'])} received stars.")


if __name__ == '__main__':
    main()
