nabors = int(input())
for _ in range(nabors):
    (n, m, k) = [int(i) for i in input().split()]
    aa = [str(i) for i in input().split()]
    bb = [str(i) for i in input().split()]
    cnt_aa = Counter(aa[:m])
    cnt_bb = Counter(bb)
    D = cnt_aa & cnt_bb
    pairs_in_D = sum(D.values())
    E = cnt_aa - D
    C = cnt_bb - D
    fnd = 1 if pairs_in_D >= k else 0
    for (in_aa, out_aa) in zip(aa[m:], aa[:n - m]):
        if D[out_aa] > 0:
            if E[out_aa] > 0:
                E[out_aa] -= 1
            else:
                D[out_aa] -= 1
                pairs_in_D -= 1
                C[out_aa] += 1
        else:
            E[out_aa] -= 1
        if C[in_aa] > 0:
            D[in_aa] += 1
            pairs_in_D += 1
            C[in_aa] -= 1
        else:
            E[in_aa] += 1
        fnd += 1 if pairs_in_D >= k else 0
    print(fnd)