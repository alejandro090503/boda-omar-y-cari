# v2: calendario iOS, dibujos que levitan, partículas, botones vivos,
# RSVP estilo boda-jennifer y hero que se funde (estilo boda-sebastian-y-diana).
import re, pathlib
p = pathlib.Path(__file__).parent / 'template.html'
s = p.read_text(encoding='utf-8')

def rep(a, b, count=1):
    global s
    assert a in s, 'NO ENCONTRADO: ' + a[:80]
    s = s.replace(a, b, count)

# ---------- HERO que se funde con la siguiente sección ----------
rep(""".hero{position:relative;height:100vh;height:100svh;min-height:560px;overflow:hidden;background:#2f3320}
.hero-img{position:absolute;inset:-6% 0 0;width:100%;height:106%;object-fit:cover;object-position:50% 30%}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(to bottom,rgba(30,32,18,0) 45%,rgba(30,32,18,.42) 100%)}
.hero-content{position:absolute;left:0;right:0;bottom:14%;""",
""".hero{position:relative;height:100vh;height:100svh;min-height:560px;overflow:hidden;background:transparent}
/* La máscara va en la capa de la foto (no en la sección) para no recortar los nombres:
   la foto se disuelve hacia abajo y deja ver el papel salvia de la página. */
.hero-media{position:absolute;inset:0;will-change:transform,opacity}
.hero-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 30%;
  -webkit-mask-image:linear-gradient(to bottom,#000 0%,#000 56%,rgba(0,0,0,.86) 72%,rgba(0,0,0,.45) 87%,rgba(0,0,0,0) 100%);
          mask-image:linear-gradient(to bottom,#000 0%,#000 56%,rgba(0,0,0,.86) 72%,rgba(0,0,0,.45) 87%,rgba(0,0,0,0) 100%)}
.hero-veil{position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(to bottom,rgba(30,32,18,.10) 0%,rgba(30,32,18,.02) 34%,rgba(30,32,18,.34) 60%,rgba(30,32,18,.50) 76%,rgba(30,32,18,.16) 92%,rgba(30,32,18,0) 100%)}
.hero-content{position:absolute;left:0;right:0;bottom:19%;""")
rep(".hero-name{font-family:var(--display);font-weight:400;font-size:clamp(40px,11.6vw,74px);line-height:1.05;letter-spacing:.01em;color:var(--crema);white-space:nowrap;text-shadow:0 2px 14px rgba(0,0,0,.25)}",
    ".hero-name{font-family:var(--display);font-weight:400;font-size:clamp(40px,11.6vw,74px);line-height:1.05;letter-spacing:.01em;color:var(--crema);white-space:nowrap;text-shadow:0 2px 18px rgba(30,32,18,.55)}")
rep("""    <img class="hero-img" src="hero.webp" alt="Omar y Cari en el bosque" fetchpriority="high">""",
    """    <div class="hero-media"><img class="hero-img" src="hero.webp" alt="Omar y Cari en el bosque" fetchpriority="high"><div class="hero-veil"></div></div>""")
rep(".quote{padding:54px 0 30px;text-align:center}", ".quote{padding:10px 0 30px;text-align:center;margin-top:-6vh;z-index:2}")
rep("""    gsap.to('.hero-img',{yPercent:8,ease:'none',scrollTrigger:{trigger:'.hero',start:'top top',end:'bottom top',scrub:true}});""",
"""    /* Al bajar: la foto se apaga, baja y crece un poco; los nombres se van antes */
    var hs = {trigger:'.hero',start:'top top',end:'bottom top',scrub:true};
    gsap.timeline({scrollTrigger:hs})
      .fromTo('.hero-media',{opacity:1,yPercent:0,scale:1},{opacity:0,yPercent:11,scale:1.06,ease:'none',duration:.78},0)
      .to({},{duration:.22});
    gsap.timeline({scrollTrigger:hs})
      .fromTo('.hero-content',{opacity:1,y:0},{opacity:0,y:-38,ease:'none',duration:.42},0)
      .to('.hero-scroll',{opacity:0,duration:.2,ease:'none'},0)
      .to({},{duration:.58});""")

# ---------- CALENDARIO: Google + iPhone ----------
rep("""        <a class="pill pill--crema" id="gcal" target="_blank" rel="noopener\"""",
    """        <div class="cal-row">
        <a class="pill pill--crema" id="gcal" target="_blank" rel="noopener\"""")
