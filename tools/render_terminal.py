"""Render the terminal portrait from the profile's real photo (Pillow and NumPy)."""
from pathlib import Path
import math
import json

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'neon-terminal'
W, H = 1000, 590
BG = '#05091a'
CYAN = '#65e6ff'
WHITE = '#edf3ff'
PURPLE = '#b493ff'


def font(size, bold=False):
    file = 'DejaVuSansMono-Bold.ttf' if bold else 'DejaVuSansMono.ttf'
    return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/' + file, size)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    base = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(base)
    # Opaque backgrounds keep every frame clean in GitHub's dark and light themes.
    for width, color in [(10, '#101537'), (6, '#1a2b59'), (3, '#3565d3')]:
        draw.rounded_rectangle((12, 76, 987, 565), radius=17, outline=color, width=width)
    draw.rounded_rectangle((17, 81, 982, 560), radius=13, fill='#08122b', outline='#65e6ff', width=1)
    draw.line((30, 82, 966, 82), fill='#72e6ff', width=2)
    for x, c in [(38, '#ff7998'), (54, '#ffd377'), (70, '#69e6ba')]:
        draw.ellipse((x-4, 94-4, x+4, 94+4), fill=c)
    draw.text((93, 85), 'nitesh@github : profile', font=font(13), fill='#d0dafe')
    draw.text((751, 85), 'Nitesh-Datascience', font=font(13), fill='#8fbde7')
    draw.text((38, 113), 'VISUAL.MAP', font=font(12, True), fill='#a4bde9')
    draw.text((418, 113), 'PROFILE.INFO', font=font(12, True), fill='#a4bde9')
    draw.rounded_rectangle((36, 135, 391, 517), radius=6, fill='#051027', outline='#308bb6', width=2)
    draw.line((36, 135, 75, 135), fill=CYAN, width=3)
    draw.line((36, 135, 36, 174), fill=CYAN, width=3)
    draw.line((352, 517, 391, 517), fill=CYAN, width=3)
    draw.line((391, 478, 391, 517), fill=CYAN, width=3)
    draw.rounded_rectangle((418, 135, 960, 517), radius=8, fill='#09152c', outline='#273d67', width=1)
    draw.text((439, 149), 'Nitesh Kumar', font=font(26, True), fill=WHITE)
    draw.rounded_rectangle((439, 184, 664, 209), radius=4, fill='#6143be')
    draw.text((448, 187), 'Nitesh-Datascience', font=font(16, True), fill=WHITE)
    fields = [
        ('Role', 'Data Analyst'), ('Focus', 'BI / Machine Learning'),
        ('Location', 'Delhi, India'), ('Education', 'BCA graduate'),
        ('Core tools', 'Python / SQL / Excel / Power BI'),
        ('Builds', 'Dashboards / Forecasting / ML'),
        ('Workflow', 'Git / GitHub / Jupyter'),
        ('Status', 'Open to entry-level roles'),
        ('Email', 'ns0762005@gmail.com'),
    ]
    for i, (label, value) in enumerate(fields):
        y = 224 + i * 29
        draw.text((439, y), label, font=font(15, True), fill=CYAN)
        draw.text((563, y), ': ' + value, font=font(15), fill='#dbe5fb')
    draw.text((44, 531), 'DATA  /  INSIGHTS  /  DECISIONS', font=font(12), fill='#94cce2')
    draw.text((418, 531), 'Portfolio · Projects · Skills · Connect', font=font(12), fill='#a79ee5')

    photo = Image.open(OUT / 'portrait-source.png').convert('RGB')
    # A crop of the actual photo preserves the user's own hair, eyes, moustache and face shape.
    photo = photo.crop((86, 12, 357, 334)).resize((302, 350), Image.Resampling.LANCZOS)
    rgb = np.asarray(photo).astype(float)
    lum = rgb @ np.array([.2126, .7152, .0722])
    yy, xx = np.mgrid[:350, :302]
    elliptical = ((xx - 151)/145)**2 + ((yy - 174)/183)**2 < 1
    mask = (rgb.min(axis=2) < 233) & elliptical
    gx, gy = np.gradient(lum)
    edge = np.minimum(np.sqrt(gx*gx+gy*gy)/55, 1)
    contrasted = np.clip((lum - 30) / 190, 0, 1)
    strength = np.clip(.93 * contrasted**1.5 + .08 * edge, 0, 1)
    points = []
    for y in range(0, 350, 3):
        for x in range(0, 302, 3):
            if mask[y, x]:
                points.append((x + 61, y + 151, strength[y, x]))
    rng = np.random.default_rng(220066242)
    scatter = rng.uniform((55, 148), (376, 500), size=(len(points), 2))
    jitters = rng.uniform(0, math.tau, len(points))
    # A low-contrast, masked layer of the same photograph gives the assembled portrait definition.
    under = np.zeros((350,302,3), dtype=np.uint8)
    under[:, :, 0] = np.clip(contrasted*150, 0, 255)
    under[:, :, 1] = np.clip(contrasted*185, 0, 255)
    under[:, :, 2] = np.clip(contrasted*235, 0, 255)
    under_image = Image.fromarray(under)

    phases = [0.0] + list(np.linspace(0, 1, 10)) + [1]*4 + list(np.linspace(1, 0, 14)) + [0]*13
    frames, durations = [], []
    role = 'Data Analyst | Python · SQL · Excel · Power BI | AI & ML'
    message = 'Building dashboards. Turning data into insights.'
    for i, phase in enumerate(phases):
        frame = base.copy()
        d = ImageDraw.Draw(frame)
        text = role if i < 16 else message[:min(len(message), (i - 16) * 2 + 1)]
        text_width = d.textlength(text, font=font(23, True))
        d.text(((W - text_width)/2, 29), text, font=font(23, True), fill=WHITE)
        if i >= 16 and len(text)<len(message):
            x = (W+text_width)/2+5
            d.rectangle((x, 34, x+8, 52), fill=CYAN)
        opacity = int(165*(1-phase)**3)
        if opacity:
            alpha = Image.fromarray((mask*opacity).astype('uint8'))
            frame.paste(under_image, (61,151), alpha)
        d = ImageDraw.Draw(frame)
        for p, (x, y, s) in enumerate(points):
            px = x*(1-phase) + scatter[p, 0]*phase + math.sin(i*.18 + jitters[p])*phase*4
            py = y*(1-phase) + scatter[p, 1]*phase + math.cos(i*.15 + jitters[p])*phase*4
            # The color follows the source photo: bright skin, darker hair and facial features.
            color = (round(15+s*228), round(23+s*226), round(45+s*210))
            r = .35 + s*.88
            d.ellipse((px-r, py-r, px+r, py+r), fill=color)
        if phase:
            scan_y = 151 + ((i*14) % 350)
            d.line((48, scan_y, 380, scan_y), fill='#204367', width=1)
        frames.append(frame)
        durations.append(1700 if i in (0,len(phases)-1) else 90)
    # One palette keeps text and borders stable as particles move.
    palette = frames[0].quantize(colors=128)
    frames = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
    frames[0].save(OUT / 'terminal.gif', save_all=True, append_images=frames[1:],
                   duration=durations, loop=0, optimize=True, disposal=1)
    print(json.dumps({'frames':len(frames),'particles':len(points),'gif_bytes':(OUT/'terminal.gif').stat().st_size}))


if __name__ == '__main__':
    main()
