from shutil import get_terminal_size
import time
import os
import sys
class TerminalDraw:

    def __init__(self, background=' ', frame='o'):
        self.background = background
        self.frame = frame
        self._height = None
        self._width = None
        self._update_dimensions()
        self.figures = []

    def _update_dimensions(self):
        self._width, self._height = get_terminal_size()

    def add_figure(self,figure):
        self.figures.append(figure)

    def animate(self, fps=2, tot_time=10):
        os.system('clear')
        os.system('setterm -cursor off')
        sleep_time = 1.0/fps
        n_sleeps = int(tot_time/sleep_time)
        for i in range(0, n_sleeps):
            self.draw()
            for fig in self.figures:
                fig.static_move()
            time.sleep(sleep_time)
        os.system('setterm -cursor on')

    def _draw_figs(self, grid):
        for figure in self.figures:
            figure.draw(grid)
        return grid

    def draw(self):
        self._update_dimensions()
        grid = []
        frame_row = [self.frame]*self._width
        grid.append(frame_row)
        for i in range(2,self._height):
            row = [self.frame]
            for j in range(2,self._width):
                row.append(self.background)
            row.append(self.frame)
            grid.append(row)
        grid.append(frame_row)
        grid = self._draw_figs(grid)
        g = "\n".join(["".join(row) for row in grid])
        sys.stdout.write(g)
        sys.stdout.flush()