rep("""           data-i18n="gcal">Agregar a Google Calendar</a>""",
"""           ><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="4.5" width="18" height="16.5" rx="2.5"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4"/><path d="M8 14h3M13 14h3M8 17.5h3"/></svg><span data-i18n="gcal">Google Calendar</span></a>
        <a class="pill pill--crema" id="ical" href="boda-omar-y-cari.ics" download="boda-omar-y-cari.ics"
           ><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.1-1.7-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.8 0-1.9-.9-3.2-.8-1.6 0-3.1 1-4 2.4-1.7 3-.4 7.4 1.2 9.8.8 1.2 1.8 2.5 3 2.4 1.2 0 1.7-.8 3.1-.8 1.5 0 1.9.8 3.2.8 1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8-.1 0-2.5-1-2.5-3.9zM14 5.5c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 1 .1 2.1-.6 2.8-1.4z"/></svg><span data-i18n="ical">Calendario iPhone</span></a>
        </div>""")

# ---------- Dibujos que levitan (cada uno con su propio movimiento) ----------
def wrap_lev(icon, kind):
    global s
    pat = f'<svg class="ic" viewBox="{{{{VB:{icon}}}}}" aria-hidden="true"><use href="#ic-{icon}"/></svg>'
    assert pat in s, icon
    s = s.replace(pat, f'<span class="lev lev--{kind}">{pat}</span>')
for icon, kind in [('church','iglesia'),('couple','baile'),('dress','vestido'),('suit','traje'),
                   ('envelope','sobre'),('card','tarjeta'),('gift','regalo')]:
    wrap_lev(icon, kind)

