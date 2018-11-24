class ZmiennePrywatne():
    def __init__(self):
        self._wys = 10
        self._szer = 15
        self._gl = 20

    @property
    def objetosc(self):
        return self._wys * self._szer * self._gl

x = ZmiennePrywatne()
print(f'{x.objetosc} cm3')