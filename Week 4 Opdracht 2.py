def new_password():
    oldpassword = input("Wat was je oude wachtwoord?")
    newpassword = input("Wat is je huidige wachtwoord?")
    if newpassword != oldpassword:
        print(len(newpassword) > 6)
    else:
        print("Je kan toch niet hetzelfde wachtwoord gebruiken!")

new_password()