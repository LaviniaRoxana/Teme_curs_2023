# Exercitiul 1

# If else este folosit atunci cand doresti codul sa se execute in anumite conditii; se bifurca codul in functie de rezultat.


# Exercitiul 2
"""Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
daca este numar intreg mai mare ca 0)"""

x = input('introduceti numarul')
if (x.isdigit() and int(x) > 0):
    print('numarul este natural')
else:
    print('numarul nu este natural')

#  Exercitiul 3

"""
Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru.
"""
numar = float(input("introduceti un numar "))
if numar > 0:
   print("numarul este pozitiv")
elif numar == 0:
   print("numarul este neutru")
else:
   print("numarul este negativ")

# Exercitiul 4

"""
Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
"""
x = int(input('introduceti numar'))
if (int (x) >=-2 and int (x) <=13):
    print ('numarul este in interval')
else:
    print('numarul nu este in interval')

#Exercitiul 5

"""
Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5 (diferenta inseamna
cate numere sunt intre x si y, nu rezultatul diferentei intre x si y). Hint: Se va folosi functia
abs
"""
x = int(input('introduceti numar'))
y = int(input('introduceti al doilea numar'))
if abs(x-y) < 5:
    print ('diferenta este mai mica decat 5')
else:
    print ('diferenta nu este mai mica')

# Exercitiul 6

"""
Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
"""

x = int(input('introduceti numar'))
if not(int(x)>=5 and int(x)<=27):
    print('x nu este in interval')
else:
    print('x este in interval')

# Exercitiul 7

"""
# Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
# daca nu, afiseaza care din ele este mai mare
# """

x = 27
y = 15
if x == y:
    print('x si y sunt egale')
elif x > y:
    print ('x este mai mare')
elif y > x:
    print ('y mai mare ca x')

# Exercitiul 8

"""
Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi, afiseaza daca
triunghiul este isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau
oarecare (nicio latura nu e egala).
 """

x = int(input('introduceti primul numar'))
y = int(input('introduceti al doilea numar'))
z = int(input('introduceti al treilea numar'))

if x == y == z:
    print ('triunghiul este echilateral')
elif x == y or y == z or z == x:
    print ('triunghiul este isoscel')
else:
    print ('triunghiul este oarecare')

# Exercitiul 9

"""
Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie!
Trebuie sa evaluati si cazurile uppercase si cazurile lowercase.

"""

litera = input('introduceti o litera')
if litera in ('a', 'e', 'i','o','u'):
    print ('litera este vocala')
elif litera in ('A', 'E','I','O','U'):
    print ('litera este VOCALA')
else:
    print ('litera este consoana')

# Exercitiul 10

"""
Transforma si printeaza notele din sistem românesc in sistem american dupa cum
urmeaza:
a. Peste 9 => A
b. Peste 8 => B
c. Peste 7 => C
d. Peste 6 => D
e. Peste 4 => E
f. 4 sau sub => F

"""
nota = float(input('introduceti nota'))
if nota > 9:
    print('A')
elif nota > 8:
    print('B')
elif nota > 7:
    print('C')
elif nota > 6:
    print('D')
elif nota > 4:
    print('E')
elif nota <= 4:
    print('F')