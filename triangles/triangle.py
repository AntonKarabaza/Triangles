from math import sqrt
from abc import ABC, abstractmethod


class Triangle(ABC):
    @abstractmethod
    def count_square(self):
        pass


class TriangleFromString(Triangle):

    def __init__(self, raw_string):
        splitted_data = [splitted_data.strip() for splitted_data in
                         raw_string.split(",")]

        if len(splitted_data) != 4:
            raise Exception("Wrong parameters number!")

        self._name = splitted_data[0]
        self._first_side = float(splitted_data[1])
        self._second_side = float(splitted_data[2])
        self._third_side = float(splitted_data[3])

    def count_square(self):
        p = (self._first_side + self._second_side + self._third_side) / 2
        square = sqrt(p * (p - self._first_side) * (p - self._second_side) *
                      (p - self._third_side))
        return square

    def __str__(self):
        return "[{name}]: {square:.2f} cm.".format(name=self._name,
                                                   square=self.count_square())


class Triangles:

    def __init__(self, *triangles: Triangle):
        self._triangles = list(triangles)

    def print_in_square_desc_order(self):
        sorted_triangles = sorted(self._triangles,
                                  key=lambda triangle: triangle.count_square(),
                                  reverse=True)

        print("================= Triangles list: =================")
        for number, triangle in enumerate(sorted_triangles, start=1):
            print("{num}.{triangle}".format(num=number, triangle=triangle))
