# Zadanie #3
#
# Zaimplementuj klase ElectricCar odwzorowujaca zachowanie
#
# samochodu elektrycznego. Klasa powinna umozliwiac pokonanie
#
# zadanego dystansu, który nie moze przekroczyc maksymalnego
#
# zasiegu zdefiniowanego dla samochodu. Samochód powinien
#
# miec takze mozliwosc naładowania baterii.
#
#
#
#   car = ElectricCar(100)
#
#
#     >> car.drive(70)
#
#
#   70
#
#     >> car.drive(50)
#
#
#   30
#
#     >> car.drive(50)
#
#
#
#   0
#
#     >> car.charge()
#
#     >> car.drive(50)
#
#   50


class ElectricCar():
    def __init__(self, max_distance):
        self.max_distance = max_distance
        self.battery_lvl = max_distance
       #self.driving = 0

    def drive(self, km):
        if km > self.max_distance:
            print(f'Za duzy dystans w tej chwili Twoja bateria jest naldowana w {self.battery_lvl -  km} % ')


        else:
           self.max_distance -= km
           print(f'Przejechales {km} km, pozostalo Ci {self.max_distance} km')


car = ElectricCar(100)
car1 = ElectricCar(120)
car.drive(20)
car.drive(30)
car.drive(40)
car.drive(90)
car.drive(100)







