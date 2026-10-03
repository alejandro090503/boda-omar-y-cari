# v3: hero con Ken Burns + haz de luz (receta gabriela-y-ulises), polvo dorado
# suave (receta yenisei-y-juan-carlos) y botón de música en vinilo.
import re, pathlib
p = pathlib.Path(__file__).parent / 'template.html'
s = p.read_text(encoding='utf-8')

def rep(a, b):
    global s
    assert a in s, 'NO ENCONTRADO: ' + a[:80]
    s = s.replace(a, b, 1)

# ---------- Vinilo ----------
s = re.sub(r"\.music-btn\{\n.*?@keyframes mPulse\{[^\n]*\}\n", r"""/* Música: disco de vinilo (receta de invitaciones recientes) en paleta salvia */
.vinyl-btn{position:fixed;bottom:18px;right:16px;z-index:9000;width:68px;height:68px;border-radius:50%;padding:0;border:none;cursor:pointer;background:transparent;opacity:0;transform:scale(.6);pointer-events:none;transition:transform .35s cubic-bezier(.2,.7,.2,1),opacity .35s;box-shadow:0 6px 18px rgba(30,32,18,.45),0 0 0 1px rgba(176,141,74,.25);-webkit-tap-highlight-color:transparent}
.vinyl-btn.is-ready{opacity:1;transform:scale(1);pointer-events:auto}
.vinyl-btn:hover{transform:scale(1.1)}
.vinyl-btn:active{transform:scale(.94)}
.vinyl-spin{width:100%;height:100%;border-radius:50%;position:relative}
.vinyl-btn.is-playing .vinyl-spin{animation:vinylSpin 1.8s linear infinite}
@keyframes vinylSpin{to{transform:rotate(360deg)}}
.vinyl-disc{width:100%;height:100%;border-radius:50%;overflow:hidden;position:relative;
  background:radial-gradient(circle,#1d1f14 4%,transparent 4.5%),radial-gradient(circle,#c9cdb0 0%,#b4b897 15%,#5f624a 18.5%,transparent 19%),
  repeating-radial-gradient(circle,transparent 20%,rgba(255,255,255,.055) 20.8%,transparent 21.5%,transparent 24%,rgba(255,255,255,.04) 24.8%,transparent 25.5%),
  radial-gradient(circle,#1d1f14 0%,#15160e 60%,#1d1f14 100%);box-shadow:inset 0 0 8px rgba(0,0,0,.45)}
.vinyl-sheen{position:absolute;inset:0;border-radius:50%;background:linear-gradient(135deg,transparent 30%,rgba(255,255,255,.09) 42%,rgba(255,255,255,.16) 48%,rgba(255,255,255,.09) 54%,transparent 66%);pointer-events:none}
.vinyl-label{position:absolute;top:50%;left:50%;width:30%;height:auto;transform:translate(-50%,-50%);opacity:.9;pointer-events:none}
.vinyl-hole{position:absolute;top:50%;left:50%;width:5px;height:5px;transform:translate(-50%,-50%);border-radius:50%;background:#1d1f14;box-shadow:0 0 0 1.5px rgba(176,141,74,.55)}
.vinyl-icons{position:absolute;left:50%;bottom:-3px;transform:translateX(-50%);width:22px;height:22px;border-radius:50%;background:var(--crema);border:1.5px solid var(--musgo);display:flex;align-items:center;justify-content:center;pointer-events:none;z-index:2}
.vinyl-icons svg{width:10px;height:10px;fill:var(--musgo)}
.vinyl-icon-pause{display:none}
.vinyl-btn.is-playing .vinyl-icon-play{display:none}
.vinyl-btn.is-playing .vinyl-icon-pause{display:block}
.vinyl-btn::after{content:"";position:absolute;inset:-5px;border-radius:50%;border:1px solid #b08d4a;opacity:.35;animation:vinylPulse 3s ease-in-out infinite}
.vinyl-btn.is-playing::after{animation-duration:1.6s}
@keyframes vinylPulse{0%,100%{transform:scale(1);opacity:.35}50%{transform:scale(1.13);opacity:.05}}
.vinyl-tonearm{position:absolute;top:-4px;right:-2px;width:24px;height:34px;transform-origin:top right;transform:rotate(-28deg);transition:transform .6s cubic-bezier(.2,.7,.2,1);pointer-events:none;z-index:1}
.vinyl-btn.is-playing .vinyl-tonearm{transform:rotate(-12deg)}
.vinyl-tonearm-line{position:absolute;top:2px;right:4px;width:2px;height:28px;background:linear-gradient(to bottom,#8a6a2e,#c4a05a 40%,#8a6a2e);border-radius:1px;transform:rotate(-5deg);transform-origin:top center}
.vinyl-tonearm-head{position:absolute;bottom:0;right:2px;width:5px;height:6px;background:#b08d4a;border-radius:0 0 2px 2px}
.vinyl-tonearm-pivot{position:absolute;top:0;right:2px;width:7px;height:7px;background:radial-gradient(circle,#f1e8d9,#b08d4a);border-radius:50%;box-shadow:0 1px 3px rgba(0,0,0,.3)}
""", s, count=1, flags=re.S)
rep("""<button class="music-btn" id="music-btn" type="button" aria-label="Música">
  <img src="logo-oc.webp" alt="">
  <span class="mb-ico">
    <svg class="i-play" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
    <svg class="i-pause" viewBox="0 0 24 24"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
  </span>
</button>""", """<button class="vinyl-btn" id="music-btn" type="button" aria-label="Música">
  <div class="vinyl-tonearm"><div class="vinyl-tonearm-pivot"></div><div class="vinyl-tonearm-line"></div><div class="vinyl-tonearm-head"></div></div>
  <div class="vinyl-spin"><div class="vinyl-disc"><div class="vinyl-sheen"></div><img class="vinyl-label" src="logo-oc.webp" alt=""><div class="vinyl-hole"></div></div></div>
  <div class="vinyl-icons">
    <svg class="vinyl-icon-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
    <svg class="vinyl-icon-pause" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>
  </div>
</button>""")
rep(".pill,.copy-btn,.rsvp-edit,.person-tg button,.lang-btn button,.music-btn{", ".pill,.copy-btn,.rsvp-edit,.person-tg button,.lang-btn button{")
rep(""".music-btn:not(.is-playing).is-ready{animation:musicoLlama 2.6s ease-in-out infinite}
@keyframes musicoLlama{0%,100%{transform:scale(1)}8%{transform:scale(1.12) rotate(-6deg)}16%{transform:scale(1) rotate(4deg)}24%{transform:scale(1)}}
""", "")
rep(".flip-more svg,.flip-more::after,.music-btn{animation:none!important}", ".flip-more svg,.flip-more::after,.vinyl-btn::after,.hero-img,.hero-shimmer::after{animation:none!important}")

