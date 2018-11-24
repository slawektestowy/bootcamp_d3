import sys


with open(sys.argv[1], 'r') as f:
    lista = f.readlines()
    for x, wart in enumerate(lista):
        print(f'{x+1}:{wart}', end="")