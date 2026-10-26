import json,re
ILL="../assets/ill/"
SAND="#F1E9DC";NIGHT="#121A16";INK="#1F2A24";SAGE="#6E8B74";CLAY="#C96F4A";PAPER="#FFFFFF"
VARS={"sand":SAND,"night":NIGHT,"ink":INK,"sage":SAGE,"clay":CLAY,"clay-ink":"#9A4E2E","sage-soft":"#DCE6DD"}
SVG_APP='<svg viewBox="0 0 24 24" width="60%" height="60%" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/></svg>'
SVG_LOCK='<svg viewBox="0 0 24 24" width="60%" height="60%" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>'
SVG_PHONE='<svg viewBox="0 0 24 24" width="60%" height="60%" fill="none" stroke="currentColor" stroke-width="2"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M10 18h4"/></svg>'
def times(lines,total,lead=0.2):
    w=[len(l) for l in lines]; s=sum(w); acc=0; out=[]
    for x in w:
        out.append(lead+(total-lead-0.3)*acc/s); acc+=x
    out.append(total); return out
def st(**k): return {kk.replace('_','-'):v for kk,v in k.items()}
def text(html,x,y,w,size,**kw):
    L={"t":"text","html":html,"style":st(left=f"{x}px",top=f"{y}px",width=f"{w}px",font_size=f"{size}px",**kw.pop('style',{}))}
    L.update(kw); return L
def img(src,**kw): L={"t":"img","src":ILL+src}; L.update(kw); return L
def card(src,x,y,w,h,**kw): L={"t":"card","src":ILL+src,"style":st(left=f"{x}px",top=f"{y}px",width=f"{w}px",height=f"{h}px")}; L.update(kw); return L
def rect(x,y,w,h,bg,**kw): L={"t":"rect","style":st(left=f"{x}px",top=f"{y}px",width=f"{w}px",height=f"{h}px",background=bg,**kw.pop('style',{}))}; L.update(kw); return L
def grad(**kw): L={"t":"rect","style":{"left":"0","top":"0","width":"100%","height":"100%","background":kw.pop('bg')}}; L.update(kw); return L
def pill(html,x,y,size,bg,color,**kw): L={"t":"pill","html":html,"style":st(left=f"{x}px",top=f"{y}px",font_size=f"{size}px",padding=f"{size*0.45}px {size*0.9}px",background=bg,color=color)}; L.update(kw); return L
def btn(html,x,y,w,h,size,**kw): L={"t":"btn","html":html,"style":st(left=f"{x}px",top=f"{y}px",width=f"{w}px",height=f"{h}px",font_size=f"{size}px")}; L.update(kw); return L
def strike(html,svg,x,y,size,**kw): L={"t":"strike","html":html,"svg":svg,"ico":f"{size*1.6}px","style":st(left=f"{x}px",top=f"{y}px",font_size=f"{size}px",color="#F2F5F2")}; L.update(kw); return L
def check(html,x,y,w,size,**kw): L={"t":"check","html":html,"ico":f"{size*1.1}px","icoF":f"{size*0.7}px","style":st(left=f"{x}px",top=f"{y}px",width=f"{w}px",font_size=f"{size}px")}; L.update(kw); return L
def disc(x,y,d,**kw): L={"t":"disc","style":st(left=f"{x}px",top=f"{y}px",width=f"{d}px",height=f"{d}px")}; L.update(kw); return L
def ring(x,y,d,**kw): L={"t":"ring","style":st(left=f"{x}px",top=f"{y}px",width=f"{d}px",height=f"{d}px")}; L.update(kw); return L
def seal(html,x,y,d,size,**kw): L={"t":"seal","html":html,"style":st(left=f"{x}px",top=f"{y}px",width=f"{d}px",height=f"{d}px",font_size=f"{size}px")}; L.update(kw); return L
def scene(start,end,bg,layers,**kw): d={"start":start,"end":end,"bg":bg,"layers":layers}; d.update(kw); return d

