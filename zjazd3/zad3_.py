class ElectricCar():
   def __init__(self,zasieg):
       self.przejechane = 0
       self.zasieg = zasieg

   def drive (self,planowane):
       if planowane <= self.zasieg-self.przejechane:
           self.przejechane += planowane
           print (f'Ok, zostanie {self.zasieg-self.przejechane}km do przejechania.\n '
                  f'Pozostaje {((self.zasieg-self.przejechane)/self.zasieg)*100:.0f}% '
                  f'baterii')

       else:
           print(f'Nie wystarczy baterii, poniewaz przekracasz '
                 f'dystans o {planowane-(self.zasieg-self.przejechane)}km.\n'
                 f'Potrzebne doladowanie baterii o '
                 f'{((planowane-(self.zasieg-self.przejechane))/self.zasieg)*100:.0f}%')
           

    def charge(self):
        self.przejechane =0

car = ElectricCar(150)
car.drive(140)
car.drive(50)