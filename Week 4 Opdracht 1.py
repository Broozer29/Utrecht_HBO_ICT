def lang_genoeg():
    minLengte = 120
    echtelengte = int(input("Hoe lang ben je?"))
    if echtelengte > minLengte:
        print("Je bent lang genoeg voor de attractie!")
    else:
        print("Sorry, je bent te klein!")
lang_genoeg()

