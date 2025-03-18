for i in range(int(input())):
    s = int(input())
    e = input()
    P = 0
    M = 0
    for q in e:
        if q == '+':
            P += 1
        else:
            M += 1
    print(P-M)