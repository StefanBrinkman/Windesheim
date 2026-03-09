from recept import Recept 
from ingredient import Ingredient
from stap import Stap
from reportlab.pdfgen import canvas
from reportlab.lib import colors

recepten = []

def vraagPDFBestand(gerechtNummer: int):
    pdfPrinten = str(input("Wilt u een PDF van het recept? (ja/nee) "))
    if pdfPrinten == 'ja' or pdfPrinten == 'nee':
        if pdfPrinten == 'ja' :
            maakPDFBestand(gerechtNummer)
        else:
            vraagVerwijderenRecept(gerechtNummer)
    else:
        print("Foutieve input")

def maakPDFBestand(receptInPDF: int):
    recept = recepten[receptInPDF - 1]
    pdfBestandsNaam = 'recept.pdf'
    pdfTitel = 'Recept'
    titel = 'Recept informatie'
    subTitel = 'Informatie over recept'

    receptInformatie = [
        f"Naam: {recept.get_naam()}",
        f"Omschrijving: {recept.get_omschrijving()}",
        f"Aantal personen: {recept.get_aantal_personen()}"]
    stappenLijst = recept.get_stappen()
    ingredientenLijst = recept.get_ingredienten()

    pdf = canvas.Canvas(pdfBestandsNaam)
    pdf.setTitle(pdfTitel)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawCentredString(300, 770, titel)
    pdf.setFillColorRGB(0,0,255)
    pdf.setFont("Courier-Bold", 10)
    pdf.drawCentredString(300, 870, subTitel)

    text = pdf.beginText(40, 680)
    for receptInfo in receptInformatie:
        text.textLines(receptInfo)
    
    text.textLines("")
    text.textLines("Ingredienten: ")
    for ingredientInfo in ingredientenLijst:
        text.textLines(f"* {ingredientInfo.get_hoeveelheid()} gram  {ingredientInfo.get_naam()}.")

    text.textLines("")
    text.textLines("STAPPEN: ")
    stapNummer = 1
    for stapInfo in stappenLijst:
        text.textLines(f"{stapNummer} {stapInfo.get_beschrijving()}")
        stapNummer += 1
    
    pdf.drawText(text)
    try:
        pdf.save()
        print("PDF is aangemaakt")
    except:
        print("Er is iets fout gegaan met het maken van de PDF")
    vraagVerwijderenRecept(receptInPDF)

def voegIngredientToe(recept): 
    print("Voeg ingredienten toe aan recept:")
    nieuweIngredient = True

    while nieuweIngredient:
        try:
            ingredient = str(input("Voer naam ingredient in:  "))
            hoeveelheid = int(input(f"Hoeveel gram {ingredient} moet toegevoegd worden? "))
            kcal = int(input(f"Hoeveel kcal is het ingredient? "))
            if ingredient and hoeveelheid > 0 and kcal > 0:
                plantaardig = str(input("Plantaardig alternatief toevoegen? (ja/nee) "))
                if plantaardig == 'ja':
                    try:
                        alternatiefIngredient = str(input("Voer naam alternatief ingredient in:  "))
                        alternatiefHoeveelheid = int(input(f"Hoeveel gram {alternatiefIngredient} moet toegevoegd worden? "))
                        alternatiefKcal = int(input(f"Hoeveel kcal is het ingredient? "))
                        recept.voeg_ingredient_toe(Ingredient(ingredient, hoeveelheid, "gram",  kcal, Ingredient(alternatiefIngredient, alternatiefHoeveelheid, "gram", alternatiefKcal)))
                    except ValueError:
                        print("Tijdens het invoeren van gegevens is ergens verkeerd gegaan.")
                else:
                    recept.voeg_ingredient_toe(Ingredient(ingredient, hoeveelheid, "gram", kcal))
            else:
                print("Ingredient, hoeveelheid of kcal is verkeerd ingevuld")

            volgendeIngredient = str(input("Wilt u een nieuwe ingredient toevoegen?  (ja/nee) "))
            if volgendeIngredient == 'nee':
                nieuweIngredient = False
                break
        except ValueError:
            print("Tijdens het invoeren van gegevens is ergens verkeerd gegaan.")

def voegStapOp(recept: Recept):
    print("Voeg stap(en) toe")
    nieuweStap = True

    while nieuweStap:
        try:
            stap = str(input("Voeg volgende stap toe: "))
            if not stap:
                print("Voer een stap in")
                stap = str(input("Voeg volgende stap toe: "))
            else:
                pass   
        except:
            print("Moet text bevatten")

        try:
            tip = str(input("Heeft u nog tips? (ja/nee) "))
            if tip == 'ja' or tip == 'nee':
                if tip == 'ja' :
                    stapTip = str(input("Voer hier uw tip in! "))
                else:
                    stapTip = None
                recept.voeg_stap_toe(Stap(stap, stapTip))
        except ValueError:
            print("Voer ja of nee in.")
    
        try:
            volgendeStap = str(input("Wilt u een nieuwe stap toevoegen?  (ja/nee) "))
            if volgendeStap == 'nee':
                nieuweStap = False
                break
        except ValueError:
            print("Voer ja of nee in.")
    
