from collections import deque

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Figure:
    """
    A super class describing a figure
    """
    def __init__(self, x_pos=0, y_pos=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dot = 'f'
        self.sm_x = deque([1, 0, -1, 0])
        self.sm_y = deque([0, 1, 0, -1])

    def point_to_pix(self, point, width, height):
        x_perc = point.x / 100
        y_perc = point.y / 100
        x = int(width * x_perc)
        y = int(height * y_perc)
        return (x, y)
    def grid_size(self, grid):
        height = len(grid)
        width =  len(grid[0])
        return (width, height)

    def static_move(self):
        self.move(self.sm_x[0], self.sm_y[0])
        self.sm_x.rotate(1)
        self.sm_y.rotate(1)

    def draw(self, grid):
        '''Draws the figure onto the grid'''
        return

    def move(self, add_x=1, add_y=1):
        self.x_pos += add_x
        self.y_pos += add_y

class Square(Figure):
    def __init__(self, x_pos=0, y_pos=0, side=3):
        super().__init__(x_pos, y_pos)
        self.side = side
        self.dot = 'x'

    def grow(self, side_inc = 1):
        self.side += side_inc

    def _update_sklt(self):
        self.sklt = [Point(self.x_pos,
                           self.y_pos),
                     Point(self.x_pos + self.side,
                           self.y_pos + self.side)]

    def draw(self, grid):
        self._update_sklt()
        (width, height) = self.grid_size(grid)
        luc = self.point_to_pix(self.sklt[0], width, height)
        rlc = self.point_to_pix(self.sklt[1], width, height)
        for y in range(luc[1], rlc[1]+1):
            try:
                for x in range(luc[0], rlc[0]+1):
                    grid[y][x] = self.dot
            except IndexError:
                pass
        return grid

