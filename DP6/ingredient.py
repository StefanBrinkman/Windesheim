class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid, kcal, plantaardig_alternatief=None):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__plantaardig_alternatief = plantaardig_alternatief
        self.__kcal = kcal

    def get_naam(self):
        return self.__naam

    def set_hoeveelheid(self, personen):
        hoeveelheid = self.__hoeveelheid * personen
        self.__hoeveelheid = hoeveelheid

    def get_hoeveelheid(self):
        return self.__hoeveelheid

    def get_kcal(self):
        return self.__kcal
    
    def set_plantaardig_alternatief(self, plantaardig_alternatief):
        self.__plantaardig_alternatief = plantaardig_alternatief

    def get_ingredient(self, wilt_alternatief):
        return self.__plantaardig_alternatief

    def __str__(self):
        return f"Geschreven door Stefan Brinkman \n Studentnummer: 1225502 Klas: ICTBC2j over {self.__naam}"