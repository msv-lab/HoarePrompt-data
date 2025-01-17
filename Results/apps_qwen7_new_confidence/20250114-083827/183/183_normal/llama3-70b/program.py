a, b, c = map(int, input().split())
x, y, z = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if (a >= x and b >= y and c >= z):
    print("Yes")
else:
    total = a + b + c
    need = x + y + z
    if total < need:
        print("No")
    else:
        if need % 2 == 0:
            if (a + b + c - x) % 2 == 0 and (a + b + c - y) % 2 == 0 and (a + b + c - z) % 2 == 0:
                print("Yes")
            else:
                print("No")
        else:
            if (a + b + c - x) % 2 != 0 and (a + b + c - y) % 2 != 0 and (a + b + c - z) % 2 != 0:
                print("Yes")
            else:
                print("No")
