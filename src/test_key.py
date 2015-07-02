import control
from control import KeyboardControl as kc
from threading import Thread
import time

def print_a():
    print('a')

def print_b():
    print('b')

KC = kc()
KC.add_handler('a', print_a)
KC.add_handler('b', print_b)
t = Thread(target=KC.kbhit)

t.start()
time.sleep(10.0)

print(" I am done")
