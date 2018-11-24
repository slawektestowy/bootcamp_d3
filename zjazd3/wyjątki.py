b = 'nie mam jeszcze nadanej wartości'
try:
    d = int([])
    a = 'ala'
    b = int(a)
    c = 1/0

except ValueError:
    # mój kawalek obslugi błędu
    print(f'"{a}" to nie jest liczba')
    # rzucanie wyjątku, żeby kod mnie wywołujący też miał szansę zareagować na nietypową sytuację
    raise ValueError
except ZeroDivisionError:
    print('nie dziel przez 0 głąbie')
# except Exception:
#     print('jakiś inny błąd')
else:
    print(b)
finally:
    print('ten blok zawsze się wykona, '
          'niezależnie czy wystapił błąd czy wszystko poszło pomyślnie')