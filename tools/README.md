# Maintain the profile

## Add a deployed project

Add its HTTPS app URL to the **Website** field in the public repository's About panel, or a clearly labeled **Live demo** link in its README. The check adds public repositories owned by `Nitesh-Datascience` to the live-project table. Creating a repository without a deployment URL does not identify an app.

The hourly ChatGPT project check and the daily GitHub workflow use the same catalog rules. They preserve the curated entries in `data/live-projects.json`, skip duplicates, forks, archived repositories, the profile repository and portfolio, and only change the marked live-project block in the README. They never scan private repositories.

Supported deployment hosts: Streamlit, Vercel, Netlify, Render, Hugging Face Spaces and the owner's GitHub Pages. URLs containing credentials or query parameters are excluded. Links are deployment references, not uptime or functionality guarantees.

To add another host or a curated app, edit the catalog explicitly. PrivyScan's public app is curated without linking its private source. APL's supplied link is marked as requiring access; this workflow does not change Streamlit permissions.

```bash
python3 tools/refresh_live_projects.py
python3 tools/refresh_profile_metrics.py
```

For an offline preview with already-verified public repository metadata and README text:

```bash
python3 tools/refresh_live_projects.py --snapshot public-repositories.json
```

## Profile panels

GitHub statistics come from public owned repositories. Language bars count primary repository languages, rather than rating skills. The workflow uses the built-in GitHub token and writes only the README catalog, catalog JSON and public metrics assets.

The terminal animation is a local GIF made from Nitesh's public profile photo. To regenerate it, install Pillow and NumPy, then run `python3 tools/render_terminal.py`.
