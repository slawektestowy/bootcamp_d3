def dekorator(func):
    def wrapper():
        print("przed funkcja")
        func()
        print("po funkcji")
    return wrapper

@dekorator
def nasza_funkcja():
    print("wewnatrz funkcji")

nasza_funkcja()