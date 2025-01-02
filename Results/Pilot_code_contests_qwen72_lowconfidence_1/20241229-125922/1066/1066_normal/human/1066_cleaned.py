(n, k, a, b) = map(int, raw_input().split())

def func_1(pos, amp, debut, fins):
    global a, b
    if debut == fins:
        return a
    if amp == 1:
        return b * (fins - debut)
    else:
        borne = pos + amp // 2
        deb = debut - 1
        fin = fins
        while fin - deb > 1:
            m = (fin + deb) // 2
            if antman[m] >= borne:
                fin = m
            else:
                deb = m
        r = min(func_1(pos, amp // 2, debut, fin) + func_1(borne, amp // 2, fin, fins), b * amp * (fins - debut))
        return r
antman = sorted(map(int, raw_input().split()))
print(func_1(1, 2 ** n, 0, k))