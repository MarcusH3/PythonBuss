
#Bibliotek
import json
import os
import random as rand

path = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(path,"Namnlista.json")) as f:
    Namnlista = json.load(f)
#Listor
kvinnligt_fornamn = Namnlista["namn_kvinna"]
manligt_fornamn = Namnlista["namn_man"]
efternamn = Namnlista["efternamn"]

passagerare = []
#Klass definitioner
class person():
    def __init__(self, namn, efternamn, kon, alder):
        self.namn = namn
        self.efternamn = efternamn
        self.kon = kon
        self.alder = alder
    def __str__(self):
        return f"Det har ar {self.namn} {self.efternamn}. {self.kon} och ar {self.alder} ar gammal."
    def setNamn(self, nyttNamn):
        self.namn = nyttNamn
    def setEfternamn(self,nyttefternamn):
        self.efternamn = nyttefternamn
    def setKon(self, nyttKon):
        self.kon = nyttKon
    def setalder(self, nyalder):
        self.alder = nyalder
#Funktionsdefinitioner
def clear_screen():
    os.system("""cls || clear""")
def plockaUpp(antal_passagerare):
    for i in range(antal_passagerare):
        if rand.random()>=0.5:
            fornamn_i_funktion = manligt_fornamn[rand.randint(0, len(manligt_fornamn)-1)]
            efternamn_i_funktion = efternamn[rand.randint(0, len(efternamn)-1)]
            alder = rand.randint(0,100)
            en_man = person (fornamn_i_funktion, efternamn_i_funktion, "Han", alder)
            passagerare.append(en_man)
        else:
            fornamn_i_funktion = kvinnligt_fornamn[rand.randint(0, len(kvinnligt_fornamn)-1)]
            efternamn_i_funktion = efternamn[rand.randint(0, len(efternamn)-1)]
            alder = rand.randint (0,100)
            en_kvinna = person(fornamn_i_funktion, efternamn_i_funktion, "Hon",alder)
            passagerare.append(en_kvinna)
def gaAv(antal_passagerare):
    for i in range(antal_passagerare):
        passagerare.pop(rand.randint(0,len(passagerare)-1))
def skrivUt():
    for i, person in enumerate(passagerare):
        print (f"{i+1}. {person}")
def sammanlagdalder():
    return sum([person.alder for person in passagerare])
def aldst():
    aldsta_personer = []
    aldsta_person = max([person.alder for person in passagerare])
    for person in passagerare:
        if person.alder == aldsta_person:
            aldsta_personer.append(person)
        for i, person in enumerate(aldsta_personer):
            print(f"{i+1}. {person}")
def medelalder():
    return round(sum([person.alder for person in passagerare])/len(passagerare))

def hittaPassagerare(lagstaalder, hogstaalder):
    alderSpann_personer = []
    for person in passagerare:
        if person.alder >= lagstaalder and person.alder <= hogstaalder:
            alderSpann_personer.append(person)
    print ("")
    if len(alderSpann_personer) == 0:
        print (f" Det finns inga passagerare mellan {lagstaalder} ar och {hogstaalder} ar.")
    else:
        for i, person in enumerate(alderSpann_personer):
            print (f"{i+1}. {person}")


def sortera():

    sorteringsVal = ""

    clear_screen()

    while sorteringsVal != "q":

        print( """"
            ---Sorteringsmeny---
            1. Sortera efter alder
            2. Sortera efter kon
            q. aterga till huvudmeny
        -----------------------            """ )
        sorteringsVal = input(" ->")

        if sorteringsVal == "1":
            passagerare.sort(key=lambda x: x.alder)
            clear_screen()
            print (" Bussen har sorterats efter passagerarnas alder")
        elif sorteringsVal == "2":
            passagerare.sort(key=lambda x: x.kon)
            clear_screen()
            print("Bussen ar nu sorterad efter kon")
        elif sorteringsVal == "q":
            clear_screen()
            print("felaktig inmatning.")
    clear_screen()
