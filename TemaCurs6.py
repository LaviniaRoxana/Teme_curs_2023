#Exercitiul 1

"""
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
"""

class Cerc:
    raza = None
    culoare = None
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
    def descriere_cerc(self):
        print(f'Cercul meu are culoarea {self.culoare} si raza {self.raza}')
    def aria(self):
        return 3.14 * self.raza ** 2
    def diametru(self):
        return 2 * self.raza
    def circumferinta(self):
        return 2 * 3.14 * self.raza

cerc = Cerc(89, 'albastru')
cerc.descriere_cerc()
print(cerc.aria())
print(cerc.diametru())
print(cerc.circumferinta())

# Exercitiul 2

"""
Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul

self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
"""

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self. culoare = culoare
    def descriere_dreptunghi(self):
        print(f'Dreptunghiul meu are lungime {self.lungime}, latime {self.latime} si culoare {self.culoare}')
    def aria(self):
        return self.lungime * self.latime
    def perimetrul(self):
        return 2 * self.lungime + 2 * self.latime
    def schimba_culoare (self, culoare_noua):
        self.culoare = culoare_noua

dreptunghi = Dreptunghi(45, 56, 'rosu')
dreptunghi.descriere_dreptunghi()
print(dreptunghi.aria())
print(dreptunghi.perimetrul())
dreptunghi.schimba_culoare('verde')
dreptunghi.descriere_dreptunghi()

# Exercitiul 3

"""
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""

class Angajat:
    nume = None
    prenume = None
    salariu = None
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    def desciere_angajat(self):
        print(f'Angajatul are nume {self.nume}, prenume {self.prenume} si salariu {self.salariu}')
    def nume_complet(self):
        return self.nume + " " + self.prenume
    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return self.salariu_lunar() * 12
    def marire_salariu(self, procent_marire):
        self.salariu = self.salariu + procent_marire * self.salariu / 100

angajat_Lavinia = Angajat('Pop', 'Lavinia', 4000)
angajat_Lavinia.desciere_angajat()
print(angajat_Lavinia.nume_complet())
print(angajat_Lavinia.salariu_lunar())
print(angajat_Lavinia.salariu_anual())
angajat_Lavinia.marire_salariu(12)
angajat_Lavinia.desciere_angajat()


angajat_Garofita = Angajat('Pop', 'Garofita', 3600)
angajat_Garofita.desciere_angajat()
print(angajat_Garofita.nume_complet())
print(angajat_Garofita.salariu_lunar())
print(angajat_Garofita.salariu_anual())
angajat_Garofita.marire_salariu(20)
angajat_Garofita.desciere_angajat()

angajat_Ovidiu = Angajat('Ciucas', 'Ovidiu', 13000)
angajat_Ovidiu.desciere_angajat()
print(angajat_Ovidiu.nume_complet())
print(angajat_Ovidiu.salariu_lunar())
print(angajat_Ovidiu.salariu_anual())
angajat_Ovidiu.marire_salariu(30)
angajat_Ovidiu.desciere_angajat()

# Exercitiul 4

"""
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
"""

class Cont:
    iban = None
    titular_cont = None
    sold = None
    def __init__(self, iban, titular_cont,sold ):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')
    def debitare_cont(self, suma):
        self.sold = self.sold - suma
    def creditare_cont (self, suma):
        self.sold = self.sold + suma

cont = Cont (23456789, 'Lavinia Pop', 5000)
cont.afisare_sold()
print(cont.debitare_cont(456))
cont.afisare_sold()
print(cont.creditare_cont(367.8))
cont.afisare_sold()