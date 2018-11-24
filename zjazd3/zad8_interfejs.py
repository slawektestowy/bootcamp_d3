from zad8 import CashMachinePremium, StackError, BadBanknotesError, WrongAmountError

# przygotowanie bankomatu
cm = CashMachinePremium(7)

try:
    cm.put_money([100,50,200,50,100,50])
except StackError:
    print('za dużo banknotów, nie mieści się')
    exit(1)

# kilka wypłat
while True:
    res = input('Podaj kwotę do wypłaty: ')

    # sprawdź czy enter -> jeśli tak to zakończ
    if res in ['','Koniec','papa','exit','quit','q','x']:
        print('Koniec')
        exit(0)

    # sprawdź czy liczba -> jeśli nie to wypisz komunikat
    try:
        amount = int(res)
    except ValueError:
        print('to nie jest liczba')
        continue

    # spróbuj wypłacić -> obsłuż wyjatki
    try:
        cash = cm.withdraw_money(amount)
        print('proszę, tu są Twoje banknoty: ',cash)
    except (BadBanknotesError, WrongAmountError) as e:
        print('zmień kwotę')
