import sys



print(sys.argv)

with open(sys.argv[1], 'r') as f:
    linie = f.readlines()
    print(linie)