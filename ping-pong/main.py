import turtle #iki boyutlu çizim modülü.
a = input("1.oyuncu adı (10 harften çok almaması gereklidir.)")
b = input("2.oyuncu adı (10 harften çok almaması gereklidir.)")

if len(a) > 10:
    a = a[0: 10]
if len(b) > 10:
    b = b[0: 10]

ac = open('score.txt' , 'w')

#tracer sayesinde topun akıcı saglandı.
pencere = turtle.Screen()
pencere.bgcolor('black')
pencere.setup(width=800,height=600)
pencere.title('Ping-Pong')
pencere.tracer(2)

oyuncua = turtle.Turtle()
oyuncua.penup()
oyuncua.shape('square')
oyuncua.color('white')
oyuncua.shapesize(5,1)
oyuncua.goto(-350,0)
puan_a = 0
ac.write('{}:{}\n'.format(b,puan_a))

oyuncub = turtle.Turtle()
oyuncub.penup()
oyuncub.shape('square')
oyuncub.color('white')
oyuncub.shapesize(5,1)
oyuncub.goto(350,0)
puan_b = 0
ac.write('{}:{}\n'.format(b, puan_b))


top = turtle.Turtle()
top.penup()
top.color('white')
top.shape('circle')
top.shapesize(1)
top.goto(0,0)
top.dy = 0.2
top.dx = 0.2


tablo = turtle.Turtle()
tablo.goto(-100,270)
tablo.color('white')
tablo.hideturtle()
tablo.penup()
tablo.write('{}:{}'.format(a,puan_a), align="center", font=('Courier', 1, "bold"))

tablo1 = turtle.Turtle()
tablo1.goto(100,270)
tablo1.color('white')
tablo1.hideturtle()
tablo1.penup()
tablo.write('{}:{}'.format(a,puan_a), align="center", font=('Courier', 18, "bold"))


def ust_1():
    oyuncua.sety(oyuncua.ycor()+20)# SETY Çizim yapan kalemin Y konumunu ayarlar.
def alt_1():
    oyuncua.sety(oyuncua.ycor()-20)
def ust_2():
    oyuncub.sety(oyuncub.ycor()+20)
def alt_2():
    oyuncub.sety(oyuncub.ycor()-20)
#tusa basılınca tetiklenmesini saglayan fonksiyon.(onkeypress)

pencere.listen()

pencere.onkeypress(ust_1,'w')
pencere.onkeypress(alt_1,'s')
pencere.onkeypress(ust_2,'Up')
pencere.onkeypress(alt_2,'Down')

while True:#temel olarak yorumlayıcıya mevcut kod yerine başka bir kod satırını doğrudan çalıştırmasını söyledilk(goto)
    top.goto(top.xcor() + top.dx,top.ycor()+ top.dy)
    if top.ycor() >= 300 or top.ycor() <= -300:
        top.dy = top.dy * -1#kenarlara carptığı zaman tam ters istikamete gitme b icin
    if top.xcor() >= 400:
        top.goto(0,0)
        puan_a+=1
        tablo1.clear()
        tablo1.write('{}:{}'.format(a,puan_a), align="center", font=('Courier', 18, "bold"))
        ac.write('{}:{}\n'.format(a, puan_a))
        top.dx = top.dx * -1  # kenarlara carptığı zaman tam ters istikamete gitme a icin

    if top.xcor() <= -400:
        top.goto(0,0)
        puan_b+=1
        tablo.clear()
        tablo.write('{}:{}'.format(b, puan_b), align="center", font=('Courier', 18, "bold"))
        ac.write('{}:{}\n'.format(b, puan_b))
        top.dx = top.dx*-1
    if oyuncua.ycor() + 60 >= 300:
        oyuncua.sety(240)
    if oyuncub.ycor() + 60 >= 300:
        oyuncub.sety(240)
    if oyuncua.ycor() - 60 <= -300:
        oyuncua.sety(-240)
    if oyuncub.ycor() - 60 <= -300:
        oyuncub.sety(-240)
    if (top.xcor() > 340 and top.xcor() < 350) and (
            top.ycor() < oyuncub.ycor() + 60 and top.ycor() > oyuncub.ycor() - 60):
        top.setx(340)
        top.dx = top.dx * -1
    if (top.xcor() > -350 and top.xcor() < -340) and (
            top.ycor() < oyuncua.ycor() + 60 and top.ycor() > oyuncua.ycor() - 60):
        top.setx(-340)
        top.dx = top.dx * -1