# ---------- Hero: la foto se mueve en su espacio y la cruza un brillo suave ----------
rep(".hero-veil{position:absolute;inset:0;pointer-events:none;", """/* Ken Burns: la foto respira dentro de su marco */
.hero-img{animation:kenBurns 24s ease-in-out infinite;transform-origin:50% 40%}
@keyframes kenBurns{0%{transform:scale(1.06) translate(0,0)}33%{transform:scale(1.11) translate(-1.5%,-.5%)}66%{transform:scale(1.09) translate(.8%,-1%)}100%{transform:scale(1.06) translate(0,0)}}
/* Haz de luz diagonal que cruza la foto (con la misma máscara para no pintar el fundido) */
.hero-shimmer{position:absolute;inset:0;pointer-events:none;overflow:hidden;
  -webkit-mask-image:linear-gradient(to bottom,#000 0%,#000 56%,rgba(0,0,0,.6) 76%,rgba(0,0,0,0) 96%);
          mask-image:linear-gradient(to bottom,#000 0%,#000 56%,rgba(0,0,0,.6) 76%,rgba(0,0,0,0) 96%)}
.hero-shimmer::after{content:"";position:absolute;top:0;left:-60%;width:60%;height:100%;
  background:linear-gradient(105deg,transparent 20%,rgba(255,240,205,.07) 42%,rgba(255,244,214,.2) 52%,rgba(255,240,205,.07) 60%,transparent 78%);
  animation:heroBeam 9s ease-in-out infinite 2.5s}
@keyframes heroBeam{0%{left:-60%}55%{left:125%}100%{left:125%}}
.hero-veil{position:absolute;inset:0;pointer-events:none;""")
rep("""<img class="hero-img" src="hero.webp" alt="Omar y Cari en el bosque" fetchpriority="high"><div class="hero-veil"></div></div>""",
    """<img class="hero-img" src="hero.webp" alt="Omar y Cari en el bosque" fetchpriority="high"><div class="hero-veil"></div><div class="hero-shimmer"></div></div>""")
