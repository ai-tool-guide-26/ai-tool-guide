from PIL import Image, ImageDraw, ImageFont
import os

assets = os.path.dirname(os.path.abspath(__file__))
SIZE = 800

# Create square canvas with navy->teal gradient
img = Image.new('RGB', (SIZE, SIZE), '#0f172a')
draw = ImageDraw.Draw(img)

# Diagonal gradient navy -> teal
c1 = (15, 23, 42)    # navy
c2 = (8, 145, 178)   # teal
for y in range(SIZE):
    for x in range(0, SIZE, 4):
        t = (x + y) / (2 * SIZE)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        draw.rectangle([x, y, x + 3, y], fill=(r, g, b))

# Inner subtle ring
draw.ellipse([70, 70, SIZE - 70, SIZE - 70], outline=(255, 255, 255, 40), width=3)

# Draw large white "A"
font_bold = None
for fp in ['C:/Windows/Fonts/arialbd.ttf', 'C:/Windows/Fonts/segoeuib.ttf', 'C:/Windows/Fonts/Arial.ttf']:
    if os.path.exists(fp):
        font_bold = ImageFont.truetype(fp, 420)
        break
if font_bold is None:
    font_bold = ImageFont.load_default()

text = 'A'
bbox = draw.textbbox((0, 0), text, font=font_bold)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
draw.text(((SIZE - tw) / 2 - bbox[0], (SIZE - th) / 2 - bbox[1] - 30), text, font=font_bold, fill='white')

# Sparkle (4-point star) top-right of A
sx, sy, sr = 590, 210, 55
star = [(sx, sy - sr), (sx + sr // 4, sy - sr // 4), (sx + sr, sy),
        (sx + sr // 4, sy + sr // 4), (sx, sy + sr), (sx - sr // 4, sy + sr // 4),
        (sx - sr, sy), (sx - sr // 4, sy - sr // 4)]
draw.polygon(star, fill='white')

# Smaller sparkle
sx2, sy2, sr2 = 190, 610, 30
star2 = [(sx2, sy2 - sr2), (sx2 + sr2 // 4, sy2 - sr2 // 4), (sx2 + sr2, sy2),
         (sx2 + sr2 // 4, sy2 + sr2 // 4), (sx2, sy2 + sr2), (sx2 - sr2 // 4, sy2 + sr2 // 4),
         (sx2 - sr2, sy2), (sx2 - sr2 // 4, sy2 - sr2 // 4)]
draw.polygon(star2, fill=(255, 255, 255, 220))

# Save PNG
out_png = os.path.join(assets, 'profile.png')
img.save(out_png, 'PNG')
print('saved', out_png)

# Save JPG copy
out_jpg = os.path.join(assets, 'profile.jpg')
img.convert('RGB').save(out_jpg, 'JPEG', quality=92)
print('saved', out_jpg)
