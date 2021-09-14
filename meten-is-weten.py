A = input('kies een heel getal tussen de 1 en de 100: ')
B = input('Kies nog een heel getal tussen de 1 en de 100: ')
MAX = A
MIN = A
if (A > B):
    print('A is het grootste getal: ' + str(MAX))
elif (A < B):
    print('A is het kleinste getal: ' + str(MIN))
else :print('B is groter dan A')