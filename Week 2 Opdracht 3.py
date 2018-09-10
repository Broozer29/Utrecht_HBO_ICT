letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
AantalA = 0
AantalB = 0
AantalC = 0


for i in letters:
    if i == 'A':
        AantalA += 1
    elif i == 'B':
        AantalB += 1
    elif i == 'C':
        AantalC += 1

Nieuwelijst = [AantalA, AantalB, AantalC]
print(Nieuwelijst)