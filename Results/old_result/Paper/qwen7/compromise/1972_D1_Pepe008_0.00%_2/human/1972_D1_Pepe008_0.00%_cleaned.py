T = int(input())
for t in range(T):
    info = input().split()
    (a, b) = (int(info[0]), int(info[1]))
    'for i in range(1,a+1):\n        for j in range(4,b+1):\n            if int((j+i)%(j*math.gcd(i,j))) == 0:\n                print(i,j)'
    suma = 0
    for i in range(1, b + 1):
        x = (a - i * (i - 1)) // i ** 2 + 1
        if a - i * (i - 1) > 0:
            suma += x
    print(suma - 1)