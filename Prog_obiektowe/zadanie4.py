class Product():
    NEXT_ID = 1

    def __init__(self, name, price):
        self.id = Product.NEXT_ID
        Product.NEXT_ID += 1
        self.name = name
        self.price = price

    def print_info(self):
        print(f'{self.name}: id:={self.id}, cena:={self.price}')


# x = Product('jablko', 10)
# y = Product('gruszka',15)
#
# x.print_info()
# y.print_info()
# print(Product.NEXT_ID)

class Basket():
    def __init__(self):
        self.products = dict()

    def add_product(self, product, amount):
        if product in self.products:
            self.products[product] += amount
        else:
            self.products[product] = amount

    def count_total_price(self):
        pass


# test skalda sie z trzech etapow
# przygotowanie srodowiska
# wywolanie testowanej funkcjonalnosci
# sprawdzenie efektów, czy sa zgodne z specyfikacja


def test_pusty_koszyk():
    b = Basket()
    assert len(b.products) == 0


def test_pierwszy_produkt():
    b = Basket()
    p = Product('jablko', 4)
    b.add_product(p, 5)
    assert len(b.products) == 1


def test_dwa_razy_produkt():
    b = Basket()
    p = Product('gruszka', 12)
    b.add_product(p, 3)
    b.add_product(p, 7)
    assert len(b.products) == 1
    assert b.products[p] == 10


def test_suma():
    b = Basket()
    p1 = Product('gruszka', 12)
    b.add_product(p1, 3)
    b.add_product(p1, 7)
    p2 = Product('jablko', 4)
    b.add_product(p2, 3)
    assert b.count_total_price() == 10
