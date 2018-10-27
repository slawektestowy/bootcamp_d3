# komentarz

# liczby calkowite

10
0
-1000

# float - zmiennoprzecinkowe
3.5
10.0
10.
.5
#nadmiarowe zera mozna pominac

+ - * /
** potega
// dzialanie na liczbach calkowitych np 9/2 bedzie sie rownac 4
% modulo - reszta z dzielenia


<< przesuwa w systemie dwojkowym w lewo wartosci - shift
>> to samo w prawo
& - dwie liczby reprezentowane binarnie - zachowanie logiczne
7 & 32 = 0
7 & 28 = 4

| - or cos lub cos, prawda lub falsz to prawda 0 or 0 = 0 w kazdym innym przypadku 1
7 | 28 = 31

^ xor - prawda jesli bity sa rozne, jedno albo drugie
7 ^ 28 = 27

~ not odwrocenie bitow

round - zaokraglanie round(4.3333, 1) zaokragla do pierwszego miejsca po przecinku

napisy - print ("hello world") tak samo zadziala print ('hello world')
ale jesli chcemy uzyc apostrofu w napisie to juz musza byc cudzyslowa i odwrotnie ("O'Hara")  ('powiedzial"czesc"') print ("'\"'") backslash powoduje brak interpretacji
print ("""wielolinijkowy
... tekst""")


print ("Ala " + "ma kota")

print (f"Wynik dodawania {2 + 2}")   - klamerki pozwalaja na uzycie zmiennych plus musi byc parametr f

print (f"Wynik dodawania {2 + 2.888888: .2f}") dwukropek oznacza jak ma byc formatowany wynik. .2f oznacza zaokraglanie po przecinku do dwoch miesc a liczba ma byc traktowana jako float

print (f"Wynik dodawania {2 + 2.888888: 20.2f}") - wyrownuje do 20 znakow
print (f"Wynik dodawania {2 + 2.888888: ^20.2f}") - wyrownuje do 20 znakow i wysrodkowuje
print (f"Wynik dodawania {2 + 2.888888: _^20.2f}") - zastepuje spacje podkreslnikiem




Wartosci logiczne musza byc pisane duzymi literami

True
False

True and False
True or False
not True
not False


bool - puste obiekty jako false pelne jako true
bool(0) - False
bool (8) - True


Typu zmiennych nie deklarujemy, mamy etykietki ktore moga przyjmowac cos dowolnego, x moze byc liczba lub napisem plus potem moze sie to zmienic

x = 2
x = 'ala ma kota'
x +  ' a kot ma ale' - dodaje do istniejacej wartosci cos nowego

== sprawdz czy jest rowne, sprawdzamy czy dana zmienna ma wartosc taka jak wpisana po ==
= przypisanie wartosci do zmiennej

a = 3
b = 9
h = 6.5
p = (a+b)*h/2
print(p)






