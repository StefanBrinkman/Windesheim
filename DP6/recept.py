from stap import Stap
from ingredient import Ingredient

class Recept:
    def __init__(self,
                 naam:str,
                 omschrijving: str,
                 aantalPersonen = 1):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen: list[Stap] = []
        self.__aantalPersonen = aantalPersonen

    def get_naam(self):
        return self.__naam
    
    def set_naam(self, naam):
        self.__naam = naam

    def voeg_omschrijving_toe(self, omschrijving):
        self.__omschrijving = omschrijving

    def get_omschrijving(self):
        return self.__omschrijving

    def voeg_ingredient_toe(self, ingredient: Ingredient):
        self.__ingredient_list.append(ingredient)

    def get_ingredienten(self):
        return self.__ingredient_list
    
    def voeg_stap_toe(self, stap: Stap):
        self.__stappen.append(stap)

    def get_stappen(self):
        return self.__stappen

    def set_aantal_personen(self, aantalPersonen):
        self.__aantalPersonen = aantalPersonen

    def get_aantal_personen(self):
        return self.__aantalPersonen

    def __str__(self):
        return f"{self.__naam} geschreven door Stefan Brinkman \n Studentnummer: 1225502 Klas: ICTBC2j"