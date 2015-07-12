from shapes import *
class Human(Figure):
    def __init__(self, x_pos=0, y_pos=0, width=20, height=30):
        super().__init__(x_pos, y_pos)
        self.width = width
        self.height = height
        self.dot = 'x'
        self.parts = []
        self._generate_parts()

    def _generate_parts(self):
        head_start_y = self.y_pos
        head_rad = self.height // 8
        head_rad = head_rad if head_rad * 2 < self.width // 2 else self.width // 2
        head_start_x = self.x_pos + (self.width - head_rad * 2) // 2
        self.parts.append(Circle(head_start_x, head_start_y, head_rad, '!'))

        neck_start_y = self.y_pos + self.height // 4
        neck_width = head_rad
        neck_height = self.height // 9
        neck_start_x = self.x_pos + (self.width - neck_width) // 2
        self.parts.append(Rectangle(neck_start_x, neck_start_y, neck_width, neck_height, '#'))

        body_start_x = self.x_pos + self.width * 2 // 7
        body_width = self.width * 3 // 7
        body_height = self.height // 3
        body_start_y = neck_start_y + neck_height
        self.parts.append(Rectangle(body_start_x, body_start_y, body_width, body_height, '='))

        arms_start_y = body_start_y
        arms_width = body_width // 5
        arms_height = body_height * 6 // 5
        arm_l_start_x = body_start_x - arms_width
        arm_r_start_x = body_start_x + body_width
        self.parts.append(Rectangle(arm_l_start_x, arms_start_y, arms_width, arms_height, '('))
        self.parts.append(Rectangle(arm_r_start_x, arms_start_y, arms_width, arms_height, ')'))


        legs_start_y = body_start_y + body_height
        legs_width = body_width // 5
        leg_l_start_x = body_start_x + legs_width
        leg_r_start_x = body_start_x + 3 * legs_width
        legs_height = self.height - (body_start_y + body_height - self.y_pos)
        self.parts.append(Rectangle(leg_l_start_x, legs_start_y, legs_width, legs_height, '\\'))
        self.parts.append(Rectangle(leg_r_start_x, legs_start_y, legs_width, legs_height, '/'))




    def grow(self, inc = 1):
        for part in parts:
            part.grow(inc)

    def move(self, add_x=1, add_y=1):
        for part in self.parts:
            part.move(add_x, add_y)

    def draw(self, grid):
        for part in self.parts:
            part.draw(grid)
        return grid