# ---------- RSVP con el diseño de boda-jennifer ----------
s = re.sub(r"/\* RSVP \*/.*?/\* Footer \*/", r"""/* RSVP — diseño de boda-jennifer (tarjeta translúcida, filete doble, esquinas) en paleta salvia */
.rsvp{padding:34px 0 46px;text-align:center;overflow:hidden}
.rsvp-bg{position:absolute;width:150px;height:auto;opacity:.5;pointer-events:none;z-index:0}
.rsvp-bg--l{left:-28px;top:40px;transform:rotate(-18deg)}
.rsvp-bg--r{right:-28px;bottom:40px;transform:scaleX(-1) rotate(-18deg)}
.rsvp .col{z-index:1}
.rsvp-card{position:relative;margin:0 auto;max-width:520px;padding:44px 22px 36px;
  background:rgba(247,243,234,.86);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  border:1px solid rgba(176,141,74,.45);box-shadow:0 24px 60px -20px rgba(53,56,36,.45),0 4px 18px rgba(176,141,74,.12)}
.rsvp-card::before{content:"";position:absolute;inset:9px;border:1px solid rgba(95,98,74,.28);pointer-events:none}
.rsvp-corner{position:absolute;width:46px;height:46px;pointer-events:none}
.rsvp-corner--tl{top:0;left:0}.rsvp-corner--tr{top:0;right:0;transform:scaleX(-1)}
.rsvp-corner--bl{bottom:0;left:0;transform:scaleY(-1)}.rsvp-corner--br{bottom:0;right:0;transform:scale(-1,-1)}
.rsvp-ornament{display:block;margin:0 auto 14px;width:min(250px,70vw);height:auto}
.rsvp-eyebrow{font-family:var(--serif);font-weight:700;font-size:13px;letter-spacing:.34em;text-transform:uppercase;color:var(--cafe);margin-bottom:2px}
.rsvp-title{font-family:var(--script);font-weight:400;font-size:clamp(40px,11vw,56px);line-height:1.15;color:var(--cafe);margin-bottom:12px}
.rsvp-text{font-family:var(--display);font-size:clamp(18px,5vw,21px);line-height:1.6;color:var(--olivo)}
.rsvp-thanks{font-family:var(--display);font-size:21px;color:var(--olivo);margin:12px 0 4px}
#rsvp-note{font-family:var(--serif);font-style:italic;font-size:17px;color:var(--cafe);margin-top:14px;display:none}
#rsvp-name{font-family:var(--script);font-size:clamp(34px,9vw,46px);line-height:1.2;color:var(--musgo);margin:2px auto 0;display:none}
.rsvp-divider{display:flex;align-items:center;gap:14px;max-width:300px;margin:16px auto 20px}
.rsvp-divider::before,.rsvp-divider::after{content:"";flex:1;height:1px;background:linear-gradient(to right,transparent,rgba(176,141,74,.6),transparent)}
.rsvp-divider svg{width:16px;height:16px;fill:#b08d4a;flex:none}
.rsvp-pases{max-width:420px;margin:0 auto 20px;padding:14px 22px;background:rgba(180,184,151,.22);border:1px solid rgba(176,141,74,.35);border-radius:14px;display:none;align-items:center;justify-content:space-between;gap:16px}
.rsvp-pases span{font-family:var(--serif);font-weight:700;font-size:14px;letter-spacing:.3em;text-transform:uppercase;color:var(--cafe)}
.rsvp-pases b{font-family:var(--script);font-weight:400;font-size:46px;line-height:1;color:var(--musgo)}
.rsvp-box{text-align:left}
.rsvp-people{display:flex;flex-direction:column;gap:12px;margin:0 auto 20px;max-width:420px}
.person{border-radius:14px;padding:14px;background:rgba(255,255,255,.55);border:1.5px solid rgba(176,141,74,.3);transition:border-color .25s,background .25s,box-shadow .25s}
.person[data-choice="yes"]{border-color:var(--musgo);background:rgba(180,184,151,.18)}
.person[data-choice="no"]{border-color:rgba(94,84,64,.55);background:rgba(94,84,64,.06)}
.person-lbl{font-family:var(--serif);font-weight:700;font-size:13px;letter-spacing:.24em;text-transform:uppercase;color:var(--cafe);margin-bottom:4px}
.person-name{font-family:var(--script);font-size:31px;line-height:1.2;color:var(--olivo);margin-bottom:10px}
.person input{width:100%;font-family:var(--serif);font-size:17px;color:var(--olivo);background:rgba(255,255,255,.8);border:1.5px solid rgba(176,141,74,.32);border-radius:12px;padding:12px 14px;margin-bottom:10px;outline:none;min-height:50px;-webkit-appearance:none}
.person input:focus{border-color:var(--musgo);box-shadow:0 0 0 3px rgba(95,98,74,.16);background:#fff}
.person input::placeholder{color:#7d7462}
.person-tg{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.person-tg button{position:relative;overflow:hidden;min-height:48px;padding:10px 6px;border-radius:10px;border:1.5px solid rgba(176,141,74,.32);background:rgba(255,255,255,.6);font-family:var(--serif);font-style:italic;font-size:17px;color:var(--olivo);cursor:pointer;transition:all .25s}
.person-tg button.on-yes{background:rgba(95,98,74,.16);border-color:var(--musgo);color:var(--olivo);font-weight:700}
.person-tg button.on-no{background:rgba(94,84,64,.1);border-color:var(--cafe);color:var(--cafe);font-weight:700}
.person-tg button:disabled{opacity:.45;cursor:not-allowed}
.rsvp-send{width:100%;max-width:420px;margin:0 auto;display:flex;min-height:56px;letter-spacing:.2em;text-transform:uppercase;font-size:15px;
  background:linear-gradient(135deg,var(--musgo) 0%,#787c5f 100%)!important;border:1.5px solid rgba(176,141,74,.55)!important}
.rsvp-send:disabled{opacity:.55;cursor:not-allowed}
#rsvp-feedback{font-family:var(--serif);font-style:italic;font-size:17px;line-height:1.5;text-align:center;margin-top:12px}
.rsvp-gracias{text-align:center;padding:22px 16px;max-width:420px;margin:0 auto;background:rgba(255,255,255,.6);border:1.5px solid rgba(176,141,74,.35);border-radius:16px}
.rsvp-gracias svg{width:40px;height:40px;margin:0 auto 10px;color:var(--musgo)}
.rsvp-gracias-title{font-family:var(--display);font-size:25px;color:var(--olivo);margin-bottom:6px}
.rsvp-gracias-sub{font-family:var(--serif);font-style:italic;font-size:17px;line-height:1.55;color:var(--cafe);margin-bottom:16px}
.rsvp-edit{position:relative;overflow:hidden;border:1.5px solid var(--musgo);background:transparent;border-radius:24px;padding:10px 22px;font-family:var(--serif);font-style:italic;font-weight:700;font-size:16px;color:var(--musgo);cursor:pointer;min-height:46px}
.rsvp-edit:disabled{opacity:.45;cursor:not-allowed}
.rsvp-deadline{display:inline-flex;align-items:center;gap:8px;margin-top:22px;font-family:var(--serif);font-weight:700;font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--cafe)}
.rsvp-deadline svg{width:13px;height:13px;fill:currentColor;flex:none}

/* Footer */""", s, flags=re.S)

