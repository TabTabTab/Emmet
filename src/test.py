from terminal_draw import TerminalDraw
from shapes import *
from text_figure import TextFigure
from control import KeyboardControl as KC
t = TerminalDraw()
s1 = Square(30,70,12)
s2 = Square(40,60,12)
s3 = Square(50,70,12)
s4 = Square(55,65,20)
tf1 = TextFigure(40,10,"hello\nI see yoou!!   ")

mv_s4_l = lambda: s4.move(-2, 0)
mv_s4_r = lambda: s4.move(2, 0)
mv_s4_u = lambda: s4.move(0, -2)
mv_s4_d = lambda: s4.move(0, 2)

grow_s4 = lambda: s4.grow(2)
shrink_s4 = lambda: s4.grow(-2)

kc = KC()

kc.add_handler('a', mv_s4_l)
kc.add_handler('d', mv_s4_r)
kc.add_handler('w', mv_s4_u)
kc.add_handler('s', mv_s4_d)

kc.add_handler('p', grow_s4)
kc.add_handler('o', shrink_s4)
kc.start()

t.add_figure(s1)
t.add_figure(s2)
t.add_figure(s3)
t.add_figure(s4)
t.add_figure(tf1)
t.animate(fps=10, tot_time = 20)

