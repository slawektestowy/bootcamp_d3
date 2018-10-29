# komentarz

# liczby całkowite
10
0
-1000
# float - zmiennoprzecinkowe
3.5
10.0
10.
0.5
.5

+ - * /
** // %

00000000
128|64|32|16|8|4|2|1
0|0|0|0|0|1|1|1 << 2
0|0|0|1|1|1|0|0  = 16+8+4=28

<<
>>
& - and dwie liczby reprezentowane binarnie
7 & 32 = 0
7 & 28 = 4

| -  or tylko  0 or  0 = 0 , w każdym innym przypadku 1

7 | 28 = 31
^ - xor - prawda jesli bity są różne
7 ^ 28 = 27

~ - not
~7
255-7 = 148

0-255
-128+127

0-65tys
-32tys +32tys

print("""
wielolinikowy
tekst
:)
""")

print(f"Wynik dodawania {2 + 2}")
print(f"Wynik dodawania {2 + 2.88888}")
print(f"Wynik dodawania {2 + 2.88888:.2f}")
print(f"Wynik dodawania #{2000 + 2.88888:20.2f}#")
print(f"Wynik dodawania #{2000 + 2.88888:^20.2f}#")
print(f"Wynik dodawania #{2000 + 2.88888:_^20.2f}#")

