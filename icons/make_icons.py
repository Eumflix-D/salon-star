# 홈 화면 아이콘 만들기 (python icons/make_icons.py)
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
import math
N=1024; G=(217,180,106); G2=(243,220,160)
bg=Image.open('img/rococo.webp').convert('RGB')
w,h=bg.size; m=min(w,h); bg=bg.crop(((w-m)//2,(h-m)//2,(w+m)//2,(h+m)//2)).resize((N,N))
bg=ImageEnhance.Brightness(bg.filter(ImageFilter.GaussianBlur(10))).enhance(.32)
im=bg.copy(); d=ImageDraw.Draw(im,'RGBA')
# 가운데 은은한 조명
glow=Image.new('L',(N,N),0); ImageDraw.Draw(glow).ellipse((212,150,812,750),fill=120)
glow=glow.filter(ImageFilter.GaussianBlur(120)); im.paste((255,214,140),(0,0),glow.point(lambda v:v*.45))
d=ImageDraw.Draw(im,'RGBA')
c=N//2
for r,wd in((400,10),(372,3)): d.ellipse((c-r,c-r,c+r,c+r),outline=G,width=wd)
# 테두리 점 장식
for i in range(24):
    a=i/24*2*math.pi; x=c+386*math.cos(a); y=c+386*math.sin(a); d.ellipse((x-7,y-7,x+7,y+7),fill=G2)
# 피아노 건반 (아래쪽)
kx,ky,kw,kh=262,610,500,150; n=10; ww=kw/n
d.rounded_rectangle((kx-8,ky-8,kx+kw+8,ky+kh+8),12,fill=(20,14,8),outline=G,width=4)
for i in range(n): d.rectangle((kx+i*ww+2,ky,kx+(i+1)*ww-2,ky+kh),fill=(246,238,222))
for i in (0,1,3,4,5,7,8):
    x=kx+(i+1)*ww; d.rectangle((x-ww*.3,ky,x+ww*.3,ky+kh*.6),fill=(18,12,8))
# 큰 S
f=ImageFont.truetype('C:/Windows/Fonts/georgiaz.ttf',430)
sh=Image.new('RGBA',(N,N),(0,0,0,0)); ds=ImageDraw.Draw(sh)
ds.text((c,395),'S',font=f,anchor='mm',fill=(0,0,0,200)); sh=sh.filter(ImageFilter.GaussianBlur(14))
im.paste(sh,(0,8),sh); d=ImageDraw.Draw(im,'RGBA')
d.text((c,395),'S',font=f,anchor='mm',fill=G2,stroke_width=6,stroke_fill=(120,84,30))
# 별
def star(cx,cy,R,r):
    pts=[(cx+(R if k%2==0 else r)*math.cos(-math.pi/2+k*math.pi/5),cy+(R if k%2==0 else r)*math.sin(-math.pi/2+k*math.pi/5)) for k in range(10)]
    d.polygon(pts,fill=(255,215,106),outline=(150,105,40))
star(690,215,62,26)
for s in (512,192,180):
    out=im.resize((s,s),Image.LANCZOS)
    out.save(f'icons/{"apple-touch-icon" if s==180 else "icon-%d"%s}.png',optimize=True)
im.resize((64,64),Image.LANCZOS).save('icons/favicon.png')
