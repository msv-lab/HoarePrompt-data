def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

area1 = a1 * b1
area2 = a2 * b2

if area1 != area2:
    print(-1)
else:
    g = gcd(a1, b1)
    a1 //= g
    b1 //= g
    g = gcd(a2, b2)
    a2 //= b2
    b2 //= g

    minutes = 0
    while a1 != a2 or b1 != b2:
        if a1 > a2:
            if a1 % 2 == 0:
                a1 //= 2
            elif a1 % 3 == 0:
                a1 //= 3
            else:
                break
            minutes += 1
        elif a1 < a2:
            if a2 % 2 == 0:
                a2 //= 2
            elif a2 % 3 == 0:
                a2 //= 3
            else:
                break
            minutes += 1
        if b1 > b2:
            if b1 % 2 == 0:
                b1 //= 2
            elif b1 % 3 == 0:
                b1 //= 3
            else:
                break
            minutes += 1
        elif b1 < b2:
            if b2 % 2 == 0:
                b2 //= 2
            elif b2 % 3 == 0:
                b2 //= 3
            else:
                break
            minutes += 1
    if a1 == a2 and b1 == b2:
        print(minutes)
        print(a1, b1)
        print(a2, b2)
    else:
        print(-1)
