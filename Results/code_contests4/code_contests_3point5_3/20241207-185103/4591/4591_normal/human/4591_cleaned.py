for line in stdin:
    q = int(line)
    if q == -1:
        break
    x = q / 2.0
    diff = q * 1e-05
    while True:
        x = x - (x ** 3 - q) / (3 * x * x)
        if abs(x ** 3 - q) < diff:
            break
    print('{:.6f}'.format(x))