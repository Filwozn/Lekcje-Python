age = int(input("Ile masz skończone lat? "))
if age>20:
    print("Możesz prowadzić samochód oraz głosować w wyborach")
elif (17<age<21):
    print("Możesz prowadzić samochód")
else:
    print("Nie możesz głosować ani prowadzić samochodu")
