class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2 * self._height + 2 * self._width

    def get_diagonal(self):
        return (self._width ** 2 + self._height ** 2) ** .5

    def __str__(self):
        return 'Rectangle(width=' + str(self._width) + ', height=' + str(self._height) + ")"

    def get_picture(self):
        if self._width > 50 or self._height > 50:
            return 'Too big for picture.'

        picture = ''

        for i in range(0, self._height):
            picture += self._width * "*" + '\n'

        return picture

    def get_amount_inside(self, shape):
        width_amount = self._width // shape._width
        height_amount = self._height // shape._height
        return width_amount * height_amount


class Square(Rectangle):

    def __init__(self, side, width=None, height=None):
        super().__init__(width, height)
        self._side = side
        self._width = side
        self._height = side

    def __str__(self):
        return 'Square(side=' + str(self._side) + ")"

    def set_width(self, width):
        self._side = width
        self._height = width
        self._width = width

    def set_height(self, height):
        self._side = height
        self._height = height
        self._width = height

    def set_side(self, side):
        self._side = side
        self._height = side
        self._width = side

