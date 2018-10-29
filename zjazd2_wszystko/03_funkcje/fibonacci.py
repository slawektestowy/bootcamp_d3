def fibonacci(n):
    jedna_temu = 1
    dwie_temu = 1
    if n == 1 or n == 2:
        return 1
    for i in range(3, n + 1):
        wynik = jedna_temu + dwie_temu
        dwie_temu = jedna_temu
        jedna_temu = wynik
    return jedna_temu
    # return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(1000))