#print("asasa\nsasasa")

# def nasza_funkcja(a, b="hopsasa", *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#
# #nasza_funkcja(3)
# nasza_funkcja(3, 5,6,8,9,10, end='koniec')

# def nasza_funkcja1(a, b, *args, **kwargs):  # zle, nie dziala
#     suma = (a +b + (*args + **kwargs))
#     return suma
#
#
# print(nasza_funkcja1(1, 3, 5,6))

def suma(*args):
    #print(args)
    wynik = 0
    for i in args:
        wynik += i
    return wynik

print(suma(1,4,6,7,4,6,2))


def formatuj(*args, **kwargs):
    napis = '\n'.join(args)
    for i in kwargs:
       napis= napis.replace(f'${i}', kwargs[i])
    return napis

print(formatuj("tu jakis $napis", "jakis inny $napis", napis="cos"))
