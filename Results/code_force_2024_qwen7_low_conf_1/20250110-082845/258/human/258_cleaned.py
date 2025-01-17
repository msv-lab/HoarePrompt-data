def func_1(x):
    if x == 1:
        return [1]
    bits = []
    while x > 0:
        bit = x & 1
        bits.append(bit)
        x >>= 1
    n = len(bits)
    a = [0] * n
    for i in range(n - 1):
        if bits[i]:
            a[i] = 1
        if bits[i + 1]:
            a[i + 1] = -1
    return a