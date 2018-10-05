def gemiddelde():
    zin = str(input("Geef uw zin op: "))
    woorden = zin.split()
    gemiddelde = sum(len(woorden) for woorden in woorden) / len(woorden)
    print(gemiddelde)


gemiddelde()
