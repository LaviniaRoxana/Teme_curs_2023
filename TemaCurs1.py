#exercitiul 1

"""
În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
"""

# o variabila este un spatiu din memorie, o cutiuta, unde se stocheaza valori.

#exercitiul 2

"""
Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :

- string
- int
- float
- bool

Observație: Valorile vor fi alese de tine după preferințe.
"""

floare = 'trandafir'
varsta = 26
total_costmasina= 24000.5
Lavinia_are_26_ani = True

#exercitiul 3

"""
Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
"""

print(type(floare))
print(type(varsta))
print(type(total_costmasina))
print(type(Lavinia_are_26_ani))

#exercitiul4

"""
Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
"""

total_costmasina = round(total_costmasina)
print(round(total_costmasina))
#suprascriere
total_costmasina = round(total_costmasina)
print (type(total_costmasina))

#exercitiul 5

"""
Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.

Rezolvă nepotrivirile de tip prin ce modalitate dorești.
"""

propozitia_1 = "Am cumparat un"
floare = "trandafir"
print (f'{propozitia_1} {floare}')

nume = 'Lavi'
varsta = 26
print(f'Ma numesc {nume} si am varsta de {varsta} de ani')

propozitia_2 = "Maria are o masina in valore de"
total_costmasina = 24000.5
print (f'{propozitia_2} {total_costmasina} lei')

a = 26
b = 22
if a >=b:
    print("Lavinia are 26 ani")
else:
    print("Lavinia nu are 26 de ani")


# #exercitiul 6

"""
Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
"""

nume = str(input('introduceti numele'))
prenume = str(input('introduceti prenume'))
nume_complet = f'{nume} {prenume}'
lungime_nume_complet  = (len(nume_complet))
print (f'Numele complet {nume_complet} are {lungime_nume_complet} caractere')

#exercitiul 7

"""
Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
"""

lungime = float(input('introduceti lungimea'))
latime = float(input('introduceti latimea'))
aria = lungime * latime
print(aria)


#exercitiul 8 si 9

"""
Având stringul: 'Coral is either the stupidest animal or the smartest rock':

- afișează de câte ori apare cuvântul 'the';

Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.
"""

string_tema = "Coral is either the stupidest animal or the smartest rock"
print(string_tema.count("the"))

#exercitiul 10

"""
Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.
"""

string_tema = "Coral is either the stupidest animal or the smartest rock"

assert string_tema.isnumeric(), 'textul nu este numeric' # -> AssertionError







