n = int(input())
a = int(input())
b = int(input())
c = int(input())
if a <= b - c:
    print(n // a)
else:
    k = (n - b) // (b - c) + 1
    remaining_rubles = n - k * (b - c)
    if remaining_rubles < b:
        print(k + remaining_rubles // a)
    else:
        print(k + 1)