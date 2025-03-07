nabors = int(input())
for _ in range(nabors):
    (n, m, k) = [int(i) for i in input().split()]
    aa = [int(i) for i in input().split()]
    bb = [int(i) for i in input().split()]
    cnt_aa = Counter(aa[:m])
    cnt_bb = Counter(bb)
    D = cnt_aa & cnt_bb
    E = cnt_aa - D
    C = cnt_bb - D
    tot = sum(D.values())
    fnd = 1 if tot >= k else 0
    for (in_aa, out_aa) in zip(aa[m:], aa[:n - m]):
        if D[out_aa] > 0:
            if E[out_aa] > 0:
                E[out_aa] -= 1
            else:
                D[out_aa] -= 1
                C[out_aa] += 1
        else:
            E[out_aa] -= 1
        if C[in_aa] > 0:
            if C[in_aa] == D[in_aa]:
                C[in_aa] += 1
            else:
                D[in_aa] += 1
        else:
            E[in_aa] += 1
        tot = sum(D.values())
        fnd += 1 if tot >= k else 0
    print(fnd)