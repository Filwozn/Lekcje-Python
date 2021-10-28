kapital_poczatkowy = int(input("Podaj kapitał poczatowy"))
wplywy = int(input("podaj miesieczne wpływy: "))
wydatki = int(input("podaj miesieczne wydatki: "))

oszczednosci = kapital_poczatkowy + 12 * (wplywy-wydatki)
print("Twoje oszczednosci wynosza: ", oszczednosci)
print(wplywy)
print(kapital_poczatkowy)               
