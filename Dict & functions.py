dictionary = {}

def namen():
    naam = str(input("Geef een naam:"))
    if naam != "":
        if naam not in dictionary:
            dictionary[naam] = 1
        elif naam in dictionary:
            dictionary[naam] += 1
        namen()
    elif naam == "" or naam == " ":
        for i in dictionary:
            if dictionary[i] == 1:
                print("Er is 1 student met de naam,", i)
            else:
                print("Er zijn",dictionary[i], "studenten met de naam", i)

namen()