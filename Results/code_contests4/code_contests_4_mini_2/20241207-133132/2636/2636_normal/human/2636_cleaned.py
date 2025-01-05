for line in stdin:
    c = [int(s) for s in line.split()]
    cards = [i for i in range(1, 11) if i not in c]
    c1c2 = c[0] + c[1]
    e = sum((int(i + c1c2 <= 20) for i in cards))
    print('YES' if e > 3 else 'NO')