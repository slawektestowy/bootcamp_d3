class Product():
    def __init__(self, id, name, price, blabla):
        self.id = id
        self.name = name
        self.price = price
        self.blabla = blabla
        self.id = 9


    def print_info(self):
        print(f'{self.name}: id:={self.id}, cena:={self.price}')

x = Product(5, 'jablko', 10,'blublu')



print(x.name)
x.print_info()