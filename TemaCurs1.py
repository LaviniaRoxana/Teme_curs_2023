#exercitiul 1

# o variabila este un spatiu din memorie, o cutiuta, unde se stocheaza valori.

#exercitiul 2

floare = 'trandafir'
varsta = 26
total_costmasina= 24000.5
Lavinia_are_26_ani = True

#exercitiul 3

print(type(floare))
print(type(varsta))
print(type(total_costmasina))
print(type(Lavinia_are_26_ani))

#exercitiul4
total_costmasina = round(total_costmasina)
print(round(total_costmasina))
#suprascriere
total_costmasina = round(total_costmasina)
print (type(total_costmasina))

#exercitiul 5

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

nume = str(input('introduceti numele'))
prenume = str(input('introduceti prenume'))
nume_complet = f'{nume} {prenume}'
lungime_nume_complet  = (len(nume_complet))
print (f'Numele complet {nume_complet} are {lungime_nume_complet} caractere')

#exercitiul 7

lungime = float(input('introduceti lungimea'))
latime = float(input('introduceti latimea'))
aria = lungime * latime
print(aria)


#exercitiul 8 si 9

string_tema = "Coral is either the stupidest animal or the smartest rock"
print(string_tema.count("the"))

#exercitiul 10

string_tema = "Coral is either the stupidest animal or the smartest rock"

assert string_tema.isnumeric(), 'textul nu este numeric' # -> AssertionError







