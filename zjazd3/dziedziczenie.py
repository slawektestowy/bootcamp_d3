# class KlasaBazowa:
#     def __init__(self):
#         self.a = 5
#         self.b = 123
#
#     def kto_ty(self):
#         print('jestem KlasaBazowa')
#
# class Podklasa(KlasaBazowa):
#     pass
#
# class Podklasa2(KlasaBazowa):
#     def __init__(self):
#         self.c = 90
#
# class Podklasa3(KlasaBazowa):
#     def __init__(self):
#         super().__init__()
#         self.d = 'ala ma kota'
#
#     def kto_ty(self):
#         print('jestem klasy: ', self.__class__.__name__)
#
# obiekt = Podklasa()
# obiekt.kto_ty()
#
# ob2 = Podklasa2()
# ob2.kto_ty()
# # print(ob2.a) # Podklasa2 nie ma atrybutu a, bo __init__ został zastąpiony
#
# ob3 = KlasaBazowa()
# ob3.kto_ty()
# # print(ob3.c)    # KlasaBazowa nie ma atrybutu c
#
# print(ob2.__class__.__name__)
# print('Czy jesteś obiektem klasy KlasaBazowa: ',isinstance(ob2, KlasaBazowa))
#
# ob4 = Podklasa3()
# ob4.kto_ty()
# print('czy mam atrybut a: ' ,ob4.a)
#

class Kolo():
    def __init__(self,r):
        self.r = r

    def powierzchnia(self):
        return 3.14 * self.r ** 2

    def obwod(self):
        return 2 * 3.14 * self.r

class Prostokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def powierzchnia(self):
        return self.a * self.b

class Walec(Kolo,Prostokat):
    def __init__(self):
        Kolo.__init__(self,3)
        Prostokat.__init__(self, self.obwod(), 10)

    def powierzchnia(self):
        podstawa = Kolo.powierzchnia(self)
        bok = Prostokat.powierzchnia(self)
        return 2* podstawa + bok

walec = Walec()
print(walec.powierzchnia())