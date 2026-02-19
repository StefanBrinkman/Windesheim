class Recept:
    def __init__(self, naam, omschrijving, aantalPersonen = 1):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []
        self.__aantalPersonen = aantalPersonen

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)

    def get_ingredienten(self):
        return self.__ingredient_list
    
    def get_naam(self):
        return self.__naam
    
    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def get_stappen(self):
        return self.__stappen

    def set_aantal_personen(self, aantalPersonen):
        self.__aantalPersonen = aantalPersonen

    def get_aantal_personen(self):
        return self.__aantalPersonen

    def get_plantaardig_recept(self, plantaardig):
        print("Plantaardig")

    def __str__(self):
        return f"{self.__naam} geschreven door Stefan Brinkman \n Studentnummer: 1225502 Klas: ICTBC2j"