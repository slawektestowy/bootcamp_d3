class Product():
    def __init__(self,id, name,price, blabla):
        self.id = id
        self.name = name
        self.price = price
        self.blabla = blabla

    def print_info(self):
        print(f'{self.name}: ID:={self.id}, cena:={self.price}')


x = Product(5,'Jabłko', 5,'blublu')
y = Product(6,'gruszka', 20,'lalala')

x.print_info()

print( x.name)
print(x.blabla)
print(y.id)

x.id = 8

print(x.id)
print(y==x)

