
b= "nie ma jeszcze nadanej wartosci"
try:
    a = "ala ma"
    b = int(a)
    c = 11 / 0
    d = int([])
except ValueError:
    print ("to nie jest liczba")
    raise ValueError
else:
    print(b)
finally:
    print("ten blok zawsze sie wykona, "
          "niezaleznie czy cos tam cos tam")