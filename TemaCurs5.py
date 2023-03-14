# Exercitiul 1

"""
1.Funcție care să calculeze și să returneze suma a două numere.
"""


# def suma_numerelor(a, b):
#     return a + b
#
# a = int(input("Introduceti primul numar: "))
# b = int(input("Introduceti al doilea numar: "))
# suma = suma_numerelor(a,b)
# print(f'Suma numerelor este {suma}')


# Exercitiul 2

"""
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
"""

# def numere_pare_si_numere_impare(numar):
#         if numar % 2 == 0:
#             return ('TRUE')
#         else:
#             return ('FALSE')
#
# numar = int(input('Introduceti numar'))
# print(f'Numarul este par? {numere_pare_si_numere_impare(numar)}')

# Exercitiul 3

"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""

# def numar_total_caractere_nume(nume, prenume, nume_mijlociu):
#     print(f'Numarul de caractere este {len(nume + prenume + nume_mijlociu)}')
#
# nume = (input("Introduceti nume"))
# prenume= (input('Inroduceti prenumele'))
# nume_mijlociu = (input('Introduceti nume_mijlociu'))
# numar_total_caractere_nume(nume,prenume,nume_mijlociu)

# Exercitiul 4

"""
4. Funcție care returnează aria dreptunghiului
"""

# def aria_dreptunghiului(lungime, latime):
#     return lungime * latime
#
# lungime = int(input("Introduceti lungimea"))
# latime = int(input('Introduceti latimea'))
# rezultat = aria_dreptunghiului(lungime,latime)
# print(f'Aria dreptunghiului este {rezultat}')

# Exercitiul 5

"""
Funcție care returnează aria cercului.
"""

# def aria_cercului(raza):
#     return 3.14 * raza ** 2
#
# raza = int(input('Introduceti raza'))
# rezultat = aria_cercului(raza)
# print(f'Aria cercului este {rezultat}')

# Exercitiul 6

"""
Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.
"""

# def cautare_caracter (litera, text_introdus):
#     if str(text_introdus).find(litera) != -1:
#         return'TRUE'
#     else:
#         return 'FALSE'
#
# text_introdus = input('Introduceti text')
# litera = input('Introduceti caracter')
# rezultat = cautare_caracter(litera,text_introdus)
# print(f'Se gaseste caracterul {litera} in {text_introdus}?: {rezultat}')


# Exercitiul 7

"""
Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
"""

# def context(text):
#     cate_litere_mici = 0
#     cate_litere_mari = 0
#     for litera in text:
#          if litera.isupper():
#               cate_litere_mari += 1 #daca litera este mare, incrementam la litere mari
#          elif litera.islower():
#               cate_litere_mici += 1 #daca litera este mica, incrementam la ltere mici
#
#     print(f'Textul a fost{text}')
#     print(f"Numarul de litere mici este {cate_litere_mici}")
#     print(f"Numarul de litere mari esti {cate_litere_mari}")
#
# textul_ales = input('Introduceti un text')
# context(textul_ales)


# Exercitiul 8
"""
Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
"""

def retrage_nr_pozitive(lista_numere):
    numere_pozitive = []
    for numar in lista_numere:
        if numar > 0:
            numere_pozitive.append(numar)
    return numere_pozitive

lista_numere = [-1, 8, 9, -10, 5, -4, 20]
rezultat = retrage_nr_pozitive(lista_numere)
print(f"Lista cu nr pozitive este {rezultat}")

# Exercitiul 9

"""
Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale
"""

# def primeste_doua_numere(x,y):
#
#      if x > y:
#          print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
#      elif y > x:
#          print(f"Al doilea numar {y} este mai mare decat primul numar {x}")
#      elif x == y:
#          print('Numerele sunt egale')
#
# x = int(input('Introduceti primul nr'))
# y = int(input('Introduceti al dolea nr'))
# primeste_doua_numere(x,y)

# Exercitiul 10

"""
Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
"""

def numar_si_set_de_numere(numar, set_de_numere):
    numarul_exista_in_set = False #pornim de la premiza ca nr nu exista in set
    for element in set_de_numere: #verificam fiecare nr din sir daca este = cu nr nostru
        if element == numar:
         numarul_exista_in_set = True #daca l-am gasit, setam variabila TRUE (exista in set)

    if numarul_exista_in_set == False: #daca nr nu exista in set, il adaugam
        set_de_numere.append(numar)
        print(f'Am adaugat numarul nou {numar} in set')
        return True
    elif numarul_exista_in_set == True:
        print('Nu am adaugat nr in set.Acesta exista deja.')
        return False

set_de_numere = [-9, -2, 10, 90, 1203, 56, 78, 34, 56]
numar = int(input('introduceti un nr'))
numar_si_set_de_numere(numar,set_de_numere)
print(set_de_numere)








