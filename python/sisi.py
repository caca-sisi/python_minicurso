
from musica_piano import*
import turtle
import random
sisi=turtle.Turtle()
janela=sisi.Screen()
sisi.color("blue")
def P1():
    Do.toca(1)
    Mi.toca(1)
    Re.toca(1)
    Do.toca(1)
for i in range (360):
    sisi.fd(200)
    sisi.bk(200)
    sisi.rt(1)
sisi.color("yellow")
sisi.circle(5)
P1()
janela.mainloop()
