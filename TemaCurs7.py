# Exercitiul 2

"""
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’

INHERITANCE
Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură

ENCAPSULATION
latura este proprietate privată
Implementează getter, setter, deleter pentru latură
Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)

POLYMORPHISM
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
Creează un obiect de tip Patrat și joacă-te cu metodele lui
Creează un obiect de tip Cerc și joacă-te cu metodele lui

"""

from abc import abstractmethod


class FormaGemoetrica:
    PI = 3.14
    @abstractmethod
    def aria(self):
        raise NotImplementedError

    @classmethod
    def descrie(cls):
        print("Cel mai probabil am colturi")



class Patrat(FormaGemoetrica):

    def __init__(self, latura):
        self.latura = latura

    __latura_private = "private"

    # getter
    def get_latura_private(self):
        return self.__latura_private

    # setter
    def set_latura_private(self, var):
        self.__latura_private = var

    # deleter
    def delete_latura_private(self):
        self.__latura_private = None

    def aria(self):
        return self.latura * self.latura

class Cerc(FormaGemoetrica):
    def __init__(self, raza):
        self.raza = raza

    __raza_private = "private"

    # getter
    def get_raza_private(self):
        return self.__raza_private

    # setter
    def set_raza_private(self, var):
        self.__raza_private = var

    # deleter
    def delete_raza_private(self):
        self.__raza_private = None

    def aria(self):
        return self.PI * self.raza ** 2

    def descrie(self):
        print("Eu nu am colturi")

cerc = Cerc(24)
patrat = Patrat(67)
print (cerc.aria())
cerc.descrie()
print(patrat.aria())
patrat.descrie()