corner = '<svg class="rsvp-corner rsvp-corner--{p}" viewBox="0 0 46 46" fill="none" aria-hidden="true"><path d="M2 44V2h42" stroke="#b08d4a" stroke-width=".9" opacity=".7"/><circle cx="2" cy="2" r="2.5" fill="#b08d4a" opacity=".6"/></svg>'
corners = '\n          '.join(corner.format(p=x) for x in ('tl', 'tr', 'bl', 'br'))
s = re.sub(r"  <!-- CONFIRMACIÓN -->.*?  </section>\n", f"""  <!-- CONFIRMACIÓN (diseño de boda-jennifer) -->
  <section class="rsvp" id="rsvp">
    <img class="rsvp-bg rsvp-bg--l" src="rama-oscura.webp" alt="" aria-hidden="true">
    <img class="rsvp-bg rsvp-bg--r" src="rama-oscura.webp" alt="" aria-hidden="true">
    <div class="col">
      <div class="rsvp-card rv">
          {corners}
        <svg class="rsvp-ornament" viewBox="0 0 320 56" fill="none" aria-hidden="true">
          <g stroke="#b08d4a" stroke-width=".9" opacity=".85" fill="none">
            <path d="M18 28 Q50 10 82 28 Q106 42 130 28"/><path d="M190 28 Q214 42 238 28 Q270 10 302 28"/>
            <circle cx="160" cy="28" r="5.5"/><circle cx="160" cy="28" r="2" fill="#b08d4a" stroke="none"/>
            <path d="M148 28 L154 28" opacity=".5"/><path d="M166 28 L172 28" opacity=".5"/>
            <path d="M154 20 Q160 13 166 20" opacity=".55"/><path d="M154 36 Q160 43 166 36" opacity=".55"/>
          </g>
        </svg>
        <p class="rsvp-eyebrow" data-i18n="rsvp_eyebrow">Confirmación</p>
        <h2 class="rsvp-title" data-i18n="confirma">Confirma tu asistencia</h2>
        <p class="rsvp-text" data-i18n="rsvp_txt">Tu asistencia hará de este día un momento aún más especial. Por favor confirma tu asistencia y acompáñanos a celebrar el comienzo de nuestra nueva historia.</p>
        <p class="rsvp-thanks" data-i18n="gracias">¡Muchas gracias!</p>
        <p id="rsvp-note"></p>
        <p id="rsvp-name"></p>
        <div class="rsvp-divider"><svg viewBox="0 0 24 22" aria-hidden="true"><use href="#ic-heart"/></svg></div>
        <div class="rsvp-pases" id="rsvp-pases"><span data-i18n="pases_lbl">Pases</span><b id="rsvp-pases-num">1</b></div>
        <div class="rsvp-box">
          <div id="rsvp-bandeja">
            <div class="rsvp-people" id="rsvp-people"></div>
            <button class="pill pill--olive rsvp-send" id="rsvp-send" type="button"><span id="rsvp-btn-text" data-i18n="enviar">Enviar confirmación</span></button>
          </div>
          <div class="rsvp-gracias" id="rsvp-gracias" style="display:none">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="8.5 12.5 11 15 16 9.5"/></svg>
            <p class="rsvp-gracias-title" id="rsvp-gracias-title"></p>
            <p class="rsvp-gracias-sub" id="rsvp-gracias-sub"></p>
            <button class="rsvp-edit" id="rsvp-edit" type="button" data-i18n="modificar">Modificar mi respuesta</button>
          </div>
          <p id="rsvp-feedback" role="status"></p>
        </div>
        <div class="rsvp-deadline"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm.5 5v5.25l4.5 2.67-.75 1.23L11 13V7h1.5z"/></svg><span data-i18n="limite">Fecha límite · 15 dic 2026</span></div>
      </div>
    </div>
  </section>
""", s, count=1, flags=re.S)

# JS del RSVP: nombre en caligrafía + caja de pases (como Jennifer)
rep("""  var noteEl = document.getElementById('rsvp-note');""",
    """  var noteEl = document.getElementById('rsvp-note');
  var nameEl = document.getElementById('rsvp-name');
  var pasesEl = document.getElementById('rsvp-pases'), pasesNum = document.getElementById('rsvp-pases-num');""")
