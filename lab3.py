#Tricky picture
picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]]

for row in picture:
    for col in row:
            print('*'if col else ' ',end='')
    print()

'''nota = input("Introdu nota: ")
if nota == '9' or nota=='10':
    print('Excelent')
elif nota == '8' or nota == '7':
    print('Bine')
elif nota == '6' or nota == '5':
    print('Suficient')
elif nota == '4' or nota == '3' or nota == '2' or nota == '1':
    print('Reexaminare')
else:
    print('Valoare invalida')'''

import random

numar = random.randint(1, 50)
numar1 = int(input("Introdu numar: "))
while numar1 != numar:
    if numar1 < numar:
        print('Numarul este mai mare')
    elif numar1 > numar:
        print('Numarul este mai mic')

    numar1 = int(input("Mai incearca: "))

print('Felicitari, ai ghicit')

