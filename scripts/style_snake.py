#!/usr/bin/env python3
"""Style the moving contribution-snake segments with a python-inspired skin."""
from pathlib import Path
import re
import sys

DEFS = """
<defs>
  <linearGradient id="pythonBody" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#c58a45"/>
    <stop offset=".48" stop-color="#9b5a2e"/>
    <stop offset="1" stop-color="#60391f"/>
  </linearGradient>
  <linearGradient id="pythonHead" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#d39a54"/>
    <stop offset=".55" stop-color="#8b512c"/>
    <stop offset="1" stop-color="#171512"/>
  </linearGradient>
  <pattern id="pythonScales" width="8" height="7" patternUnits="userSpaceOnUse">
    <rect width="8" height="7" fill="url(#pythonBody)"/>
    <path d="M0 2 Q2 0 4 2 Q6 4 8 2 M-4 5 Q-2 3 0 5 Q2 7 4 5 Q6 3 8 5"
      fill="none" stroke="#f0c27a" stroke-opacity=".48" stroke-width=".8"/>
    <path d="M0 2 Q2 4 4 2" fill="none" stroke="#4b2c18" stroke-opacity=".7" stroke-width=".6"/>
  </pattern>
  <filter id="pythonShadow" x="-40%" y="-40%" width="180%" height="180%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="1.2" result="blur"/>
    <feOffset dy="1" in="blur" result="offset"/>
    <feComponentTransfer in="offset" result="shadow">
      <feFuncA type="linear" slope=".55"/>
    </feComponentTransfer>
    <feMerge><feMergeNode in="shadow"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<style>
  .s { fill: url(#pythonScales) !important; stroke: #4b2c18; stroke-width: 1.1px; filter: url(#pythonShadow); }
  rect.s { rx: 5px; ry: 5px; }
  .snake-head { fill: url(#pythonHead); stroke: #17120d; stroke-width: 1px; }
  .snake-scales { fill: url(#pythonScales); opacity: .9; }
  .snake-eye { fill: #fff0a8; stroke: #17120d; stroke-width: .7px; }
  .snake-pupil { fill: #2a160d; }
  .snake-nostril { fill: #e7ad61; }
  .snake-tongue { fill: none; stroke: #e34b32; stroke-width: 1.35px; stroke-linecap: round; stroke-linejoin: round; }
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
    svg, count = re.subn(r'<rect class="s s0"[^>]*/>', HEAD, svg, count=1)
    if count != 1:
        raise SystemExit(f"Could not find moving snake head in {path}")
    path.write_text(svg, encoding="utf-8")

if __name__ == "__main__":
    for name in sys.argv[1:]:
        style(Path(name))
