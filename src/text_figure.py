from shapes import Figure, Point
from collections import deque

class TextFigure(Figure):

    def __init__(self, x_pos=0, y_pos=0, text=""):
        super().__init__(x_pos, y_pos)
        self.sm_x = deque([0])
        self.sm_y = deque([2, 0, 0, 0, -2, 0, 0, 0])
        lines = str.splitlines(text)
        self.char_mat = [list(v) for v in lines]

    def draw(self, grid):
        (width, height) = self.grid_size(grid)
        [sx, sy] = self.point_to_pix(Point(self.x_pos, self.y_pos),
                                  width, height)
        for y, cl in enumerate(self.char_mat):
            y += sy
            for x, c in enumerate(cl):
                x += sx
                try:
                    grid[y][x] = c
                except IndexError:
                    pass
        return grid
