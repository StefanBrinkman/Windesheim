class Stap:
    def __init__(self, beschrijving:str, tip=None):
        self.__beschrijving = beschrijving
        self.__tip = tip
    
    def get_beschrijving(self):
        return self.__beschrijving
    
    def set_beschrijving(self, beschrijving):
        self.__beschrijving = beschrijving

    def set_tip(self, tip):
        self.__tip = tip

    def get_tip(self):
        return self.__tip

    def __str__(self):
        return f"Informatie over stap met als beschrijving {self.__beschrijving}"