leeftijd = int(input("Hoe oud ben je?"))
paspoort = input("Heb je een nederlands paspoort? ja/nee")

if leeftijd > 17 and paspoort == "ja":
    print("Je mag stemmen!")
else:
    print("Je mag niet stemmen :(")