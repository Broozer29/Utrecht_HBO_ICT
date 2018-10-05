def seizoen(maand):
    if (maand < 3 or maand == 12):
        print("Het is winter! Kerstfeest woehoe!")
    if (maand > 3 and maand < 6):
        print("Het is Lente!")
    if (maand > 6 and maand < 10):
        print("Het is Zomer!")
    if (maand > 10 and maand < 12):
        print("Het is Herfst!")


seizoen(8)