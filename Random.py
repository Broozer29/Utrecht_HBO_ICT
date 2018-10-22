import random
getal = 0

def monopolyWorp():
    while True:
        a = random.randrange(1,7)
        b = random.randrange(1,7)
        print(a + b)
        if a == b:
            print("Dubbel")
            getal += 1
            print("getal", getal)
        else:
            getal = 0
        if getal == 3:
            break

monopolyWorp()