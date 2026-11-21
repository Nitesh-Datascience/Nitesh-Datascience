#!/usr/bin/env python3
"""Apply a python-inspired skin to the moving snake in Platane/snk SVGs."""
from pathlib import Path
import re
import sys

DEFS = """
<defs>
  <linearGradient id="pythonBody" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#24201b"/>
    <stop offset="0.48" stop-color="#59402a"/>
    <stop offset="1" stop-color="#171512"/>
  </linearGradient>
  <linearGradient id="pythonHead" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#745333"/>
    <stop offset="0.55" stop-color="#35271d"/>
    <stop offset="1" stop-color="#171512"/>
  </linearGradient>
  <pattern id="pythonScales" width="8" height="7" patternUnits="userSpaceOnUse">
    <path d="M0 2 Q2 0 4 2 Q6 4 8 2 M-4 5 Q-2 3 0 5 Q2 7 4 5 Q6 3 8 5"
      fill="none" stroke="#c69a58" stroke-opacity=".48" stroke-width=".8"/>
    <path d="M0 2 Q2 4 4 2" fill="none" stroke="#0d0c0a" stroke-opacity=".7" stroke-width=".6"/>
  </pattern>
  <filter id="pythonShadow" x="-40%" y="-40%" width="180%" height="180%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="1.2" result="blur"/>
    <feOffset dy="1" result="offset"/>
    <feComponentTransfer><feFuncA type="linear" slope=".55"/></feComponentTransfer>
    <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<style>
  .s { fill: url(#pythonBody) !important; stroke: #17120d; stroke-width: 1.1px; filter: url(#pythonShadow); }
  rect.s { rx: 5px; ry: 5px; }
  .snake-head { fill: url(#pythonHead); stroke: #17120d; stroke-width: 1px; }
  .snake-scales { fill: url(#pythonScales); opacity: .9; }
  .snake-eye { fill: #f6c65c; stroke: #17120d; stroke-width: .7px; }
  .snake-pupil { fill: #100e0b; }
  .snake-nostril { fill: #d99a4b; }
  .snake-tongue { fill: none; stroke: #ed6a31; stroke-width: 1.35px; stroke-linecap: round; stroke-linejoin: round; }
</style>
"""

HEAD = """
<g class="s s0">
  <path class="snake-head" d="M1 4 C2 0 7 -1 11 1 C15 3 16 7 14 11 C12 15 6 16 3 13 C0 11 -1 7 1 4 Z"/>
  <path class="snake-scales" d="M1 4 C2 0 7 -1 11 1 C15 3 16 7 14 11 C12 15 6 16 3 13 C0 11 -1 7 1 4 Z"/>
  <ellipse class="snake-eye" cx="10.8" cy="4.2" rx="1.65" ry="1.35"/>
  <ellipse class="snake-eye" cx="10.8" cy="10.1" rx="1.65" ry="1.35"/>
  <circle class="snake-pupil" cx="11.1" cy="4.2" r=".65"/>
  <circle class="snake-pupil" cx="11.1" cy="10.1" r=".65"/>
  <circle class="snake-nostril" cx="14.2" cy="7.2" r=".55"/>
  <path class="snake-tongue" d="M14.5 8 L17 8 M17 8 L18.4 6.8 M17 8 L18.4 9.2"/>
</g>
"""

def style(path: Path) -> None:
    svg = path.read_text(encoding="utf-8")
    if 'id="pythonScales"' in svg:
        return
    svg = svg.replace(">", ">" + DEFS, 1)
    pattern = re.compile(r'<rect class="s s0"[^>]*/>')
    svg, count = pattern.subn(HEAD, svg, count=1)
    if count != 1:
        raise SystemExit(f"Could not find moving snake head in {path}")
    # Add the scale texture over each of the three trailing animated body blocks.
    for n in range(1, 4):
        match = re.search(rf'(<rect class="s s{n}"[^>]*/>)', svg)
        if not match:
            raise SystemExit(f"Could not find moving body segment s{n} in {path}")
        tag = match.group(1)
        attrs = re.search(r' x="([^"]+)" y="([^"]+)"', tag)
        if not attrs:
            raise SystemExit(f"Could not read body position s{n} in {path}")
        x, y = attrs.groups()
        overlay = f'<rect class="snake-scales" x="{x}" y="{y}" width="16" height="16" rx="5" ry="5"/>'
        svg = svg.replace(tag, tag + overlay, 1)
    path.write_text(svg, encoding="utf-8")

if __name__ == "__main__":
    for name in sys.argv[1:]:
        style(Path(name))
