size1, size2 = map(int, raw_input().split())


lista1 = map(int,raw_input().split())
lista2 = map(int,raw_input().split())

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

intersec = intersection(lista1,lista2)

if(len(intersec) > 0):
    menorInter = intersec[0]
    for i in range(len(intersec)):
        if(intersec[i] < menorInter):
            menorInter = intersec[i]
    print(menorInter)
else:
    menor1 = lista1[0]
    for i in range(size1):
        if(lista1[i] < menor1):
            menor1 = lista1[i]
    
    menor2 = lista2[0]
    for i in range(size2):
        if(lista2[i] < menor2):
            menor2 = lista2[i]
    if(menor1 == menor2):
        print(menor1)
    elif(menor1 < menor2):
        print(str(menor1) + str(menor2))
    else:
        print(str(menor2) + str(menor1))

