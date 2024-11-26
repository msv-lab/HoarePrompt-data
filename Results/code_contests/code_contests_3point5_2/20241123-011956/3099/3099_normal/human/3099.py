gls = raw_input()

good_letters = set(c for c in gls)

p = raw_input()
plen = len(p)

n = input()

if '*' not in p:
    for _ in range(n):
        q = raw_input()
        qlen = len(q)
        if qlen != plen:
            print("NO")
            continue

        y = True
        for i in range(plen):
            if p[i] == '?':
                if q[i] not in good_letters:
                    print("NO")
                    y = False
                    break

            elif p[i] != q[i]:
                print("NO")
                y = False
                break

        if y:
            print("YES")

else:
    p0, p1 = p.split("*")
    p1 = p1[::-1]
    p0len = len(p0)
    p1len = len(p1)

    for _ in range(n):
        q = raw_input()
        qlen = len(q)
        if qlen < plen - 1:
            print("NO")
            continue

        y0 = True
        for i in range(p0len):
            if p0[i] == '?':
                if q[i] not in good_letters:
                    print("NO")
                    y0 = False
                    break

            elif p0[i] != q[i]:
                print("NO")
                y0 = False
                break

        if y0 == False: continue
        y1 = True
        qr = q[::-1]
        for i in range(p1len):
            if p1[i] == '?':
                if qr[i] not in good_letters:
                    print("NO")
                    y1 = False
                    break

            elif p1[i] != qr[i]:
                print("NO")
                y1 = False
                break

        if y1 == False: continue

        t = None
        if p1len == 0:
            t = q[p0len:]
        else:
            t = q[p0len:-p1len]

        if len(set(t).intersection(good_letters)) > 0:
            print("NO")
            continue
        if y0 and y1:
            print("YES")
