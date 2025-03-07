t = int(input())
for r in range(t):
    n = int(input())
    f = 1
    num = [int(_) for _ in input().split()]
    for j in range(n -1):
        if num[j] != num[j + 1]:
            f = 0
            break
    if n == 1 or f == 1:
        print(0)
        continue
    onum = num.copy()
    onum.reverse()
    cn = 1
    ck = 1
    f = 1 
    symb1 = num[0]
    symb2 = onum[0]
    for i in range(n - 1):
        if num[i] == num[i + 1]:
            cn += 1
        else:
            break
    for ii in range(n - 1):
        if onum[ii] == onum[ii + 1]:
            ck += 1
        else:
            break        
    if symb1 == symb2:
        cn += ck
    print(n - max(cn, ck))