# Exercitiul 1

"""
1.Având lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun',
'Fiat', 'Trabant', 'Opel']

# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')
#
# for masina in masini:
#     print(f' Masina mea preferata este {masina}')
#
# i = 0
# while i < len(masini):
#     print(f'Masina mea preferata este {masini[i]}')
#     i += 1
#
# # inversarea listei
# i = len(masini) -1
# while i >= 0:
#     print(f'Masina mea preferata este {masini[i]}')
#     i -= 1


# Exercitiul 2

"""
2. Aceeași listă:
Folosește un for else
În for

- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
"""

for i in range(1, len(masini)-1):
    masini[i] = masini[i].upper()
else:
    print(masini)

# Exercitiul 3

"""
Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘
"""
for masina in masini:
    if masina.lower() == 'mercedes':
        print(f' Am gasit masina dorita de dvs')
        break
    print(f'Am gasit masina {masina}. Mai cautam.')

# Exercitiul 4

"""
Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.
"""

for masina in masini:
    if masina.lower() =='Trabant'.lower() or masina.lower() == 'Lastun'.lower():
        continue
    print(f'S-ar putea sa placa masina {masina}')

# Exercitiul 5

"""
Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

● Printează Modele vechi: x.
● Modele noi: x.
"""

masini_vechi = []
for i in range(len(masini)):
    if masini[i].lower() == 'Lastun'.lower() or masini[i].lower() == 'Trabant'.lower():
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print (f'Modele vechi: {masini_vechi}')
print(f'Modele noi: {masini}')

# Exercitiul 6
"""
Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
"""

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
for key_masina in pret_masini.keys():
    if pret_masini.get(key_masina) <= 15000:
        print(f'Pentru un buget de 15000 de euro puteti alege masina {key_masina}')

for pret_masina in pret_masini.items():
    if pret_masina[1]<= 15000:
        print(f'Pentru un buget de 15000 de euro puteti alege masina {pret_masina}')

# Exercitiul 7

"""
Având lista:
numere =  [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
numere =[5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

de_cate_ori_apare_trei = 0
for numar in numere:
    if numar == 3:
        de_cate_ori_apare_trei +=1

print(f'3 apare de {de_cate_ori_apare_trei} ori')

print(numere.count(3))

# Exercitiul 8

"""
Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
suma = 0
for numar in numere:
    suma += numar
print (f'Suma numerelor este {suma}')

print(sum(numere))

# Exercitiul 9

"""
Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
"""

cel_mai_mare_nr = numere[0]   #tinem in variabila primul nr din lista
for numar in numere:    #parcurgem cu for each lista
    if numar > cel_mai_mare_nr:  #daca gasi un nr mai mare decat cel initial, supascriemvariabila cu nr mai mare gasit
        cel_mai_mare_nr = numar  #nr maxim
print(f'Cel mai mare nre din lista este {cel_mai_mare_nr}')

print(max(numere))

# Exercitiul 10

"""
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
● Afișază noua listă.
"""

for i in range(len(numere)):
    numere[i] = -numere[i]
print(numere)

for i in range(len(numere)):
    if numere[i] > 0:
        numere[i] = numere[i] * -1
print(numere)