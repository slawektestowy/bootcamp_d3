# def silnia(x):
#    if x == 0:
#        return 1
#    return x * silnia(x-1)

    # wynik = 1
    # for i in range(1, x + 1):
    #     #print(i)
    #     wynik *= i

    # return wynik

# print(silnia(5))


# for i in range(10):
#     print(i)

# def fib_rek(n):
#     if n < 1:
#         return 0
#     if n < 2:
#         return 1
#     return fib_rek(n - 1) + fib_rek(n - 2)
#
# print(fib_rek(6))


def fibonacci(n):
    dwie_temu = 1
    jedna_temu = 1
    if n ==1 or n == 2:
        return 1
    for i in range(3, n+1):
        wynik = jedna_temu + dwie_temu
        dwie_temu = jedna_temu
        jedna_temu = wynik
    return jedna_temu
print(fibonacci(50))


    # if n ==1 or n == 2:
    #     return 1
    # return fibonacci(n-1) + fibonacci(n-2)





