kapital_poczatkowy = int(input("Podaj wysokość kapitału: "))
miesieczne_wplywy = int(input("Podaj wysokość miesięcznych wpływów: "))
planowana_wartosc_koncowa = int(input("Podaj pożądaną końcową wartość inwestycji: "))
planowany_czas = int(input("Podaj planowaną ilość miesięcy na inwestycją: "))
procent_dodatkowy = 0.02

wartosc_koncowa = (kapital_poczatkowy + (planowany_czas * miesieczne_wplywy) + procent_dodatkowy * (kapital_poczatkowy + (planowany_czas * miesieczne_wplywy)))

if(wartosc_koncowa > planowana_wartosc_koncowa):
    print ("cel inwestycyjny osiągnięty")
else:
    print ("Cel nie osiągnięty") 
