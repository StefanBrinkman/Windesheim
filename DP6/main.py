from recept import Recept 
from ingredient import Ingredient
from stap import Stap

recepten = []

def voerNieuwReceptIn():
    print("VOER NIEUW RECEPT IN: ")
    keuzeMenuOpties()

def toonReceptenOverzicht():
    print("TOON OVERZICHT RECEPTEN")
    counter = 1
    for recpt in recepten:
        print(f"Receptnummer {counter}", recpt.get_naam())
        counter += 1

    gekozenGerecht = int(input("Kies een gerecht: ")) - 1
    while gekozenGerecht  > len(recepten):
        print("Recept niet gevonden")
        gekozenGerecht = int(input("Kies een gerecht: "))
    
    aantalPersonen = input("Voor hoeveel personen is het recept? ")
    while aantalPersonen.isdigit() == False:
        print("Foutieve invoer")
        aantalPersonen = input("Voor hoeveel personen is het recept? ")

    wiltPlantaardigAlternatief = input("Wilt u een plantaardig alternatief voor dit recept? (ja/nee): ")
    while (wiltPlantaardigAlternatief != "ja" and wiltPlantaardigAlternatief != "nee"):
        print("Foutive invoer")
        wiltPlantaardigAlternatief = input("Wilt u een plantaardig alternatief voor dit recept? (ja/nee): ")
    

    # Gekozen Recept
    recepten[gekozenGerecht].set_aantal_personen(aantalPersonen)
    totaalCal = 0

    for ingredient in recepten[gekozenGerecht].get_ingredienten():
        ingredient.set_hoeveelheid(aantalPersonen)
        gekozenIngredient = ingredient.get_ingredient(wiltPlantaardigAlternatief)
        totaalCal += gekozenIngredient.get_kcal() * int(aantalPersonen)
        print(f"* {gekozenIngredient.get_naam()}")

    print(f"Totaal {totaalCal} calorieën")

    stapCounter = 1
    for stap in recepten[gekozenGerecht].get_stappen():
        print(f"Stap {stapCounter}: {stap.get_beschrijving()}")
        stapCounter += 1

    keuzeMenuOpties()


def keuzeMenuOpties():
    keuzeNummer = 1
    keuzeMenu = ["Recept toevoegen", "Overzicht tonen", "Exit"]
    for keuze in keuzeMenu:
        print(keuzeNummer, keuze)
        keuzeNummer += 1

    keuze = int(input("Kies een keuze uit het menu? "))

    while keuze  > len(keuzeMenu):
        print("Keuze niet gevonden")
        keuze = int(input("Kies een keuze uit het menu? "))

    if keuze == 1:
        voerNieuwReceptIn()
    elif keuze == 2:
        toonReceptenOverzicht()
    else:
        print("Einde programma")
    
def main():
    recept1 = Recept("Kip Kerrie", "Kip kerrie zonder pakjes en zakjes")
    recept2 = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt en paprika.")
    recept3 = Recept("Babi panpang", "Rijst met atjar tjampoer")

    recept1.voeg_ingredient_toe(Ingredient("kip", 500, "gram", 500, Ingredient("Tempeh", 500, "Gram", 768)))
    recept1.voeg_ingredient_toe(Ingredient("sperziebonen", 400, "gram", 96))
    recept1.voeg_stap_toe(Stap("Kook de rijst en zet een pan water met een snuf zout op het vuur voor de sperziebonen."))
    recept1.voeg_stap_toe(Stap("Snijd de kip in kleine blokjes, snipper het uitje, snijd de knoflook fijn en snijd de kontjes van de sperziebonen (was ze ook even)."))

    recept2.voeg_ingredient_toe(Ingredient("paprika", 250, "gram", 62))
    recept2.voeg_ingredient_toe(Ingredient("gehakt", 300, "gram", 675, Ingredient("Erwteneiwit gehakt", 300,"gram", 660)))
    recept2.voeg_stap_toe(Stap("Bak het gehakt samen met de paprika in een pan."))
    recept2.voeg_stap_toe(Stap("Breng het al mengent op temperatuur en voeg zo nodig kruiden toe.", 5))

    recept3.voeg_ingredient_toe(Ingredient("Rijst", 300, "gram", 206))
    recept3.voeg_ingredient_toe(Ingredient("Hamlappen", 400, "gram",  239, Ingredient("Seitan", 400, "gram", 1480)))
    recept3.voeg_ingredient_toe(Ingredient("Tomatenpuree", 140, "gram", 159))
    recept3.voeg_stap_toe(Stap("Kook de rijst zoals de instructies aangeven"))
    recept3.voeg_stap_toe(Stap("Bak het vlees in een pan voor 30 minuten", 10))
    recept3.voeg_stap_toe(Stap("Meng de rijst met het vlees en gebruik waar nodig de tomatenpuree"))

    recepten.append(recept1)
    recepten.append(recept2)
    recepten.append(recept3)

    keuzeMenuOpties()

if __name__ == "__main__":
    main()
