# Arma index.html desde template.html: inyecta los iconos vectoriales (extraídos
# del PDF del cliente con tosvg.py) como <symbol> y las fotos de la galería.
import re, pathlib
S = pathlib.Path(__file__).parent
root = S.parent
tpl = (S / 'template.html').read_text(encoding='utf-8')

symbols, vbs = [], {}
for name in ['church', 'couple', 'dress', 'suit', 'envelope', 'card', 'gift', 'sprig', 'pin']:
    svg = (S / f'{name}.svg').read_text(encoding='utf-8')
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    inner = re.search(r'<svg[^>]*>(.*)</svg>', svg, re.S).group(1)
    # viewBox = rect real de cada dibujo en el PDF (antes solo medía extremos de trazos
    # y el moño del regalo se cortaba) + un margen pequeño en los 4 lados.
    x, y, w, h = map(float, vb.split()); pad = max(w, h) * .03
    vb = f'{x-pad:.2f} {y-pad:.2f} {w+2*pad:.2f} {h+2*pad:.2f}'
    vbs[name] = f'0 0 {w+2*pad:.2f} {h+2*pad:.2f}'  # el <symbol> ya traduce su propio viewBox
    symbols.append(f'  <symbol id="ic-{name}" viewBox="{vb}">{inner}</symbol>')

alts = ['Omar y Cari al atardecer', 'Omar y Cari caminando en el puente', 'Omar y Cari en el bosque',
        'Omar y Cari en el puente', 'Omar y Cari abrazados', 'Omar y Cari frente a frente',
        'Omar y Cari riendo', 'Omar y Cari sentados', 'Omar y Cari en blanco y negro', 'Omar y Cari entre la hierba']
wheel = '\n        '.join(
    f'<div class="wheel-card"><img src="g{i+1}.webp" alt="{a}" draggable="false"></div>' for i, a in enumerate(alts))

out = tpl.replace('{{SYMBOLS}}', '\n'.join(symbols)).replace('{{WHEEL}}', wheel)
out = re.sub(r'\{\{VB:(\w+)\}\}', lambda m: vbs[m.group(1)], out)
assert '{{' not in out, 'placeholder sin reemplazar'
(root / 'index.html').write_text(out, encoding='utf-8')
print('index.html', len(out))
