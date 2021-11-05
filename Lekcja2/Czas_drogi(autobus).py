dystansAB = 250
czasPociągu = 165
czasSamochodu = int(input("Ile minut planujesz poświęcić na pokonanie dystansu z A do B? "))
"""Trzeba wpisać prędkość średnią, a nie czas"""
if(czasPociągu > czasSamochodu):
    print("Samochodem będzie szybciej")
else:
    print("Pociągiem będzie szybciej")
