import sys
from collections import Counter
import itertools as it
import copy


print = lambda x: sys.stdout.write(str(x) + "\n")
input = lambda: sys.stdin.readline().strip()



tc = int(input())
for _ in range(tc):

    n,k  = map(int, input().split())
    a = list(map(int, input().split()))
    k = 2*k

    half = a[:n]
    half2 = a[n:]
    cnts = Counter(half)
    cnts2 = Counter(half2)
    pairs = 0
    singles = 0

    for num, cnt in cnts.items():
        if cnt == 1:
            singles+=1
        else:
            pairs+=1

    #print(f"singles: {singles}, pairs: {pairs} in {half}, k={k}")
    found = False
    ws = 0
    wp = 0
    for wanted_singles in range(k+1):
        if wanted_singles > singles:
            continue
        if (k - wanted_singles) % 2 == 1:
            continue

        wanted_pairs = (k-wanted_singles) >> 1
        if wanted_pairs > pairs:
            continue

        found = True
        ws = wanted_singles
        wp = wanted_pairs
        break

    assert found

    #print(f"ws: {ws}, wp: {wp}")

    res1 = []
    res2 = []
    hs = 0
    for ai in half:
        if hs == ws:
            break
        if cnts[ai] == 1:
            hs+=1
            res1.append(ai)
            res2.append(ai)

    hp = 0
    for ai, cnt in cnts.items():
        if hp == wp:
            break
        if cnt == 2:
            hp+=1
            res1.append(ai)
            res1.append(ai)

    hp = 0
    for ai, cnt in cnts2.items():
        if hp == wp:
            break
        if cnt == 2:
            hp+=1
            res2.append(ai)
            res2.append(ai)

    print(" ".join(map(str, res1)))
    print(" ".join(map(str, res2)))



