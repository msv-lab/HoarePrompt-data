le = sys.__stdin__.read().split('\n')[::-1]
af = []
for i in range(int(le.pop())):
    (d, k) = list(map(int, le.pop().split()))
    a = floor(d / (k * 2 ** 0.5))
    if (a * k) ** 2 + (k * (a + 1)) ** 2 > d ** 2:
        af.append('Utkarsh')
    else:
        while (a * k) ** 2 + (k * (a + 2)) ** 2 > d ** 2 and a > 0:
            a -= 1
        if ((a + 1) * k) ** 2 + (k * (a + 2)) ** 2 > d ** 2:
            af.append('Utkarsh')
        else:
            af.append('Ashish')
print('\n'.join(map(str, af)))