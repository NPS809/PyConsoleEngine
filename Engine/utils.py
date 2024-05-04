import math
from Engine.error import Error
from Engine.texts import *


class v2:
    x: int
    y: int

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return v2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return v2(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return v2(self.x * other.x, self.y * other.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __divmod__(self, other):
        return v2(self.x / other.x, self.y / other.y)

    def __idiv__(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __abs__(self):
        return v2(abs(self.x), abs(self.y))

    def __len__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"


class Dot:
    def __init__(self, sign: str, offset: v2):
        self.sign = sign
        self.offset = offset


def ConvertStringToDot(string: str):
    try:
        sign, offset = string.replace(" ", "").split(";")
        if len(sign) > 1:
            return Error(13, f">>> {sign} <<<")
        x, y = offset.split("|")
        return Dot(sign, v2(int(x), int(y)))
    except ValueError:
        return Error(12, f" >>> {string} <<< \n{text["rpos"]}")


def RemoveEmptyStringsFromList(spisok: list):
    while "" in spisok:
        spisok.remove("")
    return spisok
