k = int(input())
n, digits = 1, 1
while True:
    if k <= n * digits:
        num = (k - 1) // digits + 10**(digits-1)
        digit = (k - 1) % digits
        print(int(str(num)[digit]))
        break
    n *= 10
    k -= n * digits
    digits += 1
