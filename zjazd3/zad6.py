# Zaimplementuj klase Vector dostarczajaca funkcjonalnosc wektora
# swobodnego na dwuwymiarowej płaszczyznie. Wektory powinny
# miec mozliwosc dodawania, odejmowania, mnozenia (przez liczbe),
# porównywania (po długosci) oraz powinny posiadac czytelna
# reprezentacje napisowa.

class Vector():
    """ala ma kota : miejsce na dokumentację"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def len(self):
        """zwraca długość wektora"""
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, mul):
        return Vector(x=self.x * mul, y=self.y * mul)

    def __gt__(self, other):  # greater than >
        return self.len > other.len

    def __ge__(self, other):  # grater equal >=
        return self.len >= other.len

    def __lt__(self, other):  # less than <
        return self.len < other.len

    def __le__(self, other):  # less equal <=
        return self.len <= other.len

    def __eq__(self, other):  # equal ==
        return self.len == other.len

    def __ne__(self, other):  # not equal !=
        return self.len != other.len

    def __str__(self):
        return f'Vector : x={self.x},y={self.y}'


# print(Vector(2,3))

def test_len():
    v = Vector(3, 4)
    assert v.len == 5


def test_add():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=3, y=5)
    vector_3 = vector_1 + vector_2
    assert vector_3.x == 4 and vector_3.y == 7


def test_sub():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=3, y=5)
    vector_3 = vector_1 - vector_2
    assert vector_3.x == -2 and vector_3.y == -3


def test_mul():
    vector_1 = Vector(x=1, y=2)
    a = 3
    vector_2 = vector_1 * a
    assert vector_2.x == 3 and vector_2.y == 6


def test_greater_than():
    v1 = Vector(2, 3)
    v2 = Vector(1, 1)
    assert v1 > v2


def test_sort():
    v1 = Vector(2, 3)
    v2 = Vector(1, 1)
    v3 = Vector(2, 2)
    lista = [v1, v2, v3]
    lista.sort()
    assert lista == [v2, v3, v1]
