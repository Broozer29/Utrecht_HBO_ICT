studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
   antw = []
   for i in studentencijfers:
       gemiddelde = (i[0] + i[1] + i[2]) / 2
       antw.append(gemiddelde)
   return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    antw = 0
    aantalCijfers = len(studentencijfers[0])
    for i in studentencijfers:
        cijfer = i[0] +i[1] + i[2]
        antw += cijfer / aantalCijfers
    antw = antw / len(studentencijfers)
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))

