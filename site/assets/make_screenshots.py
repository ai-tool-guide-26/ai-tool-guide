from PIL import Image
import os, shutil

src_dir = r'C:\Users\hirom\AppData\Local\Temp\opencode'
out_dir = os.path.dirname(os.path.abspath(__file__))

# map temp screenshot -> site asset name
items = [
    ('hp-miricanvas.png', 'screen-miricanvas'),
    ('hp-hp-valueai.png', 'screen-valueai'),
    ('hp-hp-elevenlabs.png', 'screen-elevenlabs'),
    ('hp-hp-gamma.png', 'screen-gamma'),
    ('hp-hp-conoha.png', 'screen-conoha'),
]

for src_name, out_name in items:
    src = os.path.join(src_dir, src_name)
    if not os.path.exists(src):
        print('skip (missing)', src)
        continue
    im = Image.open(src).convert('RGB')
    w, h = im.size
    # crop to top portion to keep a clean 'first screen' view
    crop_h = min(h, 1200)
    im = im.crop((0, 0, w, crop_h))
    # resize to max width 1000 for web
    if im.width > 1000:
        ratio = 1000 / im.width
        im = im.resize((1000, int(im.height * ratio)), Image.LANCZOS)
    out = os.path.join(out_dir, out_name + '.jpg')
    im.save(out, 'JPEG', quality=85, optimize=True)
    print('saved', out, im.size)
