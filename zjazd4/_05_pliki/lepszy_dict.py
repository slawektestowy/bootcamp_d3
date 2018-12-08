from collections import defaultdict

default_value = lambda : 'ala ma kota'

a = defaultdict(default_value)
print(a['r'])