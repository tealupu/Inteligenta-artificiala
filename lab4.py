'''def suma(x):
    return sum(x)


print(suma([5, 10, 3]))


def my_fun(arg1, *argv):
    print("First Argument: ", arg1)
    for arg in argv:
        print("Next Argument through *argv :", arg)


my_fun('Hello', 'Welcome', 'to', 'python')


def my_func(**kwargs):
    for key, value in kwargs.items():
        print("%s==%s" % (key, value))


my_func(first='B', mid='to', last='C')

#Fibonacci

fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)
result = fib(10)
print(result)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
'''
#Ex 1
'''def piatra_foarfeca_hartie(j1, j2):
    if j1 == j2:
        return "Egalitate!"

    if (j1 == "piatra" and j2 == "foarfeca") or \
            (j1 == "foarfeca" and j2 == "hartie") or \
            (j1 == "hartie" and j2 == "piatra"):
        return "Jucatorul 1 castiga!"
    else:
        return "Jucatorul 2 castiga!"


def joc():
    while True:
        print("\n--- Joc Piatra-Hartie-Foarfeca ---")

        j1 = input("Jucatorul 1 (piatra/hartie/foarfeca): ").lower()
        j2 = input("Jucatorul 2 (piatra/hartie/foarfeca): ").lower()

        if j1 not in ["piatra", "hartie", "foarfeca"] or j2 not in ["piatra", "hartie", "foarfeca"]:
            print("Input invalid! Incearca din nou.")
            continue

        rezultat = piatra_foarfeca_hartie(j1, j2)
        print(rezultat)

        din_nou = input("Doriti sa jucati din nou? (da/nu): ").lower()
        if din_nou != "da":
            print("Multumim pentru joc!")
            break


# Pornire joc
joc()'''
#ex2

'''def genereaza_factura(nume_client, **produse):
    print("------ FACTURA ------")
    print(f"Client: {nume_client}\n")

    total = 0

    for produs, pret in produse.items():
        print(f"{produs}: {pret} lei")
        total += pret

    print("\n---------------------")
    print(f"TOTAL: {total} lei")
    print("---------------------")


# Exemplu
genereaza_factura(
    "Ana Popescu",
    paine=5,
    lapte=7,
    oua=12,
    mere=10
)'''
#ex 4
'''patrate = lambda lista: [x**2 for x in lista]
my_list = [2,14,9]
rezultat = patrate(my_list)

print(rezultat) '''

#ex 5
'''
a = [(0, 10), (4, -4), (9, 5), (10, -1)]

sorted_a = sorted(a, key=lambda x: x[1])

print(sorted_a)'''

# ex3
import random

def normalize_data(data):
    min_val = min(data)
    max_val = max(data)

    if max_val == min_val:
        return [0 for _ in data]

    return [(x - min_val) / (max_val - min_val) for x in data]


# test
data = [random.randint(1, 100) for _ in range(5)]
print("Date initiale:", data)

normalized_data = normalize_data(data)
print("Date normalizate:", normalized_data)

#ex 6
orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15]

even_list = list(filter(lambda x: x % 2 == 0, orig_list))

odd_list = list(filter(lambda x: x % 2 != 0, orig_list))

print("Lista initiala:", orig_list)
print("Numere pare:", even_list)
print("Numere impare:", odd_list)

#ex 7
prices = [100, 200, None, 50, None, 80]


valid_prices = list(filter(lambda x: x is not None, prices))

discounted_prices = list(map(lambda x: x * 0.9, valid_prices))

print("Preturi initiale:", prices)
print("Preturi valide:", valid_prices)
print("Preturi cu reducere:", discounted_prices)

#ex 8
data = "2023-04-24 09:03:32.744178"


get_year = lambda x: x.split(" ")[0].split("-")[0]
get_month = lambda x: x.split(" ")[0].split("-")[1]
get_day = lambda x: x.split(" ")[0].split("-")[2]
get_time = lambda x: x.split(" ")[1]


print(get_year(data))   # 2023
print(get_month(data))  # 04
print(get_day(data))    # 24
print(get_time(data))   # 09:03:32.744178

#ex 9
def sum_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]


list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

result = sum_lists(list1, list2)
print(result)

#ex 10
#nr pare
even_numbers = [x for x in range(0, 101) if x % 2 == 0]
print(even_numbers)

# cuburile primelor 10
cubes = [x**3 for x in range(1, 11)]
print(cubes)

#elemente comune
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = [x for x in list1 if x in list2]
print(common)

#ex 11
#primele 10 nr pare
even_set = {x for x in range(0, 20) if x % 2 == 0}
print(even_set)

#litere distincte
text = "programare python"

letters = {char for char in text if char != " "}
print(letters)

#cuv 5 litere
text = "Python este un limbaj de programare foarte popular"

words = {word for word in text.split() if len(word) >= 5}
print(words)

#ex 12
#chei si valori
squares = {x: x**2 for x in range(1, 11)}
print(squares)

#litere aparitii
text = "programare python"

freq = {char: text.count(char) for char in text if char != " "}
print(freq)

#numere divizori
divisors = {x: [d for d in range(1, x + 1) if x % d == 0] for x in range(1, 11)}
print(divisors)