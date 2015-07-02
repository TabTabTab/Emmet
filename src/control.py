import termios, fcntl, sys
from threading import Thread
class KeyboardControl:
    def __init__(self, quit_key='q'):
        quit_key = quit_key.lower()
        self._quit_keys = [quit_key, quit_key.upper()]
        self._key_handlers = {}
        self.stop = False

    def add_handler(self, key, handler):
        self._key_handlers[key] = handler

    def stop(self):
        self.stop = True

    def start(self):
        tr = Thread(target = self.kbhit)
        tr.start()

    def kbhit(self):
        self.stop = False
        fd = sys.stdin.fileno()
        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        try:
            while True:
                try:
                    c = sys.stdin.read(1)
                    if self.stop:
                        break;
                    if c in self._quit_keys:
                        break;
                    try:
                        self._key_handlers[c]()
                    except KeyError:
                        pass
                except IOError:
                    return False
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
