#!/usr/bin/python3
from terminal_draw import TerminalDraw
from shapes import *
from human import Human
from text_figure import TextFigure
from control import KeyboardControl as KC
t = TerminalDraw()
s1 = Rectangle(30,70,12,12)
s2 = Rectangle(40,60,12,12)
s3 = Rectangle(50,70,12,12)
s4 = Rectangle(55,65,20,40)
tf1 = TextFigure(40,10,"hello\nI see yoou!!   ")
c1 = Circle(20,20,30)
h1 = Human(0,0,30,50)

mv_s4_l = lambda: h1.move(-2, 0)
mv_s4_r = lambda: h1.move(2, 0)
mv_s4_u = lambda: h1.move(0, -2)
mv_s4_d = lambda: h1.move(0, 2)

grow_s4 = lambda: h1.grow(2)
shrink_s4 = lambda: h1.grow(-2)

kc = KC()

kc.add_handler('a', mv_s4_l)
kc.add_handler('d', mv_s4_r)
kc.add_handler('w', mv_s4_u)
kc.add_handler('s', mv_s4_d)

kc.add_handler('p', grow_s4)
kc.add_handler('o', shrink_s4)
kc.start()

#t.add_figure(s1)
#t.add_figure(s2)
#t.add_figure(s3)
#t.add_figure(s4)
#t.add_figure(tf1)
#t.add_figure(c1)
t.add_figure(h1)
t.animate(fps=4, tot_time = 20)

