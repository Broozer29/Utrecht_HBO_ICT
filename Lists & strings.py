def countList(list):
    nieuweList = []
    for woorden in list:
        if len(woorden) == 4:
            nieuweList.append(woorden)
    print("De nieuw-gemaakte lijst met alle vier-letter strings is: ", nieuweList)



def maakList():
    list = eval(input("Geef lijst met minimaal 10 strings: "))
    print(list)
    countList(list)
maakList()



#["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]