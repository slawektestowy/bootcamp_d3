import os
import sys

# print(sys.argv)
#
# with open(sys.argv[1],'r') as f:
#     linie = f.readlines()
#     print(linie)

#  chodzenie po katalogach
print(os.scandir('.'))
for el in os.scandir('..'):
    print(el,'czy katalog:', el.is_dir(),', czy plik:', el.is_file(), el.name)
