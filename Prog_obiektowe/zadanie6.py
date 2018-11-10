# Zaimplementuj klase Vector dostarczajaca funkcjonalnosc wektora
# swobodnego na dwuwymiarowej płaszczyznie. Wektory powinny
# miec mozliwosc dodawania, odejmowania, mnozenia (przez liczbe),
# porównywania (po długosci) oraz powinny posiadac czytelna
# reprezentacje napisowa.
# Przykład uzycia:
# vector_1 = Vector(x=1, y=2)
# vector_2 = Vector(x=1, y=2)
# vector_3 = vector_1 + vector_2


class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def len(self):
        return (self.x**2+self.y**2)**(1/2)

    def __gt__(self, other):

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y)



def test_add():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=3, y=5)
    vector_3 = vector_1 + vector_2
    assert  vector_3.x == 4 and vector_3.y == 7

def test_sub():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=3, y=5)
    vector_3 = vector_1 - vector_2
    assert  vector_3.x == -2 and vector_3.y == -3

def test_greater_than()
   v1 = Vector(1,1)
   v2 = Vector(2,3)
   assert v1 > v2