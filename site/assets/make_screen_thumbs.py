from PIL import Image
import os

out_dir = os.path.dirname(os.path.abspath(__file__))

# map full screenshot -> 16:9 thumbnail
items = [
    ('screen-miricanvas.jpg', 'screenthumb-miricanvas.jpg'),
    ('screen-valueai.jpg', 'screenthumb-valueai.jpg'),
    ('screen-conoha.jpg', 'screenthumb-conoha.jpg'),
    ('screen-elevenlabs.jpg', 'screenthumb-elevenlabs.jpg'),
    ('screen-gamma.jpg', 'screenthumb-gamma.jpg'),
]

for src_name, out_name in items:
    src = os.path.join(out_dir, src_name)
    if not os.path.exists(src):
        print('skip', src)
        continue
    im = Image.open(src).convert('RGB')
    w, h = im.size
    # crop a 16:9 region from the top of the screenshot
    target_h = int(w * 9 / 16)
    im = im.crop((0, 0, w, min(target_h, h)))
    im = im.resize((640, 360), Image.LANCZOS)
    out = os.path.join(out_dir, out_name)
    im.save(out, 'JPEG', quality=82, optimize=True)
    print('saved', out)
