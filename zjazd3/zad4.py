class Product():
    NEXT_ID = 1

    def __init__(self, name,price):
        self.id = Product.NEXT_ID
        Product.NEXT_ID += 1
        self.name = name
        self.price = price

    def print_info(self):
        print(f'{self.name}: ID:={self.id}, cena:={self.price}')

# x = Product('jabłko',10)
# y = Product('gruszka',15)
# x.print_info()
# y.print_info()
# print(Product.NEXT_ID)

# koszyk (basket)
# {etykietka:wartość}
# {id:ilosc}
# {produkt:ilosc}
#
# slownik
# {id: produkt}
class Basket():
    def __init__(self):
        self.products = dict()

    @property
    def is_empty(self):
        return not self.products

    def add_product(self, product, amount):
        if product in self.products:
            self.products[product] += amount
        else:
            self.products[product] = amount

    def count_total_price(self):
        total = 0
        for p in self.products:
            total += p.price * self.products[p]
        return total

    def info(self):
        for x in self.products:
            print(x.print_info)

# test składa się z trzech etapów:
#  przygotowanie środowiska
#  wywołanie testowanej funkcjonalności
#  sprawdzenie efektów, czy sa zgodne ze specyfikacją

def test_pusty_koszyk():
    b = Basket()
    assert len(b.products) == 0
    assert b.is_empty

def test_pierwszy_produkt():
    b = Basket()
    p = Product('jabłko',4)
    b.add_product(p,5)
    assert len(b.products) == 1

def test_dwa_razy_produkt():
    b = Basket()
    p = Product('gruszka',12)
    b.add_product(p,3)
    b.add_product(p,7)
    assert len(b.products) == 1
    assert b.products[p] == 10

def test_suma():
    b = Basket()
    p1 = Product('gruszka', 12)
    b.add_product(p1, 3)
    b.add_product(p1, 7)
    p2 = Product('jabłko', 4)
    b.add_product(p2, 5)
    assert b.count_total_price() == 140