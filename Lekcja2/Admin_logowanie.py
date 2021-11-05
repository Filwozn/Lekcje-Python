username = "Admin"
password = "1234"

get_username = input("Podaj username: ")
get_password = input("Podaj hasło: ")

while username != get_username or password != get_password:
    print("Niepoprawne dane!")
    get_username = input("Podaj username: ")
    get_password = input("Podaj hasło: ")
print("poprawne dane!")
