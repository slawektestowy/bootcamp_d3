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
