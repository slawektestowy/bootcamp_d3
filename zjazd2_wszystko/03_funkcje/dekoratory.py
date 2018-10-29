from time import time

def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

def czas(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        stop_time = time()
        print(f"Wywołanie funkcji zajęło {stop_time - start_time}s")
    return wrapper

def dekorator(func):
    def wrapper(*args, **kwargs):
        print("Przed funkcją")
        func(*args, **kwargs)
        func(*args, **kwargs)
        print("Po funkcji")
    return wrapper

@dekorator #lukier syntaktyczny
def nasza_funkcja(x):
    print(f"Wewnątrz funkcji {x}")

def fun_bez_dekoratora():
    print("Bez dekoratora")

@dekorator
@czas
def funkcja(x):
    return fib(x)

nasza_funkcja("coś")
dekorator(fun_bez_dekoratora)()

funkcja(30)