# La entrada ya no escala la foto (lo hace el Ken Burns en CSS): solo aparece
rep("tl.fromTo('.hero-img',{scale:1.12},{scale:1,duration:2.6,ease:'power2.out'},0)",
    "tl.fromTo('.hero-img',{opacity:0},{opacity:1,duration:1.6,ease:'power2.out'},0)")

# ---------- Partículas: polvo dorado lento y suave con destellos de 4 puntas ----------
s = re.sub(r"/\* ================= PARTÍCULAS:.*?\n\}\)\(\);\n", r"""/* ================= PARTÍCULAS: polvo dorado suave (receta yenisei-y-juan-carlos) ================= */
var startParticles = (function(){
  var cv = document.getElementById('particulas');
  if(!cv || prefersReduced || !cv.getContext) return function(){};
  var ctx = cv.getContext('2d'), dpr = Math.min(window.devicePixelRatio || 1, 1.5);
  var W = 0, H = 0, P = [], running = false, last = 0;
  var mobile = innerWidth < 768, N = mobile ? 18 : 32;
  var cols = ['255,246,220','232,210,150','201,168,96'];
  function size(){ W = innerWidth; H = innerHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr,0,0,dpr,0,0); }
  function mk(top){
    return { x: Math.random() * W, y: top ? -10 - Math.random() * 40 : Math.random() * H,
      r: .6 + Math.random() * (mobile ? 1.4 : 1.9), vy: .1 + Math.random() * .22,
      sw: Math.random() * 6.28, sws: .0024 + Math.random() * .005, tw: Math.random() * 6.28,
      star: Math.random() < .26, c: cols[(Math.random() * 3) | 0] };
  }
  function draw(p, a){
    ctx.globalAlpha = a; ctx.fillStyle = 'rgba(' + p.c + ',1)';
    if(p.star){
      var s = p.r * 3.2; ctx.beginPath();
      ctx.moveTo(p.x, p.y - s); ctx.quadraticCurveTo(p.x, p.y, p.x + s, p.y);
      ctx.quadraticCurveTo(p.x, p.y, p.x, p.y + s); ctx.quadraticCurveTo(p.x, p.y, p.x - s, p.y);
      ctx.quadraticCurveTo(p.x, p.y, p.x, p.y - s); ctx.fill();
    } else { ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 6.2832); ctx.fill(); }
  }
  function loop(t){
    if(!running) return;
    var dt = Math.min(3, (t - last) / 16.7 || 1); last = t;
    ctx.clearRect(0, 0, W, H);
    for(var i = 0; i < P.length; i++){
      var p = P[i];
      p.y += p.vy * dt; p.sw += p.sws * dt; p.tw += .02 * dt; p.x += Math.sin(p.sw) * .15 * dt;
      if(p.y > H + 12) P[i] = p = mk(true);
      draw(p, (.3 + .45 * Math.abs(Math.sin(p.tw))) * (p.star ? 1 : .8));
    }
    ctx.globalAlpha = 1;
    requestAnimationFrame(loop);
  }
  addEventListener('resize', size);
  document.addEventListener('visibilitychange', function(){
    if(document.hidden) running = false;
    else if(P.length && !running){ running = true; last = performance.now(); requestAnimationFrame(loop); }
  });
  return function(){
    if(running) return;
    size(); P = []; for(var i = 0; i < N; i++) P.push(mk(false));
    running = true; last = performance.now(); requestAnimationFrame(loop);
  };
})();
""", s, count=1, flags=re.S)
rep("#particulas{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:60;opacity:.8}",
    "#particulas{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:60}")

p.write_text(s, encoding='utf-8')
print('ok')
