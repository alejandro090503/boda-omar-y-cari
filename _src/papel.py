import numpy as np
from PIL import Image, ImageFilter, ImageDraw
rng=np.random.default_rng(11); N=512
def tilenoise(scale,blur):
    g=rng.random((N//scale,N//scale))
    im=Image.fromarray((g*255).astype(np.uint8))
    # wrap-around upscale para que sea seamless
    big=np.tile(np.asarray(im),(3,3))
    big=Image.fromarray(big).resize((N*3,N*3),Image.BICUBIC).filter(ImageFilter.GaussianBlur(blur))
    return np.asarray(big,float)[N:2*N,N:2*N]/255
h = 0.6*tilenoise(32,6)+0.45*tilenoise(8,2.5)+0.22*tilenoise(4,1.4)+0.08*tilenoise(1,.7)
fib=Image.new('L',(N*3,N*3),0); d=ImageDraw.Draw(fib)
for _ in range(1400):
    x,y=rng.random()*N+N,rng.random()*N+N; a=rng.random()*np.pi*2; L=5+rng.random()*26; c=rng.random()*.25-.12
    pts=[(x+np.cos(a+c*t*6)*L*t,y+np.sin(a+c*t*6)*L*t) for t in np.linspace(0,1,8)]
    for ox in (-N,0,N):
        for oy in (-N,0,N):
            d.line([(p[0]+ox,p[1]+oy) for p in pts],fill=int(60+rng.random()*120),width=1)
fib=np.asarray(fib.filter(ImageFilter.GaussianBlur(.6)),float)[N:2*N,N:2*N]/255
h = h + fib*0.35
gy,gx=np.gradient(h)
shade = (-gx*0.75 - gy*0.6)*3.2      # relieve con luz arriba-izquierda
v = 0.95 + shade + (h-h.mean())*0.06 - fib*0.045
v=v.clip(0.78,1)
Image.fromarray((v*255).astype(np.uint8)).save('C:/Users/aleja/boda-omar-y-cari/_src/papel-base.png')

# Texturas ya teñidas (sin background-blend-mode: más ligero en iPhone)
def tinted(hexcol, k, name):
    t = 1 - (1 - v) * k
    c = np.array([int(hexcol[i:i+2], 16) for i in (1, 3, 5)], float)
    Image.fromarray((t[..., None] * c).clip(0, 255).astype(np.uint8)).save('C:/Users/aleja/boda-omar-y-cari/' + name, 'WEBP', quality=84)

tinted('#b4b897', .26, 'tx-salvia.webp')
tinted('#5f624a', .30, 'tx-olivo.webp')
tinted('#f4efe4', .3, 'tx-papel.webp')
tinted('#e6e4d6', .36, 'tx-flip.webp')
tinted('#ebe2ce', .40, 'tx-sobre.webp')