# ---------------- AD (1080x1920, 49.71 s) ----------------
AD_DUR=49.71
AD_LINES=["Si tu hijo se duerme con el teléfono en la mano.","Si la cena se come en silencio, cada uno mirando una pantalla.","Si ya gritaste, escondiste, quitaste el teléfono... y a la semana todo volvió a ser igual.","No es tu culpa. Y tampoco es culpa de tu hijo.","Hay una razón, comprobada en estudios, por la que ninguna regla de pantallas aguanta más de siete días.","Mi familia y yo la encontramos. Y la solución no fue una app de control, ni una contraseña, ni quitarles el teléfono.","Fue algo que cabe en la palma de tu mano, y vive en la cocina.","Toca el botón, responde cinco preguntas sobre tu casa, y te mostramos qué está pasando en realidad, y cómo lo resolvimos nosotros.","Son dos minutos. Y puede cambiar cómo se siente tu casa esta misma semana."]
T=times(AD_LINES,AD_DUR)
W,H=1080,1920
DARKGRAD="linear-gradient(to top,rgba(18,26,22,.96) 0%,rgba(18,26,22,.75) 38%,rgba(18,26,22,0) 70%)"
cap=lambda html,**kw: text(html,80,1380,920,66,display=True,fx="words",style={"color":"#F2F5F2"},**kw)
ad=[]
# S1
ad.append(scene(T[0],T[1],NIGHT,[img("ill1-teen-asleep.png",kb=[1.12,1.22],pan=[0,0,-40,0]),grad(bg=DARKGRAD),pill("1:04 a.m.",80,1270,34,"rgba(255,255,255,.12)","#F2F5F2",fx="up",**{"in":0.2}),cap("Si tu hijo se duerme con el teléfono en la mano.",wordsEnd=2.4)]))
# S2
ad.append(scene(T[1],T[2],NIGHT,[img("ill2-silent-dinner.png",kb=[1.15,1.25],pan=[20,0,-30,0]),grad(bg=DARKGRAD),cap("Si la cena se come en silencio. Cada uno mirando una pantalla.",wordsEnd=2.6)]))
# S3
ad.append(scene(T[2],T[3],NIGHT,[img("ill3-rules-fail.png",kb=[1.1,1.2]),grad(bg=DARKGRAD),cap("Gritaste. Escondiste. Quitaste el teléfono.",wordsEnd=1.8),text("Y a la semana, todo volvió a ser igual.",80,1660,920,50,fx="up",style={"color":"#D3DDD5","font-weight":"700"},**{"in":2.6})]))
# S4
d=T[4]-T[3]
ad.append(scene(T[3],T[4],SAND,[text("No es<br>tu culpa.",90,560,900,150,display=True,fx="pop",style={"color":INK}),text("Y tampoco es culpa<br>de tu hijo.",90,1040,900,88,display=True,fx="up",style={"color":CLAY},**{"in":d*0.5})]))
# S5
d=T[5]-T[4]
ad.append(scene(T[4],T[5],SAND,[text("Hay una razón,<br>comprobada en estudios,",90,200,900,74,display=True,fx="up",style={"color":INK}),card("ill4-brain-drain.png",90,520,900,506,kb=[1,1.06],fx="pop",**{"in":0.4}),text("por la que ninguna regla de pantallas aguanta más de",90,1120,900,60,fx="words",wordsEnd=d*0.55,style={"color":INK,"font-weight":"700","line-height":"1.2"},**{"in":d*0.3}),text("7 días",90,1330,900,230,display=True,fx="pop",style={"color":CLAY},**{"in":d*0.72})]))
# S6
d=T[6]-T[5]
ad.append(scene(T[5],T[6],NIGHT,[text("Mi familia y yo<br>la encontramos.",90,300,900,96,display=True,fx="up",style={"color":"#F2F5F2"}),text("Y la solución no fue:",90,720,900,52,fx="up",style={"color":"#B9C4BC","font-weight":"700"},**{"in":d*0.3}),strike("Una app de control",SVG_APP,90,860,58,**{"in":d*0.42}),strike("Una contraseña",SVG_LOCK,90,1020,58,**{"in":d*0.62}),strike("Quitarles el teléfono",SVG_PHONE,90,1180,58,**{"in":d*0.8})]))
# S7 mystery disc
d=T[7]-T[6]
ad.append(scene(T[6],T[7],NIGHT,[rect(0,0,W,H,"radial-gradient(circle at 50% 42%,rgba(201,111,74,.35),rgba(18,26,22,0) 45%)"),ring(340,560,400,per=1.8,**{"in":0.3}),ring(340,560,400,per=1.8,**{"in":1.2}),disc(390,610,300,breathe=True,fx="pop",style={"filter":"blur(2px) brightness(.55)"}),text("Fue algo que cabe en la palma de tu mano.",90,1180,900,72,display=True,fx="words",wordsEnd=1.8,style={"color":"#F2F5F2"}),text("Y vive en la cocina.",90,1500,900,72,display=True,fx="up",style={"color":"#E8B79F"},**{"in":d*0.6})]))
# S8 quiz mock
d=T[8]-T[7]
quiz='''<div style="padding:44px 40px;font-size:30px;color:#1F2A24"><div style="font:600 22px JetBrains Mono,monospace;letter-spacing:.12em;color:#C96F4A">PREGUNTA 1 DE 5</div><div style="height:10px;background:#E4DED3;border-radius:6px;margin:16px 0 34px"><div style="width:20%;height:100%;background:#C96F4A;border-radius:6px"></div></div><div style="font:600 46px/1.1 Fraunces,serif;margin-bottom:30px">¿Dónde duerme el teléfono de tu hijo?</div><div style="display:grid;gap:14px;font-weight:800"><div style="border:3px solid #C96F4A;background:#F6E2D7;border-radius:16px;padding:20px">En su cuarto, con él</div><div style="border:3px solid #E4DED3;border-radius:16px;padding:20px">En su cuarto, lejos de la cama</div><div style="border:3px solid #E4DED3;border-radius:16px;padding:20px">Fuera de su cuarto</div></div></div>'''
ad.append(scene(T[7],T[8],SAND,[text("Responde 5 preguntas<br>sobre tu casa.",90,170,900,80,display=True,fx="up",style={"color":INK}),{"t":"phone","html":quiz,"style":st(left="190px",top="520px",width="700px",height="1000px"),"fx":"up","in":0.5},text("y te mostramos qué está pasando en realidad.",90,1620,900,50,fx="up",style={"color":"#4A5650","font-weight":"700"},**{"in":d*0.5})]))
# S9 CTA
d=T[9]-T[8]
ad.append(scene(T[8],T[9]+0.01,SAND,[text("Son 2 minutos.",90,420,900,120,display=True,fx="pop",style={"color":INK}),text("Y puede cambiar cómo se siente<br>tu casa esta misma semana.",90,620,900,62,fx="up",style={"color":"#4A5650","font-weight":"700","line-height":"1.25"},**{"in":d*0.35}),btn("Responder las 5 preguntas →",120,1040,840,150,52,pulse=True,fx="pop",**{"in":d*0.3}),text("Gratis · sin tarjeta · una familia de tu comunidad",90,1230,900,36,fx="up",style={"color":"#8A948E","font-weight":"700","text-align":"center"},**{"in":d*0.5}),text("Pausa",90,1700,900,64,display=True,fx="up",style={"color":SAGE,"text-align":"center"},**{"in":d*0.5})]))
json.dump({"w":W,"h":H,"fps":24,"duration":AD_DUR,"audio":"../assets/vo/ad-m1.mp3","vars":VARS,"scenes":ad},open("ad.json","w"),ensure_ascii=False,indent=0)

