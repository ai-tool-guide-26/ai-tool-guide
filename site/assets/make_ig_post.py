from PIL import Image, ImageDraw, ImageFont
import os

W = H = 1080
out = r'C:\Users\hirom\AppData\Local\Temp\opencode\ig-ai-writing-1080.png'

img = Image.new('RGB', (W, H), '#f8fafc')
d = ImageDraw.Draw(img)

# Header
d.rectangle([0, 0, W, 200], fill='#16324f')
d.rectangle([0, 196, W, 200], fill='#0e7490')

fp = None
for p in ['C:/Windows/Fonts/meiryo.ttc','C:/Windows/Fonts/meiryob.ttc','C:/Windows/Fonts/YuGothM.ttc','C:/Windows/Fonts/msgothic.ttc']:
    if os.path.exists(p):
        fp = p
        break

def font(sz):
    if fp:
        try: return ImageFont.truetype(fp, sz)
        except: pass
    return ImageFont.load_default()

d.text((60, 60), 'AIライティング比較 2026', font=font(56), fill='white')

rows = [
    ('Value AI Writer', '日本語SEO・円建て', '月840円〜', '#0e7490'),
    ('Writesonic', '英語記事・多言語', 'トライアルあり', '#1e293b'),
    ('Surfer', 'SEO分析・最適化', '分析重視', '#334155'),
]

y = 250
for name, desc, note, color in rows:
    d.rounded_rectangle([60, y, W-60, y+200], radius=20, fill='white', outline='#dce4ec', width=3)
    d.rounded_rectangle([60, y, 72, y+200], radius=6, fill=color)
    d.text((100, y+30), name, font=font(46), fill='#16324f')
    d.text((100, y+100), desc, font=font(36), fill='#334155')
    d.text((100, y+150), note, font=font(34), fill=color)
    y += 225

d.rectangle([0, H-100, W, H], fill='#16324f')
d.text((60, H-70), '「最強」より「あなたの言語と目的」で選ぶ', font=font(40), fill='white')

img.save(out, 'PNG')
print('saved', out, img.size)
