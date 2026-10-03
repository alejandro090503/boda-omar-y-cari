import numpy as np, qrcode
from PIL import Image, ImageFilter, ImageOps
P='C:/Users/aleja/boda-omar-y-cari/'
F='fotos/'
def save(im,name,w,q=80):
    im=ImageOps.exif_transpose(im).convert('RGB')
    if im.width>w: im=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
    im.save(P+name,'WEBP',quality=q,method=6)
    print(name,im.size)
save(Image.open(F+'c5.jpg'),'hero.webp',1100,78)
save(Image.open(F+'c3.jpg'),'foto-pasto.webp',1200,78)
for k,i in enumerate([1,6,4,2,8,11,12,9,7,10]):
    im=ImageOps.exif_transpose(Image.open(F+f'c{i}.jpg'))
    # recorte 2:3 vertical
    w,h=im.size; tw=min(w,round(h*2/3)); th=round(tw*3/2)
    im=im.crop(((w-tw)//2,(h-th)//2,(w-tw)//2+tw,(h-th)//2+th))
    save(im,f'g{k+1}.webp',640,76)
# OG 1200x630 desde la portada
im=ImageOps.exif_transpose(Image.open(F+'c5.jpg')).convert('RGB')
w,h=im.size; th=round(w*630/1200); y=int(h*0.30)
im.crop((0,y,w,y+th)).resize((1200,630),Image.LANCZOS).save(P+'og-image.jpg',quality=84)
# Ramas de olivo (dibujo)
for src,name in [('ref/ex/img03_x268.png','rama-oscura.webp'),('ref/ex/img08_x292.png','rama-clara.webp')]:
    im=Image.open(src).convert('RGBA'); im=im.crop(im.getbbox()); im.thumbnail((340,400),Image.LANCZOS)
    im.save(P+name,'WEBP',quality=82,method=6); print(name,im.size)
im=Image.open('ref/logo_oc.png'); im.save(P+'logo-oc.png',optimize=True); im.save(P+'logo-oc.webp','WEBP',quality=88)
# QR nítido del álbum
q=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=12,border=2)
q.add_data('https://www.wedtrove.com/event/fvpcqTUt1G'); q.make(fit=True)
q.make_image(fill_color=(53,56,36),back_color=(248,244,234)).convert('RGB').save(P+'album-qr.png',optimize=True)
# Textura papel grueso (tile 512, neutra, se multiplica sobre el color)
rng=np.random.default_rng(7); N=512
def fbm(oct=5):
    acc=np.zeros((N,N));amp=1;tot=0
    for o in range(oct):
        s=2**(o+2); g=rng.random((s,s))
        g=np.tile(g,(1,1))
        im=Image.fromarray((g*255).astype(np.uint8)).resize((N,N),Image.BICUBIC)
        acc+=amp*np.asarray(im,float)/255; tot+=amp; amp*=0.55
    return acc/tot
base=fbm()
grain=rng.normal(0,1,(N,N)); grain=np.asarray(Image.fromarray(((grain*30)+128).clip(0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.6)),float)/255-0.5
# fibras
fib=Image.new('L',(N,N),0)
from PIL import ImageDraw
d=ImageDraw.Draw(fib)
for _ in range(900):
    x,y=rng.random()*N,rng.random()*N; a=rng.random()*np.pi; L=6+rng.random()*22
    pts=[]
    for t in np.linspace(0,1,6):
        pts.append((x+np.cos(a)*L*t+np.sin(t*3)*1.5,y+np.sin(a)*L*t))
    d.line(pts,fill=int(40+rng.random()*70),width=1)
fib=np.asarray(fib.filter(ImageFilter.GaussianBlur(.7)),float)/255
v=0.93+ (base-0.5)*0.10 + grain*0.07 - fib*0.10 + 0.0
v=v.clip(0,1)
# hacerlo seamless: mezcla con versión desplazada
sh=np.roll(np.roll(v,N//2,0),N//2,1)
yy,xx=np.mgrid[0:N,0:N]; m=np.minimum(np.minimum(xx,N-1-xx),np.minimum(yy,N-1-yy))/(N/2); m=np.clip(m*2.2,0,1)
v=v*m+sh*(1-m)
Image.fromarray((v*255).astype(np.uint8)).convert('RGB').save(P+'papel.webp','WEBP',quality=70)
print('papel ok')
