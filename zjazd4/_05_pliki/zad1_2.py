import sys

# with open(sys.argv[1],'r') as f:
# with open ('plik.txt','w') as f:
#     f.write('basia ma kota')

try:
    # path = '\\'.join(sys.argv[0].split('\\')[0:-1])
    # print(path)
    # path += '\\' + sys.argv[1]
    # print(path)
    # with open(path, 'r') as f:
    with open(sys.argv[1], 'r') as f:
        for x,wart in enumerate(f.readlines()):
            print(f'{x+1}: {wart}', end='')
except FileNotFoundError:
    print('nie ma pliku:',sys.argv[1])
    # print(path)
except IndexError:
    print('podaj nazwę pliku do odczytania, np: zad1_2.py plik.txt')