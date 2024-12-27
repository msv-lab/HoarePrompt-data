def kgood():
  a = raw_input().split()
  for i in range(len(a)):
    a[i] = int(a[i])
  kg = 0
  K = []
  k = int(a[1])
  for t in range(k):
    K.append(t)
  ligne = int(a[0])
  L = []
  for i in range(ligne):
    L.append(raw_input())
  for x in range(len(L)):
    L[x]= list(L[x])
    for i in range(len(L[x])):
      L[x][i] = int(L[x][i])
    test = True
    for j in K:
      test1 = j in L[x]
      if test1 == False:
        test = False
    if test == True:
      kg = kg + 1
  print(kg)

kgood()