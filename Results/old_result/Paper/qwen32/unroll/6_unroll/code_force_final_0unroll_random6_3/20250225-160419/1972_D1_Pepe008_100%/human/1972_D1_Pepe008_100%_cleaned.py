T = int(input())
for t in range(T):
    info = input().split()
    (a, b) = (int(info[0]), int(info[1]))
    suma = 0
    for i in range(1, b + 1):
        x = (a - i * (i - 1)) // i ** 2 + 1
        if (a - i * (i - 1)) // i ** 2 + 1 > 0:
            suma += x
            if (a - i * (i - 1)) % i ** 2 == 0 and i * (i - 1) % i ** 2 == 0:
                suma += 1
    print(suma - 2)