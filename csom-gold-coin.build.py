import math

CX = CY = 300
def pt(r, deg):
    a = math.radians(deg)
    return CX + r*math.cos(a), CY + r*math.sin(a)

P = []
P.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">')

P.append('''<defs>
  <radialGradient id="goldBase" cx="38%" cy="32%" r="75%">
    <stop offset="0%" stop-color="#FFF4C2"/><stop offset="42%" stop-color="#F3C64A"/>
    <stop offset="78%" stop-color="#D89A28"/><stop offset="100%" stop-color="#A9711A"/>
  </radialGradient>
  <radialGradient id="goldField" cx="40%" cy="34%" r="80%">
    <stop offset="0%" stop-color="#FBE29A"/><stop offset="55%" stop-color="#E8B23C"/>
    <stop offset="100%" stop-color="#BE8622"/>
  </radialGradient>
  <linearGradient id="navyRing" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#26317f"/><stop offset="100%" stop-color="#141a54"/>
  </linearGradient>
  <linearGradient id="coverGrad" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#2b3a86"/><stop offset="55%" stop-color="#1c2668"/>
    <stop offset="100%" stop-color="#101748"/>
  </linearGradient>
  <linearGradient id="pagesGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#B9852A"/><stop offset="45%" stop-color="#F1CE63"/>
    <stop offset="100%" stop-color="#C99230"/>
  </linearGradient>
  <linearGradient id="pagesGradB" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#F1CE63"/><stop offset="100%" stop-color="#B9852A"/>
  </linearGradient>
  <linearGradient id="beadLight" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#FFE7A0"/><stop offset="100%" stop-color="#C68C22"/>
  </linearGradient>
  <linearGradient id="beadDark" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#D9A63A"/><stop offset="100%" stop-color="#9C6B16"/>
  </linearGradient>
  <linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#ffffff" stop-opacity="0.42"/>
    <stop offset="55%" stop-color="#ffffff" stop-opacity="0.03"/>
    <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
  </linearGradient>
  <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
    <feDropShadow dx="0" dy="6" stdDeviation="9" flood-color="#000" flood-opacity="0.35"/>
  </filter>
  <filter id="bookShadow" x="-30%" y="-30%" width="160%" height="160%">
    <feDropShadow dx="3" dy="5" stdDeviation="4" flood-color="#0a0f30" flood-opacity="0.55"/>
  </filter>
</defs>''')

# base disc
P.append('<g filter="url(#softShadow)">')
P.append(f'<circle cx="{CX}" cy="{CY}" r="284" fill="url(#goldBase)"/>')
P.append('</g>')
P.append(f'<circle cx="{CX}" cy="{CY}" r="284" fill="none" stroke="#8A5B12" stroke-width="3"/>')

# braided rope
RB=268; NB=58
for i in range(NB):
    deg=360.0*i/NB
    x,y=pt(RB,deg); tang=deg+90
    fill='url(#beadLight)' if i%2==0 else 'url(#beadDark)'
    P.append(f'<g transform="translate({x:.2f},{y:.2f}) rotate({tang:.2f})"><ellipse rx="12.5" ry="7.2" fill="{fill}" stroke="#7E540F" stroke-width="1"/></g>')
P.append(f'<circle cx="{CX}" cy="{CY}" r="255" fill="none" stroke="#8A5B12" stroke-width="2.5"/>')

# navy ring + gold field
P.append(f'<circle cx="{CX}" cy="{CY}" r="253" fill="url(#navyRing)"/>')
P.append(f'<circle cx="{CX}" cy="{CY}" r="253" fill="none" stroke="#0A1030" stroke-width="2"/>')
P.append(f'<circle cx="{CX}" cy="{CY}" r="190" fill="url(#goldField)"/>')
P.append(f'<circle cx="{CX}" cy="{CY}" r="190" fill="none" stroke="#8A5B12" stroke-width="3"/>')
P.append(f'<circle cx="{CX}" cy="{CY}" r="184" fill="none" stroke="#FBE7A0" stroke-width="1.5" opacity="0.55"/>')

# curved text
RT=224
tx1,ty1=pt(RT,212); tx2,ty2=pt(RT,328)
P.append(f'<path id="topArc" d="M {tx1:.2f} {ty1:.2f} A {RT} {RT} 0 0 1 {tx2:.2f} {ty2:.2f}" fill="none"/>')
RB2=226
bx1,by1=pt(RB2,161); bx2,by2=pt(RB2,19)
P.append(f'<path id="botArc" d="M {bx1:.2f} {by1:.2f} A {RB2} {RB2} 0 0 0 {bx2:.2f} {by2:.2f}" fill="none"/>')
P.append('<text font-family="Arial, Helvetica, sans-serif" font-weight="700" fill="#EAF0FF" font-size="34" letter-spacing="6"><textPath href="#topArc" startOffset="50%" text-anchor="middle">CERTIFIED</textPath></text>')
P.append('<text font-family="Arial, Helvetica, sans-serif" font-weight="700" fill="#EAF0FF" font-size="23" letter-spacing="2.2"><textPath href="#botArc" startOffset="50%" text-anchor="middle">SECURITY OPERATIONS MANAGER</textPath></text>')

