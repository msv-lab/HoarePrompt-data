t = int(input())
for q in range(t):
    a = input()
    b = input()
    kq1 = ''
    kq2 = ''
    vt = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            kq1 = kq1 + a[i]
            kq2 = kq2 + a[i]
            continue
        else:
            (x, y) = (min(int(a[i]), int(b[i])), max(int(a[i]), int(b[i])))
            if vt == 0:
                vt = 1
                kq1 = kq1 + str(x)
                kq2 = kq2 + str(y)
            else:
                kq1 = kq1 + str(y)
                kq2 = kq2 + str(x)
    print(kq1)
    print(kq2)