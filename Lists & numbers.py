def main():
    invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
    list = invoer.split("-")
    list.sort()
    nieuweList = []
    totaal = 0
    for i in list:
        totaal += int(i)
        nieuweList.append(int(i))
    print("Gesoorteerde list: ", nieuweList)
    print("Het minimum getal is: ", min(list), "Het maximum getal is: ", max(list))
    print("Aantal getallen: ", len(list), "Som van de getallen: ", totaal)
    print("Gemiddelde: ", totaal / len(list))


main()
