# Zadanie #3
# Zaimplementuj klase ElectricCar odwzorowujaca zachowanie
# samochodu elektrycznego. Klasa powinna umozliwiac pokonanie
# zadanego dystansu, który nie moze przekroczyc maksymalnego
# zasiegu zdefiniowanego dla samochodu. Samochód powinien
# miec takze mozliwosc naładowania baterii.
# >>> car = ElectricCar(100)    #<-maksymalny zasięg na pełnej baterii
# >>> car2 = ElectricCar(150)   #<-maksymalny zasięg na pełnej baterii
# >>> car3 = ElectricCar(60)    #<-maksymalny zasięg na pełnej baterii
# >>> car.drive(70)
# 70
# >>> car.drive(50)
# 30
# >>> car.drive(50)
# 0
# >>> car.charge()
# >>> car.drive(50)
# 50

class ElectricCar():
    def __init__(self, max_dist):
        self.MAX_DIST = max_dist    #jaki maksymalny dystans może pokonać (km)
        self.dist = 0               #ile przejechał już km
        self.battery_lvl = max_dist #ile km baterii mu zostalo

    # jezdzić:
    # drive < dostępny_zasięg
        # jedziemy całe drive
        # zmniejszamy baterię
    # drive > dostępny_zasięg  to wtedy mamy problem
        # przejeżdżamy cały dostępny_zasięg
        # bateria się zeruje
    # co to jest dostępny_zasięg?
    #   battery_lvl
    #
    # ładowanie:
    # 1. ładujemy na maksa
    # 2. ładujemy o zadany poziom
        # sprawdzamy czy nie przekroczymy dopuszcczalnego maksymalnego poziomu