def main():

    menyVal = ""

    clear_screen()

    while menyVal != "q":

        print (
            """ Valkommen ombord pa bussen                                                  
                                    _____________
                                 _/_|[][][][][] | - -
                                (      City Bus | - -
                                =--OO-------OO--=dwb 
            """)
        print(
            """Valj ett alternativ nedan for att borja
             1. Plocka upp ny passagerare
             2. Lat passagerare ga av
             3. Skriv ut alla passagerare
             4. Skriv ut total alder
             5. Hitta passagerare med hogst alder
             6. Berakna medelalder
             7. Sorterings meny
             8. Hitta passagerare med viss alder
             q. Avsluta
             ---------------------------------------------- 
            """)

        menyVal = input (" -> ")

        if menyVal == "1":

            antal = rand.randint(0, 10)
            lediga_platser = 25 - len(passagerare)

            if lediga_platser > 0:
                if lediga_platser>= antal:
                    antal_pastigna = antal
                    clear_screen()
                    print(f"{antal_pastigna}ny/nya passagerare steg ombord bussen.")
                else:
                    antal_pastigna = lediga_platser #Annars far endast vissa personer plats
                    clear_screen()
                    print(f"Det fanns {antal} passagerare pa busshalsplatsen men endast {antal_pastigna} kunde stiga pa.")
                plockaUpp(antal_pastigna) #Funktionen plockaUpp anropas sedan med antalet som far plats som argument
            else: #Om bussen ar full far inga ga ga
                clear_screen()
                print("Bussen ar full.")

        elif menyVal == "2":
            if len (passagerare) > 10:
                antal = rand.randint(0,10)
                gaAv(antal)
                clear_screen()
                print (f"{antal} passagerare stev av bussen.")
            elif len(passagerare)>= 1:
                antal =rand.randint(0,len(passagerare))
                gaAv(antal)
                clear_screen()
                print(f"{antal} passagerare steg av bussen.")
            else:
                clear_screen()
                print("Inga passagerare befinner sig pa bussen")

        elif menyVal == "3":
            if len(passagerare)>=1:
                clear_screen()
                skrivUt()
            else:
                clear_screen()
                print ("Inga passagerare ar pa bussen")

        elif menyVal == "4":
            if len(passagerare)>=1:
                clear_screen()
                print(f"Den sammanlagda aldern hos  {len(passagerare)} passagerare ar {sammanlagdalder()}.")
            else:
                clear_screen()
                print("inga passagerare befinner sig pa bussen, sammanlagd alder = 0")

        elif menyVal == "5":
            if len(passagerare)>=1:
                clear_screen()
                aldst()
            else:
                clear_screen()
                print (" Bussen ar tom, inga passagerare har stigit pa.")

        elif menyVal == "6":
            if len(passagerare)>=1:
                clear_screen()
                print(f"Medelaldern hos de {len(passagerare)} passagerare ar {medelalder()}.")
            else:
                clear_screen()
                print("Inga passagerare ar pa bussen, saledes gar ej medelaldern att berakna.")

        elif menyVal == "7":
            if len(passagerare)>= 1:
                clear_screen()
                sortera()
            else:
                clear_screen()
                print ("Inga passagerare pa bussen")
        elif menyVal == "8":
            if len(passagerare)>=1:
                clear_screen()

                while True:
                    lagstaalder = input("Ange lagst alder for passageraren du vill hitta -> ")
                    if lagstaalder.isdigit():
                        break
                    else:
                        clear_screen()
                        print("Du har angivit ett felaktigt varde.")
                while True:
                    hogstaalder = input("Ange hogst alder for den passagerare du vill hitta -> ")
                    if hogstaalder.isdigit():
                        break
                    else:
                        clear_screen()
                        print("Du har angivit ett felaktigt varde")

                clear_screen()
                hittaPassagerare(int(lagstaalder),int (hogstaalder))

                input(
                    """
                    Tryck pa valfri knapp for att fortsatta...        
                      """)
            else:
                clear_screen()
                print (" Inga passagerare ar pa bussen.")

        elif menyVal== "q":
            clear_screen()
            print("Felaktig inmatning.")

main()