# ---------------- VSL (1920x1080, 348.19 s) ----------------
W,H=1920,1080
SEC=[36.52,58.51,82.99,50.05,42.37,49.79,27.95]; OFF=[0]
for s in SEC: OFF.append(OFF[-1]+s)
VSL_DUR=OFF[-1]
G16="linear-gradient(to right,rgba(18,26,22,.94) 0%,rgba(18,26,22,.78) 42%,rgba(18,26,22,.05) 75%)"
def sec_times(i,lines): return times(lines,SEC[i],lead=0.25)
vsl=[]
# S1 promise
L=["Gracias por responder. Tu resultado ya está en pantalla, y en un momento te explico qué significa.","Pero primero, una promesa.","Quédate hasta el final de este video, porque al final te voy a mostrar el sistema exacto que usamos en mi casa para que mis hijos dejaran el teléfono sin una sola pelea.","Y una tecnología, pequeña, que probablemente crees que cuesta miles de dólares.","No cuesta eso. Y no necesitas saber nada de tecnología para usarla.","Soy parte de una familia como la tuya. No somos una empresa grande.","Somos una familia que vive en tu comunidad y que pasó por lo mismo que tú estás viviendo."]
t=sec_times(0,L)
vsl.append(scene(OFF[0],OFF[1],SAND,[
 text("Tu resultado está en pantalla.",120,150,900,70,display=True,fx="up",style={"color":INK},out=t[1]),
 pill("↑ Mira tu puntaje arriba",120,290,30,"#DCE6DD","#3E5A45",fx="up",**{"in":0.6,"out":t[1]}),
 text("Una promesa:",120,150,900,44,fx="up",style={"color":CLAY,"font-weight":"900","letter-spacing":".04em","text-transform":"uppercase"},**{"in":t[1]}),
 text("Quédate hasta el final.",120,220,900,92,display=True,fx="pop",style={"color":INK},**{"in":t[1]+0.2}),
 check("El sistema exacto que usamos en casa, sin una sola pelea",120,420,860,40,fx="up",**{"in":t[2]+0.8}),
 check("Una tecnología pequeña que crees que cuesta miles",120,520,860,40,fx="up",**{"in":t[3]}),
 check("No cuesta eso. Y no necesitas ser experto",120,620,860,40,fx="up",**{"in":t[4]}),
 card("ill7-dinner-after.png",1060,140,760,428,kb=[1,1.07],fx="right",**{"in":0.3}),
 card("ill5-house-zones.png",1060,610,760,330,kb=[1.02,1.1],fx="right",**{"in":t[3]}),
 rect(120,780,860,3,"#E4DED3",**{"in":t[5]}),
 text("Somos una familia de tu comunidad. No una empresa grande.",120,820,860,40,fx="up",style={"color":"#4A5650","font-weight":"800"},**{"in":t[5]}),
 text("Pasamos por lo mismo que tú estás viviendo.",120,880,860,40,fx="up",style={"color":CLAY,"font-weight":"800"},**{"in":t[6]}),
]))
# S2 pain
L=["Mira si esto te suena.","Tu hijo llega de la escuela y desaparece dentro del teléfono. Le hablas y responde con un ajá sin mirarte.","La tarea toma tres horas porque cada cinco minutos hay una notificación.","La cena se volvió silenciosa.","Y de noche, a la una de la mañana, la luz azul sigue encendida debajo de la almohada.","Probaste de todo. Contraseñas: las adivinó en una semana.","Apps de control: encontró la vuelta en dos.","Quitarle el teléfono: funcionó hasta que saliste de la casa.","Y cada intento terminó igual: gritos, portazos, y tú sintiéndote culpable por ser la policía de tu propia casa.","Quiero que escuches esto con atención. No es tu culpa.","Y no es que tu hijo sea débil o malcriado.","Estás peleando contra un dispositivo diseñado por miles de ingenieros para ganar esa pelea.","Y la estás peleando con la herramienta equivocada: tu voz."]
t=sec_times(1,L)
big=lambda html,i,o=None,**kw: text(html,120,760,1000,60,display=True,fx="words",wordsEnd=i+1.6,style={"color":"#F2F5F2"},**{"in":i,"out":o if o else SEC[1]},**kw)
vsl.append(scene(OFF[1],OFF[2],NIGHT,[
 img("ill2-silent-dinner.png",kb=[1.05,1.12],**{"in":0,"out":t[3]}),
 img("ill1-teen-asleep.png",kb=[1.05,1.14],**{"in":t[3],"out":t[5]}),
 img("ill3-rules-fail.png",kb=[1.02,1.1],**{"in":t[5],"out":t[9]}),
 grad(bg=G16,**{"out":t[9]}),
 text("¿Te suena?",120,150,900,44,fx="up",style={"color":"#E8B79F","font-weight":"900","letter-spacing":".04em","text-transform":"uppercase"},**{"in":0.2,"out":t[5]}),
 big("Desaparece dentro del teléfono. Responde \"ajá\" sin mirarte.",t[1],t[2]),
 big("La tarea toma 3 horas. Una notificación cada 5 minutos.",t[2],t[3]),
 big("La cena se volvió silenciosa.",t[3],t[4]),
 big("1:00 a.m. La luz azul sigue encendida.",t[4],t[5]),
 text("Probaste de todo",120,150,900,44,fx="up",style={"color":"#E8B79F","font-weight":"900","letter-spacing":".04em","text-transform":"uppercase"},**{"in":t[5],"out":t[9]}),
 strike("Contraseñas · adivinadas en 1 semana",SVG_LOCK,120,330,46,**{"in":t[5]+0.3,"out":t[9]}),
 strike("App de control · la vuelta en 2",SVG_APP,120,450,46,**{"in":t[6],"out":t[9]}),
 strike("Quitarle el teléfono · hasta que saliste",SVG_PHONE,120,570,46,**{"in":t[7],"out":t[9]}),
 text("Gritos. Portazos. Y tú, la policía de tu propia casa.",120,760,1000,54,fx="words",wordsEnd=t[8]+2.2,style={"color":"#F2F5F2","font-weight":"800"},**{"in":t[8],"out":t[9]}),
 rect(0,0,W,H,SAND,**{"in":t[9]}),
 text("No es tu culpa.",120,300,1680,160,display=True,fx="pop",style={"color":INK,"text-align":"center"},**{"in":t[9],"out":t[11]}),
 text("Y no es que tu hijo sea débil o malcriado.",120,520,1680,56,fx="up",style={"color":CLAY,"font-weight":"800","text-align":"center"},**{"in":t[10],"out":t[11]}),
 text("Tu voz",120,330,760,150,display=True,fx="left",style={"color":INK,"text-align":"right"},**{"in":t[11]}),
 text("vs.",960,370,80,60,fx="pop",style={"color":"#8A948E","font-weight":"900","text-align":"center"},**{"in":t[11]+0.3}),
 text("miles de<br>ingenieros",1060,300,760,120,display=True,fx="right",style={"color":CLAY},**{"in":t[11]+0.4}),
 text("Estás peleando con la herramienta equivocada.",120,720,1680,50,fx="up",style={"color":"#4A5650","font-weight":"800","text-align":"center"},**{"in":t[12]}),
]))
# S3 science
L=["Esto es lo que dicen los estudios, y lo que cambió todo para nosotros.","Primero. Investigadores de la Universidad de Texas pusieron a casi ochocientas personas a resolver tareas de concentración.","A unos les dejaron el teléfono sobre el escritorio, boca abajo. A otros, en el bolsillo. A otros, en otra habitación.","El teléfono no sonaba. Nadie lo tocó.","Y aun así, quienes lo tenían en otra habitación rindieron claramente mejor que quienes lo tenían a la vista.","Lo llamaron fuga de cerebro: la simple presencia del teléfono consume parte de la capacidad de pensar. Apagado o encendido, da igual.","Segundo. La Academia Americana de Pediatría no recomienda a las familias contar minutos.","Recomienda algo mucho más simple: zonas y horas sin pantallas. Los dormitorios. La mesa. La hora antes de dormir. Lugares, no límites de tiempo.","Tercero. Los estudios sobre lo que se llama phubbing, ignorar a alguien por mirar el teléfono, muestran que los hijos copian el uso del teléfono de sus padres,","y que cuando los padres lo usan frente a ellos, la relación y la autoestima de los hijos se asocian con resultados peores.","Esto nos duele decirlo, porque nosotros también lo hacíamos.","¿Ves el patrón? El problema nunca fue cuántos minutos.","El problema es dónde está el teléfono."]
t=sec_times(2,L)
lab=lambda n,html,i,o: pill(f"{n} · {html}",120,130,30,"#1F2A24","#F2F5F2",fx="up",**{"in":i,"out":o})
vsl.append(scene(OFF[2],OFF[3],SAND,[
 text("Lo que dicen los estudios",120,420,1680,96,display=True,fx="pop",style={"color":INK,"text-align":"center"},**{"in":0,"out":t[1]}),
 text("y lo que cambió todo para nosotros",120,560,1680,46,fx="up",style={"color":"#4A5650","font-weight":"800","text-align":"center"},**{"in":1.2,"out":t[1]}),
 # study 1
 lab("1","Universidad de Texas · casi 800 personas",t[1],t[6]),
 card("ill4-brain-drain.png",120,220,900,506,kb=[1,1.05],fx="up",**{"in":t[1],"out":t[6]}),
 text("Mismo examen. Tres lugares para el teléfono.",120,770,900,40,fx="up",style={"color":"#4A5650","font-weight":"800"},**{"in":t[2],"out":t[6]}),
 {"t":"bars","items":[{"h":"52%","v":"escritorio","l":"a la vista"},{"h":"68%","v":"bolsillo","l":"guardado"},{"h":"100%","v":"otro cuarto","l":"fuera de vista"}],"style":st(left="1120px",top="260px",width="680px",height="400px",font_size="30px",color=INK),"in":t[2],"out":t[6]},
 text("Rendimiento en tareas de concentración",1120,730,680,28,fx="up",style={"color":"#8A948E","font-weight":"800","text-align":"center"},**{"in":t[2],"out":t[6]}),
 text("No sonaba. Nadie lo tocó.",1120,820,680,44,display=True,fx="up",style={"color":INK,"text-align":"center"},**{"in":t[3],"out":t[6]}),
 text("\"Fuga de cerebro\": su sola presencia consume capacidad de pensar.",1120,900,680,34,fx="up",style={"color":CLAY,"font-weight":"800","text-align":"center"},**{"in":t[5],"out":t[6]}),
 # study 2
 lab("2","Academia Americana de Pediatría",t[6],t[8]),
 card("ill5-house-zones.png",960,220,840,472,kb=[1,1.06],fx="right",**{"in":t[6],"out":t[8]}),
 text("No cuentes minutos.",120,240,800,90,display=True,fx="up",style={"color":INK},**{"in":t[6],"out":t[8]}),
 check("Dormitorios sin pantallas",120,420,780,42,fx="up",**{"in":t[7]+0.6,"out":t[8]}),
 check("La mesa sin pantallas",120,510,780,42,fx="up",**{"in":t[7]+1.6,"out":t[8]}),
 check("La hora antes de dormir",120,600,780,42,fx="up",**{"in":t[7]+2.6,"out":t[8]}),
 text("Lugares, no límites de tiempo.",120,740,800,54,display=True,fx="pop",style={"color":CLAY},**{"in":t[7]+4.5,"out":t[8]}),
 # study 3
 lab("3","Phubbing · lo que los hijos copian",t[8],t[11]),
 img("ill2-silent-dinner.png",kb=[1.05,1.1],alpha=0.22,**{"in":t[8],"out":t[11]}),
 text("Los hijos copian el uso del teléfono de sus padres.",120,260,1200,72,display=True,fx="words",wordsEnd=t[8]+3,style={"color":INK},**{"in":t[8],"out":t[11]}),
 text("Cuando los padres lo usan frente a ellos, la relación y la autoestima de los hijos se asocian con peores resultados.",120,480,1200,46,fx="words",wordsEnd=t[9]+4,style={"color":"#4A5650","font-weight":"800","line-height":"1.3"},**{"in":t[9],"out":t[11]}),
 text("Nosotros también lo hacíamos.",120,760,1200,54,display=True,fx="up",style={"color":CLAY},**{"in":t[10],"out":t[11]}),
 # pattern
 rect(0,0,W,H,NIGHT,**{"in":t[11]}),
 text("El problema nunca fue<br>cuántos minutos.",120,260,1680,96,display=True,fx="up",style={"color":"#B9C4BC","text-align":"center"},**{"in":t[11]}),
 text("Es dónde está el teléfono.",120,600,1680,120,display=True,fx="pop",style={"color":"#E8B79F","text-align":"center"},**{"in":t[12]}),
]))
# S4 insight
L=["Aquí está la idea que cambió nuestra casa.","Una regla que vive en tu boca hay que repetirla cada noche. Y cada noche cuesta más.","Una regla que vive en un lugar, se cumple sola.","Las llaves se dejan en la entrada. Los zapatos, en la puerta. Nadie pelea por eso. Es parte de la casa.","Nosotros hicimos lo mismo con el teléfono. Elegimos un lugar. Una hora. Una regla visible, igual para todos, adultos incluidos. Y dejamos de ser los policías.","A eso le llamamos uso con espacio y tiempo dedicados.","Monitorear no es espiar. Es saber el patrón, nunca el contenido.","Es poner un límite claro, en un lugar claro, y dejar que el lugar haga el trabajo.","Los límites claros crían hijos que confían en ti.","La vigilancia escondida cría hijos que aprenden a esconderse."]
t=sec_times(3,L)
vsl.append(scene(OFF[3],OFF[4],SAND,[
 text("La idea que cambió nuestra casa",120,440,1680,90,display=True,fx="pop",style={"color":INK,"text-align":"center"},**{"in":0,"out":t[1]}),
 rect(120,200,820,560,"#FFFFFF",style={"border-radius":"28px","border":"2px solid #E4DED3"},fx="up",**{"in":t[1],"out":t[4]}),
 rect(980,200,820,560,"#DCE6DD",style={"border-radius":"28px"},fx="up",**{"in":t[2],"out":t[4]}),
 text("Una regla que vive<br>en tu boca",170,250,720,64,display=True,fx="up",style={"color":INK},**{"in":t[1],"out":t[4]}),
 text("Se repite cada noche.<br>Cada noche cuesta más.",170,480,720,40,fx="up",style={"color":CLAY,"font-weight":"800"},**{"in":t[1]+1.5,"out":t[4]}),
 text("Una regla que vive<br>en un lugar",1030,250,720,64,display=True,fx="up",style={"color":"#2F4536"},**{"in":t[2],"out":t[4]}),
 text("Se cumple sola.",1030,480,720,56,display=True,fx="pop",style={"color":"#3E5A45"},**{"in":t[2]+1.6,"out":t[4]}),
 text("Las llaves en la entrada. Los zapatos en la puerta. Nadie pelea por eso.",120,820,1680,44,fx="words",wordsEnd=t[3]+3,style={"color":"#4A5650","font-weight":"800","text-align":"center"},**{"in":t[3],"out":t[4]}),
 img("ill5-house-zones.png",kb=[1.02,1.1],**{"in":t[4],"out":t[8]}),
 grad(bg=G16,**{"in":t[4],"out":t[8]}),
 text("Un lugar. Una hora. Una regla visible, igual para todos.",120,200,900,66,display=True,fx="words",wordsEnd=t[4]+3.5,style={"color":"#F2F5F2"},**{"in":t[4],"out":t[5]}),
 text("Adultos incluidos.",120,520,900,54,display=True,fx="up",style={"color":"#E8B79F"},**{"in":t[4]+5,"out":t[5]}),
 pill("Uso con espacio y tiempo dedicados",120,160,34,"#C96F4A","#FFF8F3",fx="up",**{"in":t[5],"out":t[8]}),
 text("Monitorear no es espiar.",120,300,900,80,display=True,fx="up",style={"color":"#F2F5F2"},**{"in":t[6],"out":t[8]}),
 text("Saber el patrón. Nunca el contenido.",120,480,900,48,fx="up",style={"color":"#D3DDD5","font-weight":"800"},**{"in":t[6]+1.4,"out":t[8]}),
 text("Un límite claro, en un lugar claro. Y el lugar hace el trabajo.",120,620,900,48,fx="words",wordsEnd=t[7]+2.5,style={"color":"#E8B79F","font-weight":"800"},**{"in":t[7],"out":t[8]}),
 rect(0,0,W,H,SAND,**{"in":t[8]}),
 text("Los límites claros crían hijos que confían en ti.",120,300,1680,76,display=True,fx="up",style={"color":"#3E5A45","text-align":"center"},**{"in":t[8]}),
 text("La vigilancia escondida cría hijos que aprenden a esconderse.",120,560,1680,76,display=True,fx="up",style={"color":CLAY,"text-align":"center"},**{"in":t[9]}),
]))
# S5 program
L=["Todo lo que aprendimos lo escribimos en un programa de treinta días. Se llama el Programa Familiar Pausa.","Adentro está: cómo presentarle la nueva regla a tus hijos sin que sea un castigo, con las palabras exactas por edad.","Qué horarios funcionan a los ocho años, a los doce, a los dieciséis.","Dónde poner la zona sin teléfono en tu casa y por qué ese lugar lo es todo.","Un plan semana por semana, con lo que va a pasar y cuándo viene la resistencia.","Y un acuerdo familiar para firmar juntos.","No cuesta cuarenta y siete dólares, aunque lo vale.","Cuesta siete. Siete dólares, porque queremos que llegue a todas las familias de nuestra comunidad, no solo a las que pueden pagar un curso."]
t=sec_times(4,L)
cover='''<div style="position:absolute;inset:0;background:linear-gradient(160deg,#6E8B74,#2F4536);padding:60px 54px;color:#F2F5F2"><div style="font:600 22px JetBrains Mono,monospace;letter-spacing:.14em;opacity:.8">PROGRAMA FAMILIAR</div><div style="font:600 86px/1 Fraunces,serif;margin:18px 0 10px">Pausa</div><div style="font:800 30px Nunito;opacity:.9">30 días para recuperar<br>la cena, la tarea y el sueño</div><div style="position:absolute;left:54px;bottom:54px;width:110px;height:110px;border-radius:50%;background:#C96F4A;box-shadow:0 20px 40px -10px rgba(0,0,0,.5)"></div><div style="position:absolute;right:54px;bottom:60px;font:700 22px Nunito;opacity:.8">Una familia de tu comunidad</div></div>'''
vsl.append(scene(OFF[4],OFF[5],SAND,[
 {"t":"rect","html":cover,"style":st(left="1180px",top="140px",width="600px",height="800px",border_radius="22px",overflow="hidden",box_shadow="0 60px 120px -40px rgba(0,0,0,.45)"),"fx":"right","in":0.3,"rot":-3},
 text("Programa Familiar Pausa",120,170,980,84,display=True,fx="up",style={"color":INK}),
 pill("30 días · PDF + plan",120,330,32,"#DCE6DD","#3E5A45",fx="up",**{"in":1}),
 check("Cómo presentar la regla sin que sea castigo: las palabras exactas por edad",120,450,960,38,fx="up",**{"in":t[1]}),
 check("Horarios que funcionan a los 8, a los 12, a los 16",120,560,960,38,fx="up",**{"in":t[2]}),
 check("Dónde poner la zona sin teléfono, y por qué el lugar lo es todo",120,650,960,38,fx="up",**{"in":t[3]}),
 check("Plan semana por semana: qué va a pasar y cuándo viene la resistencia",120,760,960,38,fx="up",**{"in":t[4]}),
 check("Acuerdo familiar para firmar juntos",120,870,960,38,fx="up",**{"in":t[5]}),
 rect(0,0,W,H,NIGHT,**{"in":t[6]}),
 text("$47",120,300,1680,200,display=True,fx="pop",style={"color":"#7E8A82","text-align":"center","text-decoration":"line-through","text-decoration-color":"#C96F4A","text-decoration-thickness":"12px"},**{"in":t[6],"out":t[7]}),
 text("$7",120,220,1680,340,display=True,fx="pop",style={"color":"#E8B79F","text-align":"center"},**{"in":t[7]}),
 text("Para que llegue a todas las familias de nuestra comunidad.",120,700,1680,52,fx="words",wordsEnd=t[7]+4,style={"color":"#D3DDD5","font-weight":"800","text-align":"center"},**{"in":t[7]+1.5}),
]))
# S6 tech reveal
L=["Y ahora, lo que te prometí.","Cuando pusimos la regla, nos faltaba una cosa: que el teléfono la obedeciera aunque nosotros no estuviéramos.","Creamos un disco. Del tamaño de un posavasos.","Lo pones en la cocina, en la entrada, en tu mesa de noche.","Las apps que tú elijas se apagan a la hora que tú elijas.","Y solo vuelven a encenderse cuando el teléfono toca el disco. Físicamente. Donde tú lo dejaste.","No hay contraseña que adivinar. No hay botón que apretar.","Si el disco está en la cocina, tu hijo viene a la cocina. Tú lo ves. Él lo sabe. Y nadie tuvo que gritar.","Tal vez pensaste que algo así cuesta miles de dólares.","Es un disco y una app gratuita. Cabe en un sobre.","Y te lo mostramos justo después del programa, por si tu casa necesita que la regla también sea física."]
t=sec_times(5,L)
vsl.append(scene(OFF[5],OFF[6],NIGHT,[
 text("Lo que te prometí.",120,440,1680,110,display=True,fx="pop",style={"color":"#F2F5F2","text-align":"center"},**{"in":0,"out":t[1]}),
 text("Nos faltaba una cosa: que el teléfono obedeciera<br>aunque nosotros no estuviéramos.",120,380,1680,64,display=True,fx="words",wordsEnd=t[1]+4,style={"color":"#D3DDD5","text-align":"center"},**{"in":t[1],"out":t[2]}),
 rect(0,0,W,H,"radial-gradient(circle at 50% 50%,rgba(201,111,74,.35),rgba(18,26,22,0) 40%)",**{"in":t[2],"out":t[3]}),
 ring(760,340,400,per=1.8,**{"in":t[2]+0.4,"out":t[3]}),ring(760,340,400,per=1.8,**{"in":t[2]+1.3,"out":t[3]}),
 disc(810,390,300,breathe=True,fx="pop",**{"in":t[2],"out":t[3]}),
 text("Un disco. Del tamaño de un posavasos.",120,800,1680,64,display=True,fx="words",wordsEnd=t[2]+2.5,style={"color":"#F2F5F2","text-align":"center"},**{"in":t[2],"out":t[3]}),
 img("ill5-house-zones.png",kb=[1.02,1.12],**{"in":t[3],"out":t[5]}),
 grad(bg=G16,**{"in":t[3],"out":t[5]}),
 text("Cocina. Entrada. Tu mesa de noche.",120,220,900,70,display=True,fx="words",wordsEnd=t[3]+2.5,style={"color":"#F2F5F2"},**{"in":t[3],"out":t[5]}),
 text("Las apps que tú elijas se apagan a la hora que tú elijas.",120,500,900,50,fx="words",wordsEnd=t[4]+3,style={"color":"#E8B79F","font-weight":"800"},**{"in":t[4],"out":t[5]}),
 img("ill6-disc-tap.png",kb=[1.0,1.1],**{"in":t[5],"out":t[8]}),
 grad(bg=G16,**{"in":t[5],"out":t[8]}),
 text("Solo vuelven cuando el teléfono toca el disco.",120,220,900,68,display=True,fx="words",wordsEnd=t[5]+3,style={"color":"#F2F5F2"},**{"in":t[5],"out":t[8]}),
 text("Físicamente. Donde tú lo dejaste.",120,460,900,50,fx="up",style={"color":"#E8B79F","font-weight":"800"},**{"in":t[5]+3.5,"out":t[8]}),
 strike("Sin contraseña que adivinar",SVG_LOCK,120,600,44,**{"in":t[6],"out":t[8]}),
 strike("Sin botón que apretar",SVG_APP,120,710,44,**{"in":t[6]+1.5,"out":t[8]}),
 text("Si el disco está en la cocina, tu hijo viene a la cocina. Tú lo ves. Él lo sabe.",120,860,1000,44,fx="words",wordsEnd=t[7]+4,style={"color":"#F2F5F2","font-weight":"800"},**{"in":t[7],"out":t[8]}),
 rect(0,0,W,H,SAND,**{"in":t[8]}),
 text("¿Miles de dólares?",120,330,1680,130,display=True,fx="pop",style={"color":"#8A948E","text-align":"center"},**{"in":t[8],"out":t[9]}),
 text("Un disco y una app gratuita.",120,280,1680,110,display=True,fx="pop",style={"color":INK,"text-align":"center"},**{"in":t[9]}),
 text("Cabe en un sobre.",120,460,1680,80,display=True,fx="up",style={"color":CLAY,"text-align":"center"},**{"in":t[9]+1.6}),
 card("ill8-car-work-church.png",360,620,1200,330,kb=[1,1.05],fx="up",**{"in":t[10]}),
 text("Te lo mostramos justo después del programa.",120,980,1680,36,fx="up",style={"color":"#8A948E","font-weight":"800","text-align":"center"},**{"in":t[10]+1}),
]))
# S7 close
L=["Esto es lo que va a pasar ahora. Toca el botón, obtén el Programa Familiar por siete dólares, y en dos minutos lo tienes en tu correo.","Si en treinta días tu casa no se siente distinta, nos escribes y te devolvemos los siete dólares. Sin preguntas.","Nosotros somos una familia que decidió no rendirse. Y cada programa que vendemos nos permite seguir ayudando a las familias que vienen detrás.","Tu casa puede sentirse distinta esta misma semana. Toca el botón."]
t=sec_times(6,L)
vsl.append(scene(OFF[6],VSL_DUR+0.01,SAND,[
 img("ill7-dinner-after.png",kb=[1.05,1.12],alpha=0.18),
 text("Esto es lo que va a pasar ahora.",120,140,1680,60,display=True,fx="up",style={"color":"#4A5650","text-align":"center"}),
 btn("Obtener el Programa Familiar · $7 →",460,260,1000,130,48,pulse=True,fx="pop",**{"in":0.8}),
 text("En 2 minutos lo tienes en tu correo.",120,420,1680,36,fx="up",style={"color":"#8A948E","font-weight":"800","text-align":"center"},**{"in":1.6}),
 seal("30 días<br>garantía",120,560,200,34,fx="pop",**{"in":t[1]}),
 text("Si tu casa no se siente distinta, te devolvemos los $7. Sin preguntas.",360,590,1000,44,fx="words",wordsEnd=t[1]+3,style={"color":INK,"font-weight":"800"},**{"in":t[1]}),
 text("Una familia que decidió no rendirse. Cada programa ayuda a las familias que vienen detrás.",120,800,1680,38,fx="up",style={"color":"#4A5650","font-weight":"800","text-align":"center"},**{"in":t[2]}),
 text("Tu casa puede sentirse distinta esta misma semana.",120,920,1680,52,display=True,fx="up",style={"color":CLAY,"text-align":"center"},**{"in":t[3]}),
]))
json.dump({"w":W,"h":H,"fps":24,"duration":VSL_DUR,"audio":"../assets/vo/vsl-full.mp3","vars":VARS,"scenes":vsl},open("vsl.json","w"),ensure_ascii=False,indent=0)
print("ad",AD_DUR,len(ad),"scenes | vsl",round(VSL_DUR,2),len(vsl),"scenes")
