from random import random

class AccessDeniedError(Exception):
    pass

class UkryteZasoby:
    login = 'ala'
    haslo = 'makota'

    def __init__(self,login, haslo):
        self._moje_tajne_dane = 'ala ma kota'
        self._czy_jest_dostep = False
        self.login = login
        self.haslo = haslo

    def autoryzacja(self, login, haslo):
        self._czy_jest_dostep = \
            (self.login, self.haslo) == (login, haslo) \
            or (UkryteZasoby.login, UkryteZasoby.haslo) == (login, haslo)

    # getter
    @property
    def dane(self):
        if self._czy_jest_dostep:
            return self._moje_tajne_dane
        else:
            raise AccessDeniedError

    @dane.setter
    def dane(self,nowe_dane):
        if self._czy_jest_dostep:
            self._moje_tajne_dane = nowe_dane
        else:
            raise AccessDeniedError

    @dane.deleter
    def dane(self):
        if self._czy_jest_dostep:
            self._czy_jest_dostep = False
        else:
            raise AccessDeniedError

a = UkryteZasoby('agata','tajne haslo')
a.autoryzacja('bledny login','bledne haslo')
print(a.dane)
a.dane='kot ma alę'
print(a.dane)
del a.dane
print(a.dane)