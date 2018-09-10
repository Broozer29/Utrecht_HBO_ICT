#Opdracht 1
a = 6
b = 7

if 75 > a and 75 < b:
    print('75 is groter dan A en kleiner dan B')
else:
    print('75 is NIET groter dan A en kleiner dan B')

#Opdracht 2
voornaam = 'Bruus'
tussenvoegsel = ' '
achternaam = 'Riezebos'

mijnnaam = voornaam + ' ' + tussenvoegsel + ' ' + achternaam
if len(mijnnaam) == (len(voornaam + tussenvoegsel + achternaam)):
    print("Mijn naam is even lang dan mijn naam")
else:
    print("De spaties tussen de voornaam, tussenvoegsel en achternaam tellen ook als letters, dus hij is niet langer. 10/10")

#Opdracht 3
if len(mijnnaam) > len(tussenvoegsel * 5):
    print('Mijnnaam is groter dan 5 maal mijn tussenvoegsel')
else:
    print('Mijnnaam is niet groter dan 5 maal mijn tussenvoegsel')

#Opdracht 4
if tussenvoegsel in achternaam:
    print('Tussenvoegsel zit in achternaam')
else:
    print('Tussenvoegsel zit niet in achternaam')