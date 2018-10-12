def main():
    totaal = 0
    aantalGetallen = 0
    user_input = int(input("Enter number: "))

    while user_input != 0:
        totaal += user_input
        aantalGetallen += 1
        user_input = int(input("Enter number: "))
    if user_input == 0:
        print("Er zijn ",aantalGetallen," getallen ingevoerd, de som is: ",totaal)

main()