s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = "aeiou"

for letter in s:
    if letter in klinkers:
        print(letter)
