# Exercitiul 1

"""
Declara o lista note_muzicale in care sa pui do re mi etc pana la do
a. Afiseaz-o
b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
varianta actuala (inversata)
c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
varianta inițială
Concluzii: slicing e temporar, dacă vrei sa pastrezi noua varianta va trebuie sa
suprascrii lista sau sa o salvezi intr-o listă nouă. Metoda gasita de tine face
suprascrierea automat și permanentizeaza aceste modificări. Ambele variante își
găsesc utilitatea în funcție de ce ne dorim in acel moment.
"""

note_muzicale = list(["do", "re", "mi", "fa", "sol", "la", "si", "do"])
#punctul a
print("ex 1 note_muzicale =", note_muzicale)

#puncul b
note_muzicale = note_muzicale[::-1] #suprascriere
print("ex 1 note_muzicale =", note_muzicale)

#punctul c

note_muzicale.reverse() # -> suprascriere automata si inversare
print("ex 1 note_muzicale =", note_muzicale)

#Exercitiul 2

"""
2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
"""

note_muzicale = list(["do", "re", "mi", "fa", "sol", "la", "si", "do"])
DO = note_muzicale.count('do')
print(f" ex 2 Nota DO apare de {DO} ori")

#Exercitiul 3

"""
3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
"""

list_1 = [3, 1, 0, 2]
list_2 = [6, 5, 4]

list_3 = list_1 + list_2
print(f'ex 3 {list_3}')

list_1.extend(list_2)
list_3 = list_1
print(f'ex 3 {list_3}')

#Exercitiul 4

"""
Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
folosind o functie si apoi afiseaza din nou lista.
"""
list_3.sort()
print(f' ex 4 {list_3}')

list_3.sort(reverse=True)
print(f' ex 4 lista sortata descrescator {list_3}')

list_3.remove(0)
print(f' ex 4 {list_3}')


#Exercitiul 5

"""
Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura
urmatoarele:
- Lista este goala (IF)
- Lista nu este goala (ELSE)
"""

if len(list_3) == 0:
    print('ex5 -> Lista este goala')
else:
    print('ex 5 -> Lista nu este goala')

# Exercitiul 6

"""
Foloseste o functie care sa goleasca lista de la exercitiul 3.

"""

list_3.clear()
print(f'ex 6 {list_3}')

# Exercitiul 7

"""
Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
afiseze ca lista e goala.
"""

if len(list_3) == 0:
    print('ex 7 -> Lista este goala')
else:
    print('ex 7 -> Lista nu este goala')

# Exercitiul 8

"""
Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
afisezi Elevii (cheile)

"""

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(f'ex 8 {dict1.keys()}')

# Exercitiul 9

"""
Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
Ex: ‘Ana a luat nota {x}’.
Doar nota o vei lua folosindu-te de cheie.

"""

print(f' ex 9 Ana a luat nota {dict1["Ana"]} ')
print(f' ex 9 Gigel a luat nota {dict1["Gigel"]}')
print(f' ex 9 Dorel a luat nota {dict1["Dorel"]}')

# Exercitiul 10

"""
Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
- Modifica nota lui Dorel in 6
- Printeaza nota lui dupa modificare

"""

dict1["Dorel"] = 6
print(f' ex 10 Dorel a luat nota {dict1["Dorel"]} dupa contestatie')

# Exercitiul 11

"""
Imagineaza-ti ca Gigel se transfera din clasa.
- Cauta o functie care sa il stearga
Vine un coleg nou.
- Adaugati-l in lista pe Ionica, cu nota 9
- Printati dictionarul cu noii elevi
"""

dict1.pop("Gigel")
print (f' ex 11 {dict1}')
dict1.update({"Ionica":"9"})
print(f' ex 11 {dict1}')

# Exercitiul 12

"""
Ai urmatoarele seturi:
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
- Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.
- Afiseaza setul zile_sapt si constata rezultatul adaugarii anterioare.
"""

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add("luni")
print(zile_sapt) # -> nu accepta duplicate

#  Exercitiul 13

"""
Foloseste un if si verifica daca:
- Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
regasesc intre elementele din setul zile_sapt)
- Weekend nu este un subset al zilelor din sapt
Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
punct de mai sus va fi un boolean
"""

if zile_sapt.intersection(weekend) == weekend:
    print('Weekend este subset al zile_sapt')
else:
    print('Weekend nu este subset')

# Exercitiul 14

"""
Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
sunt in weekend si invers)
"""

print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))

# Exercitiul 15

"""
Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
ambele seturi). Hint: Va puteti folosi de o functie.
"""

print(zile_sapt.intersection(weekend))