rep("""    noteEl.style.display = 'block';
    noteEl.textContent = M('para') + urlPara;""",
    """    noteEl.style.display = 'block';
    noteEl.textContent = M('para').trim();
    nameEl.style.display = 'block';
    nameEl.textContent = urlPara;
    if(people.length){ pasesEl.style.display = 'flex'; pasesNum.textContent = people.length; }""")

# i18n nuevos
rep("    gcal:'Add to Google Calendar',", "    gcal:'Google Calendar', ical:'iPhone Calendar',")
rep("    confirma:'Kindly Reply',", "    confirma:'Kindly Reply', rsvp_eyebrow:'RSVP', pases_lbl:'Seats',")
rep("gracias:'Thank you so much!', limite:'Please reply before December 15, 2026',",
    "gracias:'Thank you so much!', limite:'Reply by · Dec 15, 2026',")
rep("para:'Esta invitación es para ',", "para:'Esta invitación es para',")
rep("para:'This invitation is for ',", "para:'This invitation is for',")

# ---------- CSS: levitación, botones vivos, partículas ----------
rep("/* Revelado al hacer scroll */", r"""/* Calendario */
.cal-row{display:flex;flex-direction:column;align-items:center;gap:10px}
.cal-row .pill{min-width:250px}

/* ===== Dibujos que levitan: cada uno con su propio movimiento =====
   .lev lleva la animación de reposo; el <svg> de adentro reacciona al dedo/ratón
   (--px/--py/--pr/--ps) y al scroll (--sy/--sr, con retardo elástico). */
.lev{display:block;width:100%;will-change:transform}
.lev > svg{display:block;width:100%;height:auto;margin:0 auto;transition:transform .6s cubic-bezier(.2,.9,.25,1.25);
  transform:translate3d(var(--px,0px),calc(var(--py,0px) + var(--sy,0px)),0) rotate(calc(var(--pr,0deg) + var(--sr,0deg))) scale(var(--ps,1))}
.lev--sobre{animation:levSobre 4.2s ease-in-out infinite}
.lev--tarjeta{animation:levTarjeta 5.6s ease-in-out infinite}
.lev--regalo{animation:levRegalo 3.8s ease-in-out infinite;transform-origin:50% 100%}
.lev--vestido{animation:levVestido 3.6s ease-in-out infinite;transform-origin:50% 3%}
.lev--traje{animation:levTraje 4.6s ease-in-out infinite;transform-origin:50% 2%;animation-delay:-1.3s}
.lev--iglesia{animation:levIglesia 5.2s ease-in-out infinite;position:relative}
.lev--iglesia::before{content:"";position:absolute;inset:8% 14% 0;border-radius:50%;background:radial-gradient(circle,rgba(176,141,74,.32),transparent 68%);animation:levHalo 5.2s ease-in-out infinite;z-index:-1}
.lev--baile{animation:levBaile 3s ease-in-out infinite;transform-origin:50% 100%}
@keyframes levSobre{0%,100%{transform:translateY(0) rotate(-2.5deg)}50%{transform:translateY(-9px) rotate(2.5deg)}}
@keyframes levTarjeta{0%,100%{transform:perspective(520px) translateY(0) rotateY(0) rotateX(0)}25%{transform:perspective(520px) translateY(-6px) rotateY(16deg) rotateX(5deg)}50%{transform:perspective(520px) translateY(-10px) rotateY(0) rotateX(0)}75%{transform:perspective(520px) translateY(-5px) rotateY(-16deg) rotateX(-4deg)}}
@keyframes levRegalo{0%,55%,100%{transform:translateY(0) scale(1,1)}63%{transform:translateY(2px) scale(1.07,.9)}74%{transform:translateY(-14px) scale(.95,1.06) rotate(-4deg)}84%{transform:translateY(0) scale(1.05,.94) rotate(1deg)}92%{transform:translateY(-3px) scale(1,1)}}
@keyframes levVestido{0%,100%{transform:rotate(-4deg)}50%{transform:rotate(4deg)}}
@keyframes levTraje{0%,100%{transform:translateY(0) rotate(1.8deg)}50%{transform:translateY(-6px) rotate(-1.8deg)}}
@keyframes levIglesia{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-6px) scale(1.035)}}
@keyframes levHalo{0%,100%{opacity:.35;transform:scale(.9)}50%{opacity:1;transform:scale(1.12)}}
@keyframes levBaile{0%,100%{transform:rotate(-3.5deg) translateX(-3px)}25%{transform:rotate(0) translateY(-5px)}50%{transform:rotate(3.5deg) translateX(3px)}75%{transform:rotate(0) translateY(-2px)}}

/* ===== Botones que invitan a tocarlos ===== */
.pill,.copy-btn,.rsvp-edit,.person-tg button,.lang-btn button,.music-btn{-webkit-tap-highlight-color:transparent}
.pill{position:relative;overflow:hidden;isolation:isolate;transition:transform .35s cubic-bezier(.2,.9,.25,1.3),box-shadow .35s,background .3s}
.pill::after{content:"";position:absolute;top:-10%;bottom:-10%;left:-70%;width:45%;pointer-events:none;
  background:linear-gradient(100deg,transparent,rgba(255,255,255,.55),transparent);transform:skewX(-22deg);animation:pillShine 4.8s ease-in-out infinite}
.pill:nth-of-type(2)::after{animation-delay:1.6s}
@keyframes pillShine{0%,68%{left:-70%}100%{left:135%}}
.pill:hover{transform:translateY(-3px) scale(1.03);box-shadow:0 14px 26px -12px rgba(53,56,36,.75)}
.pill:active{transform:scale(.95);transition-duration:.12s}
.pill--olive{animation:ctaPulse 2.8s ease-out infinite}
@keyframes ctaPulse{0%{box-shadow:0 6px 14px -8px rgba(53,56,36,.8),0 0 0 0 rgba(95,98,74,.5)}70%,100%{box-shadow:0 6px 14px -8px rgba(53,56,36,.8),0 0 0 12px rgba(95,98,74,0)}}
.pill--crema{animation:ctaPulseC 3.2s ease-out infinite}
@keyframes ctaPulseC{0%{box-shadow:0 4px 12px -6px rgba(0,0,0,.4),0 0 0 0 rgba(241,232,217,.55)}70%,100%{box-shadow:0 4px 12px -6px rgba(0,0,0,.4),0 0 0 11px rgba(241,232,217,0)}}
.pill svg,.copy-btn svg{transition:transform .4s cubic-bezier(.2,.9,.25,1.4)}
.pill:hover svg{transform:scale(1.18) rotate(-8deg)}
.copy-btn,.rsvp-edit{transition:transform .3s cubic-bezier(.2,.9,.25,1.3),background .25s,color .25s}
.copy-btn{position:relative;overflow:hidden}
.copy-btn:hover,.rsvp-edit:hover{transform:translateY(-2px) scale(1.04)}
.copy-btn:active,.rsvp-edit:active,.person-tg button:active,.lang-btn button:active{transform:scale(.93)}
.person-tg button:hover{transform:translateY(-2px);box-shadow:0 8px 16px -10px rgba(53,56,36,.6)}
.person-tg button.on-yes,.person-tg button.on-no{animation:elige .45s cubic-bezier(.2,.9,.25,1.4)}
@keyframes elige{0%{transform:scale(.9)}60%{transform:scale(1.06)}100%{transform:scale(1)}}
.music-btn:not(.is-playing).is-ready{animation:musicoLlama 2.6s ease-in-out infinite}
@keyframes musicoLlama{0%,100%{transform:scale(1)}8%{transform:scale(1.12) rotate(-6deg)}16%{transform:scale(1) rotate(4deg)}24%{transform:scale(1)}}
/* Las tarjetas de regalos se "asoman" de vez en cuando para que den ganas de girarlas */
.flip:not(.is-flipped) .flip-in{animation:asoma 7s ease-in-out infinite}
.flip:nth-of-type(2):not(.is-flipped) .flip-in{animation-delay:2.3s}
.flip:nth-of-type(3):not(.is-flipped) .flip-in{animation-delay:4.6s}
@keyframes asoma{0%,84%,100%{transform:rotateY(0)}89%{transform:rotateY(-14deg)}94%{transform:rotateY(7deg)}97%{transform:rotateY(-2deg)}}
.flip:hover .flip-front{box-shadow:0 18px 30px -16px rgba(53,56,36,.7)}
.flip-front{transition:box-shadow .3s}
.flip-more svg{animation:giraIco 2.4s ease-in-out infinite}
@keyframes giraIco{0%,60%,100%{transform:rotate(0)}80%{transform:rotate(-200deg)}}
.flip-more{position:relative}
.flip-more::after{content:"";position:absolute;left:50%;bottom:-6px;width:0;height:1.5px;background:currentColor;transform:translateX(-50%);animation:subraya 2.4s ease-in-out infinite}
@keyframes subraya{0%,100%{width:0;opacity:0}50%{width:70%;opacity:.7}}
/* Onda al tocar */
.rip{position:absolute;border-radius:50%;pointer-events:none;transform:translate(-50%,-50%) scale(0);background:rgba(255,255,255,.55);animation:rip .65s ease-out forwards;z-index:2}
.on-dark .rip,.pill--crema .rip{background:rgba(95,98,74,.3)}
@keyframes rip{to{transform:translate(-50%,-50%) scale(1);opacity:0}}

/* ===== Partículas doradas ===== */
#particulas{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:60}

@media (prefers-reduced-motion:reduce){
  .lev,.lev--iglesia::before,.pill::after,.pill--olive,.pill--crema,.flip .flip-in,.flip-more svg,.flip-more::after,.music-btn{animation:none!important}
  #particulas{display:none}
}

/* Revelado al hacer scroll */""")

