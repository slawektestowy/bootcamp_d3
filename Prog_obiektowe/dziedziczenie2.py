class Pierwsza:
    NEXT_VALUE = 1
    print('blok konstrukcyjny 1 klasy Pierwsza')

    def __init__(self):
        print("init klasy Pierwsza")

    print ('blok 2 klasy Pierwsza')

    def metoda(self):
        print("metoda klasy Pierwsza")
    print('blok 3 klasy Pierwsza')


class Druga(Pierwsza):

    print('blok konstrukcyjny 1 klasy Druga')

    def __init__(self):
        print("init klasy Druga")

    print('blok 2 klasy Druga')

    def metoda(self):
        print("metoda klasy Druga")

    print('blok 3 klasy Druga')

if __name__ == '__main__':
    print("jestem glownym watkiem")
    obiekt = Pierwsza
else:
    print("najprawdopodniej ktos mnie zaimportowal")