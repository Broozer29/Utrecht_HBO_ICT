def main():
    user_input = str(input("Geef een string van vier letters: "))

    while user_input != " ":
        lengte = len(user_input)
        while lengte != 4:
            user_input = str(input("Geef een string van vier letters: "))
            lengte = len(user_input)
            print(user_input, "heeft: ", lengte, "letters.")
        if lengte == 4:
            print("Inlezen van correcte string: ",user_input," is geslaagd!")
            break

main()