from math import sqrt


class Triangle:

    def __init__(self, name, first_side, second_side, third_side):
        self.name = name
        self._first_side = first_side
        self._second_side = second_side
        self._third_side = third_side

    def count_square(self):
        p = (self._first_side + self._second_side + self._third_side) / 2
        square = sqrt(p * (p - self._first_side) * (p - self._second_side) * (p - self._third_side))

        return square
