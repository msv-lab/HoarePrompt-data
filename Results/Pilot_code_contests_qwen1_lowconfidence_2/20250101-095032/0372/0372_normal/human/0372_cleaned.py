n = int(raw_input())
for i in range(n / 2):
    if gcd(n - i, i) == 1:
        print(str(i) + ' ' + str(n - i))