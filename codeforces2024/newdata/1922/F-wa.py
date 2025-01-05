from collections import Counter
t = int(input())
list1 = []
for i in range(t):
    a1 = input()
    a2 = a1.split()
    n = int(a2[0])
    x = int(a2[1])
    m = input()
    m1 = m.split()
    m2 = [int(k) for k in m1]

    tekrar_sayilari = Counter(m2)

    en_az_tekrar = min(tekrar_sayilari.values())

    list1.append(en_az_tekrar)

for i in list1:
    print(i)
