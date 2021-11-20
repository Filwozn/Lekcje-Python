
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista3 = [1,2,2,3,3,4,5]

if(set(lista1) == set(lista2) == set(lista3)):
    print("takie same elementy tych list")
else:
    print("inne")

set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)

containts_duplicate = len(lista1) !=len(set1)
if containts_duplicate == True:
    print('lista1 zawieta duplikaty!')
containts_duplicate = len(lista2) !=len(set2)
if containts_duplicate == True:
    print('lista2 zawieta duplikaty!')
containts_duplicate = len(lista3) !=len(set3)
if containts_duplicate == True:
    print('Lista3 zawieta duplikaty!')

'''
print('zad6 sprawdzenie elementów w listach')

lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
lista3 = [1,2,2,3,3,4,5]
set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)
print(set1, set2, set3)
print(set1 |set2)
print(set2 |set3)
print(set2 & set3)
print(set2.issubset(set3))
'''