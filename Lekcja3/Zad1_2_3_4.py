import heapq



print('zad1 odwrócenie listy')
lista = [1,2,3,4,5]
lista.reverse()
print('odwrocona_lista =', lista)

print('zad2 lista_max')

lista.sort()
print('lista_max = [', lista[len(lista)-1],',',lista[len(lista)-2],']')

print('zad3 lista liczb')

for x in range(3, 14):
  lista [x] =+ x
  lista.append(x)

print(lista)

lista2 = []
i = 0
while len(lista2) < 11:
  lista2.append(i)
  i +=1

print(lista2)

print('zad4 skryptUser')

dane_logowania = {'Admin':'1234'}
print(dane_logowania)


get_username = input("Podaj username: ")
get_password = input("Podaj hasło: ")

dane_logowania_uzytkownika ={get_username : get_password}




while dane_logowania != dane_logowania_uzytkownika:
    get_username = input("Podaj username: ")
    get_password = input("Podaj hasło: ")
    dane_logowania_uzytkownika = {get_username : get_password} 
print('Logowanie poprawne')
   
 




 












'''
def rev_list(lista):
    lista = [1,2,3,4,5]
    odwrocona_lista = lista[::-1]
    return odwrocona_lista
    '''