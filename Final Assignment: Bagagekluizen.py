def toon_aantal_kluizen_vrij(tekstBestand):
    maxAantalKluizen = 12
    aantalRegels = 0
    for i in tekstBestand:
        if i == '\n':
            aantalRegels += 1
    print("Aantal kluizen vrij: ", maxAantalKluizen - aantalRegels)

def nieuwe_kluis(tekstBestand):
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    gebruikteKluisnummer = []
    bruikbaareNummers = []
    for line in tekstBestand:
        currentline = line.split(";")
        gebruikteKluisnummer.append(int(currentline[0]))
    for x in kluisnummers:
        if x not in gebruikteKluisnummer:
            bruikbaareNummers.append(x)
            if len(gebruikteKluisnummer) < 12:
                password = input("Voer uw wachtwoord van minimaal 4 tekens in: ")
                if len(password) >= 4:
                    bestand = open("Kluizen.txt", "a")
                    bestand.write(str(min(bruikbaareNummers)) + ';' + str(password) + '\n')
                    bestand.close()
                    print('Uw kluisnummer is: ' + str(min(bruikbaareNummers)))
                    return
            else:
                print("Er zijn geen kluizen beschikbaar.")

    return

def kluis_openen(bestand):
    nummer = input("Wat is uw kluisnummer: ")
    wachtwoord = input("Wat is uw wachtwoord: ")
    gegevens = nummer + ';' + wachtwoord + '\n'
    if gegevens in bestand:
        print("Kluis nummer " + str(nummer) + " is nu open.")
    else:
        print("Kluisnummer en/of code incorrect.")
    return

def kluis_teruggeven(bestand):
    nummer = input("Wat is uw kluisnummer: ")
    wachtwoord = input("Wat is uw wachtwoord: ")
    gegevens = nummer + ';' + wachtwoord + '\n'
    if gegevens in bestand:
        bestand = [x for x in bestand if x not in gegevens]
        for i in bestand:
            tekstBestand = open("Kluizen.txt", 'w')
            tekstBestand.write(i)
            tekstBestand.close()
            print("Uw kluist is vrijgegeven.")
    else:
        print("Uw ingevoerde gegevens zijn incorrect.")
    return

def main():
    bestand = open("Kluizen.txt", "r+")
    tekstBestand = bestand.readlines()
    bestand.close()
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen \n4: Ik geef mijn kluis terug")
    welkeKeus = int(input("Wat wilt u doen: "))
    if welkeKeus == 1:
        toon_aantal_kluizen_vrij(tekstBestand)
    elif welkeKeus == 2:
        nieuwe_kluis(tekstBestand)
    elif welkeKeus == 3:
        kluis_openen(tekstBestand)
    elif welkeKeus == 4:
        kluis_teruggeven(tekstBestand)


main()
