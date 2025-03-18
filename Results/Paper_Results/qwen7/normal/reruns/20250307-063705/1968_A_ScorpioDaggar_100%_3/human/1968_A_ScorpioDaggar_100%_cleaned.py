n: int = int(input(''))
for _ in range(n):
    x: int = int(input(''))
    max = -1
    argmax_y = -1
    for y in range(1, x):
        eq = gcd(x, y) + y
        if eq > max:
            max = eq
            argmax_y = y
    print(argmax_y)