file = open('Kaartnummer.txt', 'r').read()
aantalRegels = 1
getal = ''
tijdelijkGetal = 0

for i in file:
    if i == '\n':
        aantalRegels += 1
    if i.isdecimal():
        getal += i
    if len(getal) == 6:
        if int(getal) > tijdelijkGetal:
            tijdelijkGetal = int(getal)
            print(tijdelijkGetal)
            getal = ''
        else:
            getal = ''
