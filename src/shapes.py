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

class Rectangle(Figure):
    def __init__(self, x_pos=0, y_pos=0, side_x=3, side_y=3):
        super().__init__(x_pos, y_pos)
        self.side_x = side_x
        self.side_y = side_y
        self.dot = 'x'

    def grow(self, side_inc = 1):
        self.side_x += side_inc
        self.side_y += side_inc

    def _update_sklt(self):
        self.sklt = [Point(self.x_pos,
                           self.y_pos),
                     Point(self.x_pos + self.side_x,
                           self.y_pos + self.side_y)]

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

class Circle(Figure):
    def __init__(self, pos_x=0, pos_y=0, radius=3):
        super().__init__(pos_x, pos_y)
        self.radius = radius
        self.dot = '+'

    def grow(self, rad_inc = 1):
        self.radius += rad_inc

    def _update_sklt(self):
        self.sklt = [Point(self.x_pos,
                           self.y_pos),
                     Point(self.x_pos + self.radius * 2,
                           self.y_pos + self.radius * 2)]

    def _is_inside(self, x, y, rad, center):
        rad2 = rad * rad
        dist2 = (x - center[0])**2 + (y-center[1])**2
        return dist2 <= rad2

    def draw(self, grid):
        # ugly temporary way of drawing a circle
        self._update_sklt()
        (width, height) = self.grid_size(grid)
        #left upper corner
        luc = self.point_to_pix(self.sklt[0], width, height)
        #right lower corner
        rlc = self.point_to_pix(self.sklt[1], width, height)

        rad_x = (rlc[0] - luc[0]) / 2
        rad_y = (rlc[1] - luc[1]) / 2

        rad = 0
        y_fact = 1
        x_fact = 1
        if rad_x < rad_y:
            x_fact = rad_y / rad_x
            rad = rad_y
        else:
            y_fact = rad_x / rad_y
            rad = rad_x
        cx = luc[0] + rad_x
        cy = luc[1] + rad_y
        center = (cx, cy)

        for y in range(luc[1], rlc[1] + 1):
            try:
                for x in range(luc[0], rlc[0] + 1):
                    x_diff = (cx - x) * x_fact
                    y_diff = (cy - y) * y_fact
                    X = cx + x_diff
                    Y = cy + y_diff
                    if(self._is_inside(X, Y, rad, center)):
                        grid[y][x] = self.dot
            except IndexError:
                pass
        return grid
