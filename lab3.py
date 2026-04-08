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

'''import random

numar = random.randint(1, 50)
numar1 = int(input("Introdu numar: "))
while numar1 != numar:
    if numar1 < numar:
        print('Numarul este mai mare')
    elif numar1 > numar:
        print('Numarul este mai mic')

    numar1 = int(input("Mai incearca: "))

print('Felicitari, ai ghicit')'''

#exercitiul4
orase = ["București", "Cluj-Napoca", "Timișoara", "Iași", "Sibiu", "Cisnadie", "Valcea"]

for index, oras in enumerate(orase, start=1):
    print(f"{index}. {oras}")

#Exercitiul 5
'''import random


numere_utilizator = set()

print("Alege 6 numere între 1 și 49:")

while len(numere_utilizator) < 6:
    nr = int(input(f"Numărul {len(numere_utilizator) + 1}: "))

    if nr < 1 or nr > 49:
        print("Numărul trebuie să fie între 1 și 49!")
    elif nr in numere_utilizator:
        print("Ai ales deja acest număr!")
    else:
        numere_utilizator.add(nr)


numere_castigatoare = set(random.sample(range(1, 50), 6))


potriviri = numere_utilizator.intersection(numere_castigatoare)


print("\nNumerele tale:", sorted(numere_utilizator))
print("Numerele câștigătoare:", sorted(numere_castigatoare))
print(f"Ai ghicit {len(potriviri)} numere: {sorted(potriviri)}")

# Mesaj de câștig
if len(potriviri) == 6:
    print("Jackpot! Ai câștigat marele premiu!")
elif len(potriviri) >= 4:
    print("Felicitări! Ai câștigat un premiu!")
elif len(potriviri) >= 2:
    print("Ai câștigat un premiu mic.")
else:
    print("Nu ai câștigat. Mai încearcă!")

'''


# Exercitiul 6

'''import random

inventar = []

print("Bine ai venit în pădurea magică!")

while True:
    alegere = input("\nAlegi direcția (stanga/dreapta sau 'stop'): ").lower()

    if alegere == "stop":
        print("Aventura s-a încheiat!")
        print("Inventarul tău:", inventar if inventar else "Gol")
        break

    elif alegere == "stanga":
        eveniment = random.choice(["lup", "comoara"])

        if eveniment == "lup":
            print("\nTe-ai întâlnit cu un lup!")
            if "sabie" in inventar:
                print("Ai o sabie și reușești să alungi lupul!")
            else:
                print("Nu ai nimic să te aperi... fugi speriat!")

        elif eveniment == "comoara":
            print("\nAi găsit o comoară!")
            obiect = random.choice(["sabie", "poțiune", "scut"])
            print(f"În comoară ai găsit: {obiect}")
            inventar.append(obiect)

    elif alegere == "dreapta":
        eveniment = random.choice(["comoara", "vrajitor"])

        if eveniment == "comoara":
            print("\n Ai găsit o comoară!")
            obiect = random.choice(["sabie", "poțiune", "scut"])
            print(f"În comoară ai găsit: {obiect}")
            inventar.append(obiect)

        elif eveniment == "vrajitor":
            print("\n Ai întâlnit un vrăjitor misterios!")
            if "poțiune" in inventar:
                print("Îi dai o poțiune și te răsplătește cu un scut magic!")
                inventar.append("scut")
            else:
                print("Nu ai ce să-i oferi... dispare în ceață.")

    else:
        print("Alegere invalidă!")

    print("\n Inventarul tău:", inventar if inventar else "Gol")'''

# Exercitiul 7

# liste de cuvinte
'''
cuvinte_pozitive = ["bine", "frumos", "super", "excelent", "minunat"]
cuvinte_negative = ["urât", "prost", "groaznic", "dezamăgitor"]

# citirea comentariului
comentariu = input("Introdu comentariul: ").lower()

# variabile pentru detectare
pozitiv = False
negativ = False

# verificare cuvinte pozitive
for cuvant in cuvinte_pozitive:
    if cuvant in comentariu:
        pozitiv = True

# verificare cuvinte negative
for cuvant in cuvinte_negative:
    if cuvant in comentariu:
        negativ = True

# afișare rezultat
if pozitiv and not negativ:
    print("Comentariu pozitiv!")
elif negativ and not pozitiv:
    print("Comentariu negativ!")
elif pozitiv and negativ:
    print("Comentariu mixt!")
else:
    print("Comentariu neutru.")  '''

tari_risc = ["coreea de nord", "siria", "iran"]

nr_tranzactii = 0
tranzactii_suspecte = 0

print("Sistem de monitorizare tranzacții bancare")

while True:
    alegere = input("\nVrei să introduci o tranzacție? (da/nu): ").lower()

    if alegere == "nu":
        print("Program încheiat.")
        break

    if alegere != "da":
        print("Alegere invalidă!")
        continue

    nr_tranzactii += 1

    # introducere date
    suma = float(input("Introdu suma (RON): "))
    tara = input("Introdu țara: ").lower()

    suspicios = False
    fraudulos = False

    # regula 1: suma mare
    if suma > 10000:
        print("⚠️ Tranzacție suspectă: sumă mare!")
        suspicios = True

    # regula 2: țară cu risc
    if tara in tari_risc:
        print("🚨 Tranzacție posibil frauduloasă: țară cu risc ridicat!")
        fraudulos = True

    # regula 3: prea multe tranzacții (simulare simplă)
    if nr_tranzactii > 3:
        print("🤖 Posibilă activitate de tip bot (prea multe tranzacții)!")
        suspicios = True

    # rezultat final
    if fraudulos:
        print("🔴 Tranzacție FRAUDULOASĂ!")
        tranzactii_suspecte += 1
    elif suspicios:
        print("🟠 Tranzacție SUSPECTĂ!")
        tranzactii_suspecte += 1
    else:
        print("🟢 Tranzacție sigură.")

    # verificare blocare utilizator
    if tranzactii_suspecte >= 3:
        print("\n⛔ Utilizator blocat! Prea multe tranzacții suspecte.")
        break