def voegReceptToe(nieuwRecept: Recept):
    try:
        recepten.append(nieuwRecept)
    except:
        print("Toevoegen recept is mislukt!")

    nieuwReceptIndex = recepten.index(nieuwRecept)
    print(f"Naam: {nieuwRecept.get_naam()}")
    print(f"Omschrijving: {nieuwRecept.get_omschrijving()}")

    ingredientenLijst = nieuwRecept.get_ingredienten()
    for ingredient in ingredientenLijst:
        print(f"* {ingredient.get_hoeveelheid()} gram {ingredient.get_naam()}.")

    toonStappenRecept(nieuwReceptIndex)
    print("____________")

def voerNieuwReceptIn():
    print("VOER NIEUW RECEPT IN: ")
    nieuwRecept = True
    while nieuwRecept:
        try:
            nieuwReceptNaam = str(input("Voer naam recept in: "))
            nieuwReceptOmschrijving = str(input("Voer omschrijving recept in: "))
            if nieuwReceptNaam and nieuwReceptOmschrijving:
                nieuwRecept = Recept(nieuwReceptNaam, nieuwReceptOmschrijving)
                
                voegIngredientToe(nieuwRecept)
                voegStapOp(nieuwRecept)
                voegReceptToe(nieuwRecept)
                nieuwRecept = False
                keuzeMenuOpties()
            else:
                print("Naam en omschrijving mogen niet leeg zijn!")
        except ValueError:
            print("Foutive invoer")

def vraagAantalPersonenOp():
    while True:
        try:
            aantalPersonen = int(input("Voor hoeveel personen is het recept? "))
            return aantalPersonen
        except ValueError:
            print("Foutieve invoer")

def vraagVerwijderenRecept(receptNummer: int):
    while True:
        try:
            verwijderRecept = str(input("Wilt u het recept verwijderen? (ja/nee) "))
        except:
            print("Foutive invoer")
    
        if verwijderRecept == 'ja' :
            verwijderenRecept(receptNummer - 1)
            break
        elif verwijderRecept == 'nee':
            keuzeMenuOpties()
            break
        else:
            print("Foutive invoer")

def verwijderenRecept(receptNummer: int):
    print("Verwijderen recept")
    recepten.pop(receptNummer)
    print("Recept is verwijderd")
    keuzeMenuOpties()

def vraagGekozenGerechtOp():
    gerecht = 0
    counter = 1

    for recpt in recepten:
        print(f"Receptnummer {counter}", recpt.get_naam())
        counter += 1

    while gerecht < 1 or gerecht > len(recepten):
        try:
            gerecht = int(input("Kies een recept: "))
        except:
            print("Foutieve invoer")
    
        if gerecht >= 1 and (gerecht - 1) < len(recepten):
            return gerecht
        else:
            print("Kies een geldig recept")

def vraagPlantaardigAlternatiefOp():
    while True:
        try:
            wiltPlantaardigAlternatief = input("Wilt u een plantaardig alternatief voor dit recept? (ja/nee): ")
            if wiltPlantaardigAlternatief != 'ja' and wiltPlantaardigAlternatief != 'nee':
                print("Foutive invoer")
            else:
                return wiltPlantaardigAlternatief
        except ValueError:
            print("Foutieve invoer")

def toonStappenRecept(recept: int):
    stapCounter = 1
    for stap in recepten[recept].get_stappen():
        print(f"Stap {stapCounter}: {stap.get_beschrijving()}")
        stapCounter += 1

def toonTotaalCalorieen(gekozenGerecht, plantaardigAlternatief, personen):
    totaalCal = 0
    for ingredient in recepten[gekozenGerecht].get_ingredienten():
        ingredient.set_hoeveelheid(personen)
        gekozenIngredient = ingredient.get_ingredient(plantaardigAlternatief)
        totaalCal += gekozenIngredient.get_kcal() * int(personen)
        print(f"* {gekozenIngredient.get_naam()}")

    print(f"Totaal {totaalCal} calorieën")

def toonReceptenOverzicht():
    print("TOON OVERZICHT RECEPTEN")
    gekozenGerecht = vraagGekozenGerechtOp()
    aantalPersonen = vraagAantalPersonenOp()
    recepten[gekozenGerecht - 1].set_aantal_personen(aantalPersonen)
    wiltPlantaardigAlternatief = vraagPlantaardigAlternatiefOp()
    toonStappenRecept(gekozenGerecht - 1)
    toonTotaalCalorieen(gekozenGerecht - 1, wiltPlantaardigAlternatief, aantalPersonen)

    vraagPDFBestand(gekozenGerecht)
            
def keuzeMenuOpties():
    keuzeNummer = 1
    keuzeMenu = ["Recept toevoegen", "Overzicht tonen", "Exit"]
    keuze = 0
    keuzeIngevoerd = False

    for keuze in keuzeMenu:
        print(keuzeNummer, keuze)
        keuzeNummer += 1

    while True:
        try:
            keuze = int(input("Kies een keuze uit het menu? "))
            keuzeIngevoerd = True
            break
        except ValueError:
            print("Foutive invoer")

    while keuze > len(keuzeMenu):
        print("Foutieve invoer. Kies toevoegen, tonen of exit")
        keuze = int(input("Kies een keuze uit het menu? "))

    if keuzeIngevoerd:
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