# canvas de partículas
rep('<div class="wrap">', '<canvas id="particulas" aria-hidden="true"></canvas>\n<div class="wrap">')

# ---------- JS: interacción de los dibujos, ondas, partículas ----------
rep("""/* ================= CUENTA REGRESIVA ================= */""", r"""/* ================= DIBUJOS VIVOS (responden al dedo y al scroll) ================= */
(function(){
  var levs = [].slice.call(document.querySelectorAll('.lev'));
  if(!levs.length || prefersReduced) return;
  levs.forEach(function(lev){
    var svg = lev.querySelector('svg');
    var card = lev.closest('.paper,.olive,.flip') || lev;
    function mira(e){
      var r = card.getBoundingClientRect();
      var x = ((e.clientX - r.left) / r.width - .5), y = ((e.clientY - r.top) / r.height - .5);
      svg.style.setProperty('--px', (x * 12).toFixed(1) + 'px');
      svg.style.setProperty('--py', (y * 10).toFixed(1) + 'px');
      svg.style.setProperty('--pr', (x * 9).toFixed(1) + 'deg');
    }
    function suelta(){ ['--px','--py','--pr'].forEach(function(k){ svg.style.removeProperty(k); }); }
    card.addEventListener('pointermove', mira);
    card.addEventListener('pointerleave', suelta);
    card.addEventListener('pointerdown', function(e){
      mira(e);
      svg.style.setProperty('--ps', '1.16');
      setTimeout(function(){ svg.style.setProperty('--ps', '1'); }, 190);
      setTimeout(suelta, 900);
    });
  });
  /* El scroll los "arrastra": se quedan atrás un instante y regresan con rebote */
  var lastY = scrollY, lastT = performance.now(), tick = false, quieto = null, root = document.documentElement;
  addEventListener('scroll', function(){
    if(tick) return; tick = true;
    requestAnimationFrame(function(){
      var now = performance.now(), v = (scrollY - lastY) / Math.max(16, now - lastT) * 16;
      lastY = scrollY; lastT = now; tick = false;
      var sy = Math.max(-12, Math.min(12, v * .9)), sr = Math.max(-6, Math.min(6, v * .35));
      root.style.setProperty('--sy', sy.toFixed(1) + 'px');
      root.style.setProperty('--sr', sr.toFixed(1) + 'deg');
      clearTimeout(quieto);
      quieto = setTimeout(function(){ root.style.setProperty('--sy','0px'); root.style.setProperty('--sr','0deg'); }, 120);
    });
  }, {passive:true});
})();

/* ================= ONDA AL TOCAR CUALQUIER BOTÓN ================= */
document.addEventListener('pointerdown', function(e){
  var b = e.target.closest('.pill,.copy-btn,.rsvp-edit,.person-tg button,.flip-face');
  if(!b || b.disabled) return;
  var r = b.getBoundingClientRect(), d = Math.max(r.width, r.height) * 2.2;
  var c = document.createElement('span'); c.className = 'rip';
  c.style.width = c.style.height = d + 'px';
  c.style.left = (e.clientX - r.left) + 'px'; c.style.top = (e.clientY - r.top) + 'px';
  if(getComputedStyle(b).position === 'static') b.style.position = 'relative';
  if(b.classList.contains('flip-face')) b.style.overflow = 'hidden';
  b.appendChild(c); setTimeout(function(){ c.remove(); }, 700);
}, {passive:true});

/* ================= PARTÍCULAS: polvo de oro y hojitas de olivo que caen ================= */
var startParticles = (function(){
  var cv = document.getElementById('particulas');
  if(!cv || prefersReduced || !cv.getContext) return function(){};
  var ctx = cv.getContext('2d'), W = 0, H = 0, dpr = Math.min(2, window.devicePixelRatio || 1), P = [], running = false, last = 0;
  function size(){ W = innerWidth; H = innerHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr,0,0,dpr,0,0); }
  function make(top){
    var hoja = Math.random() < .22;
    return { x: Math.random() * W, y: top ? Math.random() * H : -20 - Math.random() * 60,
      r: hoja ? 4 + Math.random() * 3 : .8 + Math.random() * 1.9, hoja: hoja,
      vy: hoja ? .35 + Math.random() * .35 : .25 + Math.random() * .5, vx: (Math.random() - .5) * .25,
      a: Math.random() * Math.PI * 2, va: (Math.random() - .5) * .03, ph: Math.random() * Math.PI * 2, tw: .02 + Math.random() * .04 };
  }
  function n(){ return W < 700 ? 26 : 40; }
  function dibuja(p){
    var brillo = .55 + .45 * Math.sin(p.ph);
    ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(p.a);
    if(p.hoja){
      ctx.globalAlpha = .55;
      var g = ctx.createLinearGradient(-p.r, 0, p.r, 0); g.addColorStop(0, '#5f624a'); g.addColorStop(1, '#8f936f');
      ctx.fillStyle = g; ctx.beginPath();
      ctx.moveTo(-p.r * 1.6, 0); ctx.quadraticCurveTo(0, -p.r * .9, p.r * 1.6, 0); ctx.quadraticCurveTo(0, p.r * .9, -p.r * 1.6, 0); ctx.fill();
    } else {
      ctx.globalAlpha = .35 + .55 * brillo;
      var gg = ctx.createRadialGradient(0, 0, 0, 0, 0, p.r * 3);
      gg.addColorStop(0, 'rgba(255,244,214,1)'); gg.addColorStop(.35, 'rgba(214,178,104,.9)'); gg.addColorStop(1, 'rgba(176,141,74,0)');
      ctx.fillStyle = gg; ctx.beginPath(); ctx.arc(0, 0, p.r * 3, 0, Math.PI * 2); ctx.fill();
      if(brillo > .9 && p.r > 1.6){ /* destello en cruz */
        ctx.globalAlpha = (brillo - .9) * 8; ctx.strokeStyle = 'rgba(255,248,226,.9)'; ctx.lineWidth = .7;
        ctx.beginPath(); ctx.moveTo(-p.r * 4, 0); ctx.lineTo(p.r * 4, 0); ctx.moveTo(0, -p.r * 4); ctx.lineTo(0, p.r * 4); ctx.stroke();
      }
    }
    ctx.restore();
  }
  function loop(t){
    if(!running) return;
    var dt = Math.min(3, (t - last) / 16.7 || 1); last = t;
    ctx.clearRect(0, 0, W, H);
    for(var i = 0; i < P.length; i++){
      var p = P[i];
      p.ph += p.tw * dt; p.a += p.va * dt;
      p.y += p.vy * dt; p.x += (p.vx + Math.sin(p.ph * .5) * (p.hoja ? .45 : .18)) * dt;
      if(p.y > H + 20 || p.x < -30 || p.x > W + 30) P[i] = make(false);
      dibuja(p);
    }
    requestAnimationFrame(loop);
  }
  addEventListener('resize', size);
  document.addEventListener('visibilitychange', function(){
    if(document.hidden){ running = false; } else if(P.length && !running){ running = true; last = performance.now(); requestAnimationFrame(loop); }
  });
  return function(){
    if(running) return;
    size(); P = []; for(var i = 0; i < n(); i++) P.push(make(true));
    running = true; last = performance.now(); requestAnimationFrame(loop);
  };
})();

/* ================= CUENTA REGRESIVA ================= */""")
rep("  initReveals();\n}", "  initReveals();\n  startParticles();\n}")

p.write_text(s, encoding='utf-8')
print('ok')
