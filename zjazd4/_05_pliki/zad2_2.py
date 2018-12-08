from collections import defaultdict

# default_value = lambda x,y: x+y
default_value = lambda : 0
with open('logs.txt','r') as f:
    suma_czasow = defaultdict(default_value)
    for linia in f.readlines():
        user,akcja,czas = linia.split(';')
        czas = int(czas)
        if akcja == 'LOGIN':
            suma_czasow[user] -= czas
        else:
            suma_czasow[user] += czas

for linia in suma_czasow:
    print(f'{linia}:{suma_czasow[linia]}')
