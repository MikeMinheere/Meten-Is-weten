A = input('kies een heel getal: ')
B = input('Kies nog een heel getal: ')
MAX = int(A)
MIN = int(A)
if (A > B):
    print('A is het grootste getal: ' + str(MAX))
    MIN = B
elif (A < B):
    print('A is het kleinste getal: ' + str(MIN))
    MAX = B
else :print("A is evengroot als B")
print("met minimum is: "+ str(MIN))
print("het maximum is: "+ str(MAX))