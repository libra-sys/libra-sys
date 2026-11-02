from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, shutil, html

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / 'assets'
A.mkdir(exist_ok=True)
SOURCE = A / 'gpt-dragon.png'
if not SOURCE.is_file():
    raise FileNotFoundError('Place the approved transparent mascot at assets/gpt-dragon.png')
W,H=1600,720
im=Image.new('RGB',(W,H)); px=im.load()
for y in range(H):
    for x in range(W):
        g=math.exp(-(((x-1230)/590)**2+((y-510)/410)**2))
        b=math.exp(-(((x-270)/650)**2+((y-770)/250)**2))
        px[x,y]=(int(10+35*g+10*b),int(12+24*g+15*b),int(20+66*g+32*b))
im=im.convert('RGBA')
glow=Image.new('RGBA',im.size); d=ImageDraw.Draw(glow)
d.arc((-340,390,1920,1300),190,332,fill=(114,109,231,170),width=72)
d.arc((320,-670,1930,410),2,175,fill=(181,179,244,105),width=35)
im=Image.alpha_composite(im,glow.filter(ImageFilter.GaussianBlur(27)))
d=ImageDraw.Draw(im)
d.arc((-340,510,1920,1420),190,332,fill=(128,122,178,255),width=2)
glass=Image.new('RGBA',im.size); gd=ImageDraw.Draw(glass)
gd.rounded_rectangle((45,42,1555,678),radius=46,fill=(150,153,193,18),outline=(221,221,255,70),width=2)
gd.line((90,43,1470,43),fill=(255,255,255,70),width=2)
im=Image.alpha_composite(im,glass)
mascot=Image.open(A/'gpt-dragon.png').convert('RGBA')
mascot.thumbnail((720,640),Image.Resampling.LANCZOS)
im.alpha_composite(mascot,(845,78))
d=ImageDraw.Draw(im)
def font(size,bold=False): return ImageFont.truetype('C:/Windows/Fonts/'+('msyhbd.ttc' if bold else 'msyh.ttc'),size)
d.text((105,107),'LIBRA-SYS  /  GITHUB',font=font(22),fill='#bab4d9')
d.text((100,191),'Hi, I’m why.',font=font(82,True),fill='#f7f5ff')
d.rounded_rectangle((106,315,182,321),3,fill='#b8a4ff')
d.text((105,355),'把想法，做成作品。',font=font(35),fill='#e5dff8')
d.text((107,424),'Explore. Build. Iterate.',font=font(25),fill='#aaa5c0')
for i,label in enumerate(['AI · 智能眼镜','Web · 应用','Data · 可视化']):
    x=105+i*233
    d.rounded_rectangle((x,531,x+214,583),26,fill='#302c44',outline='#5b526f',width=1)
    d.text((x+20,543),label,font=font(20),fill='#d8d2ed')
im.convert('RGB').save(A/'hero.png',optimize=True)

# Reuse the content-only builder so full visual rebuilds keep the current catalog.
import runpy
runpy.run_path(str(ROOT / 'tools' / 'build_catalog.py'), run_name='__main__')
