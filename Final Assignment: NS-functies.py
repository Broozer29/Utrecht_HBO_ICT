def standaardprijs(afstandKM):
    teBetalen = 0
    if afstandKM > 50:
        return teBetalen + (afstandKM * 0.60) + 15
    elif afstandKM < 0:
        return teBetalen
    else:
        return teBetalen + (afstandKM * 0.80)


def ritprijs(leeftijd, weekendrit, afstandKM):
    teBetalen = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd > 65:
        teBetalen = (teBetalen / 100) * 70
        print('70%!')
        if weekendrit is True:
            teBetalen = (teBetalen / 100) * 65
            print('Weekend korting!')
    else:
        if weekendrit is True:
            teBetalen = (teBetalen / 100) * 60
            print('Weekend korting!')
    print(teBetalen)


ritprijs(11, False, 51)