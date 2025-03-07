for _ in range(int(input())):
    a = list(map(int,list(input())))
    b = list(map(int,list(input())))
    new = [None]*len(a)
    new2 = [None]*len(a)
    i = 0
    while i<len(a) and a[i] == b[i]:
        new[i] = max(a[i],b[i])
        new2[i] = min(a[i],b[i])
        i += 1
    if i!=len(a):
        new[i] = max(a[i],b[i])
        new2[i] = min(a[i],b[i])
        i += 1
        while i<len(a):
            new[i] = min(a[i],b[i])
            new2[i] = max(a[i],b[i])
            i+=1
    print("".join(str(x) for x in new))
    print("".join(str(x) for x in new2))