# side stars
for deg in (180,0):
    sx,sy=pt(221,deg); star=[]
    for k in range(10):
        rr=13 if k%2==0 else 5.5
        aa=math.radians(-90+k*36)
        star.append(f'{sx+rr*math.cos(aa):.2f},{sy+rr*math.sin(aa):.2f}')
    P.append(f'<polygon points="{" ".join(star)}" fill="#F4CF57" stroke="#8A5B12" stroke-width="0.8"/>')

# ===== center BOOK / TOME emblem =====
# front cover quad (slight tilt)
TL=(238,196); TR=(392,190); BR=(398,406); BL=(244,412)
# left page-block depth
LP_back_top=(214,208); LP_back_bot=(220,424)
# bottom page-block depth
BP_fr=(404,420); BP_bl=(252,426)

P.append('<g filter="url(#bookShadow)">')
# bottom depth (pages)
P.append(f'<polygon points="{BL[0]},{BL[1]} {BR[0]},{BR[1]} {BP_fr[0]},{BP_fr[1]} {BP_bl[0]},{BP_bl[1]}" fill="url(#pagesGradB)" stroke="#7E540F" stroke-width="2"/>')
# left depth (pages) with page lines
P.append(f'<polygon points="{TL[0]},{TL[1]} {LP_back_top[0]},{LP_back_top[1]} {LP_back_bot[0]},{LP_back_bot[1]} {BL[0]},{BL[1]}" fill="url(#pagesGrad)" stroke="#7E540F" stroke-width="2"/>')
for t in (0.28,0.5,0.72):
    x1=LP_back_top[0]+(TL[0]-LP_back_top[0])*t; y1=LP_back_top[1]+(TL[1]-LP_back_top[1])*t
    x2=LP_back_bot[0]+(BL[0]-LP_back_bot[0])*t; y2=LP_back_bot[1]+(BL[1]-LP_back_bot[1])*t
    P.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#9A6B18" stroke-width="1.4" opacity="0.7"/>')
# front cover
P.append(f'<polygon points="{TL[0]},{TL[1]} {TR[0]},{TR[1]} {BR[0]},{BR[1]} {BL[0]},{BL[1]}" fill="url(#coverGrad)" stroke="#F0C24C" stroke-width="4"/>')
P.append('</g>')
# inner bevel line on cover
def lerp(a,b,t): return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
itl=lerp(TL,BR,0.045); ibr=lerp(BR,TL,0.045); itr=lerp(TR,BL,0.045); ibl=lerp(BL,TR,0.045)
P.append(f'<polygon points="{itl[0]:.1f},{itl[1]:.1f} {itr[0]:.1f},{itr[1]:.1f} {ibr[0]:.1f},{ibr[1]:.1f} {ibl[0]:.1f},{ibl[1]:.1f}" fill="none" stroke="#4a5aa8" stroke-width="1.6" opacity="0.8"/>')

# clip circuit traces to the front cover
P.append(f'<clipPath id="coverClip"><polygon points="{TL[0]},{TL[1]} {TR[0]},{TR[1]} {BR[0]},{BR[1]} {BL[0]},{BL[1]}"/></clipPath>')
P.append('<g clip-path="url(#coverClip)" stroke="#EBC65A" stroke-width="2" fill="none" opacity="0.85" stroke-linecap="round" stroke-linejoin="round">')
# circuit traces (PCB-style), mostly right/lower, deterministic
traces = [
 "M352,205 L352,250 L378,276 L378,330",
 "M372,205 L372,232 L392,252",
 "M336,232 L336,300 L360,324 L360,392",
 "M392,300 L368,300 L368,352 L344,376",
 "M318,214 L318,262 L300,280 L300,340 L322,362 L322,404",
 "M300,392 L340,392 L358,374",
 "M382,346 L382,398",
 "M260,300 L286,300 L286,344",
 "M276,214 L276,244 L262,258",
 "M356,344 L332,344",
]
for d in traces:
    P.append(f'<path d="{d}"/>')
P.append('</g>')
# circuit nodes
nodes=[(352,205),(372,205),(378,330),(336,232),(360,392),(322,404),(300,392),(382,398),
       (286,344),(262,258),(392,252),(344,376),(318,214),(276,214),(356,344),(392,300)]
P.append('<g clip-path="url(#coverClip)">')
for nx,ny in nodes:
    P.append(f'<circle cx="{nx}" cy="{ny}" r="3.6" fill="#F2CB58"/>')
P.append('</g>')

# subtle navy clearing behind wordmark for legibility
P.append('<g clip-path="url(#coverClip)"><rect x="222" y="286" width="156" height="52" rx="10" fill="#141c52" opacity="0.72"/></g>')
# CSOM wordmark on cover (left-center)
P.append('<text x="300" y="323" text-anchor="middle" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="50" letter-spacing="1" fill="#F5E4A8" stroke="#0C1238" stroke-width="1.1">CSOM</text>')

# gloss
P.append(f'<ellipse cx="{CX}" cy="{CY-120}" rx="230" ry="150" fill="url(#gloss)"/>')
P.append('</svg>')

open('/tmp/csom2.svg','w').write("\n".join(P))
print("written")
