from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, shutil, html

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / 'assets'
A.mkdir(exist_ok=True)
SOURCE = Path('C:/Users/吴海睿/.codex/generated_images/01a16857-42b0-7fe3-b687-4197436087bc/exec-d060d82e-3e82-4df0-bef6-6fbd0f68cf17.png')
shutil.copy2(SOURCE, A / 'gpt-dragon.png')
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

projects=[('ai-glasses-platform','AI 眼镜组件平台','组件发布 · 分享 · AI 工具箱'),('smart-glasses-management','智能眼镜管理系统','微信小程序 · 设备管理'),('web','Web 项目','浏览项目源码'),('douban-top250-analysis','豆瓣 Top250 数据分析','电影数据 · 清洗 · 可视化')]
for i,(slug,title,desc) in enumerate(projects,1):
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="780" height="236" viewBox="0 0 780 236"><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#151722"/><stop offset="1" stop-color="#292339"/></linearGradient><radialGradient id="shine"><stop stop-color="#9784d4" stop-opacity=".22"/><stop offset="1" stop-color="#9784d4" stop-opacity="0"/></radialGradient></defs><rect x="1" y="1" width="778" height="234" rx="24" fill="url(#bg)" stroke="#514761"/><ellipse cx="690" cy="205" rx="220" ry="150" fill="url(#shine)"/><g font-family="Segoe UI,Microsoft YaHei,Arial,sans-serif"><text x="32" y="43" fill="#b8a7de" font-size="16">0{i} / PROJECT</text><text x="32" y="89" fill="#f2eefa" font-size="28" font-weight="600">{title}</text><text x="32" y="131" fill="#c1b8d4" font-size="19">{desc}</text><text x="32" y="194" fill="#9d94b3" font-size="17">{slug}</text><text x="715" y="195" fill="#d0bfff" font-size="28">↗</text></g></svg>'''
    (A/f'project-{i}.svg').write_text(svg,encoding='utf-8')

readme='''<p align="center">
  <img src="assets/hero.png" width="100%" alt="Hi, I’m why. 把想法，做成作品。黑紫液态玻璃背景与白发 Q 版龙娘。" />
</p>

<h2>精选项目 <sub>Selected projects</sub></h2>

'''
for i,(slug,title,desc) in enumerate(projects,1):
    readme+=f'<a href="https://github.com/libra-sys/{slug}"><img src="assets/project-{i}.svg" width="49%" alt="{title}：{desc}。打开 {slug} 仓库" /></a>\n'
readme+='''
<p align="center">
  <sub>探索 · 构建 · 迭代</sub><br />
  <a href="https://github.com/libra-sys?tab=repositories">查看全部公开仓库 ↗</a>
</p>

<!-- Visual source and maintenance notes: docs/DESIGN.md -->
'''
(ROOT/'README.md').write_text(readme,encoding='utf-8')
print('Built hero, transparent mascot, four SVG cards and README.')
