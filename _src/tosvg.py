import fitz
d=fitz.open('inv.pdf');p=d[0];D=p.get_drawings()
groups={'church':[17,18,19,20],'couple':[30,31,32,33,34,35,36,37],'dress':[48],'suit':[49,50],
 'envelope':[56],'card':[58],'gift':[54],'sprig':[8],'pin':[13,14,15]}
def f(v):return ('%.2f'%v).rstrip('0').rstrip('.')
for name,ids in groups.items():
  paths=[];xs=[];ys=[]
  for i in ids:
    dr=D[i];s='';last=None
    for it in dr['items']:
      k=it[0]
      if k=='l':
        a,b=it[1],it[2]
        if last is None or abs(a.x-last.x)>.01 or abs(a.y-last.y)>.01: s+='M%s %s'%(f(a.x),f(a.y))
        s+='L%s %s'%(f(b.x),f(b.y));last=b;xs+=[a.x,b.x];ys+=[a.y,b.y]
      elif k=='c':
        a,b,c,e=it[1:5]
        if last is None or abs(a.x-last.x)>.01 or abs(a.y-last.y)>.01: s+='M%s %s'%(f(a.x),f(a.y))
        s+='C%s %s %s %s %s %s'%(f(b.x),f(b.y),f(c.x),f(c.y),f(e.x),f(e.y));last=e;xs+=[a.x,e.x];ys+=[a.y,e.y]
      elif k=='re':
        r=it[1];s+='M%s %sH%sV%sH%sZ'%(f(r.x0),f(r.y0),f(r.x1),f(r.y1),f(r.x0));last=None;xs+=[r.x0,r.x1];ys+=[r.y0,r.y1]
      elif k=='qu':
        q=it[1];s+='M%s %sL%s %sL%s %sL%s %sZ'%(f(q.ul.x),f(q.ul.y),f(q.ur.x),f(q.ur.y),f(q.lr.x),f(q.lr.y),f(q.ll.x),f(q.ll.y));last=None
        xs+=[q.ul.x,q.lr.x];ys+=[q.ul.y,q.lr.y]
    if dr.get('closePath'): s+='Z'
    paths.append('<path fill-rule="%s" d="%s"/>'%('evenodd' if dr.get('even_odd') else 'nonzero',s))
  x0,y0,x1,y1=min(xs),min(ys),max(xs),max(ys)
  svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s %s %s %s" fill="currentColor">%s</svg>'%(f(x0),f(y0),f(x1-x0),f(y1-y0),''.join(paths))
  open('svg/%s.svg'%name,'w').write(svg);print(name,len(svg))
