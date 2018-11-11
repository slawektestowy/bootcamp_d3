# class MojWyjatek(Exception):
#     pass
#
#
# try:
#     print('przed wyjatkiem')
#     raise MojWyjatek
#     print('po wyjatku')
# except:
#     print('zlapany')
#
# testowanie kodu, który powinien rzucić wyjatek

# test przejdzie tylko jesli wyjątek rzeczywiście zostanie rzucony

import pytest


def test_zlap_wyjatek():
    with pytest.raises(ZeroDivisionError):
        print('attata')

        # 1/0# definicja mojego wyjatku


class MojWyjatek(Exception):
    pass


try:

    print('przed wyjatkiem')

    raise MojWyjatek()

    print('po wyjatku')

except:

    print('zlapany')