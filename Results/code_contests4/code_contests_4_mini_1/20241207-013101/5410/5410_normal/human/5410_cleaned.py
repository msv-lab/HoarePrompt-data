(N, A, B) = map(int, raw_input().split())
v = map(int, raw_input().split())
resultValue = 0
resultCount = 0
for pcs in range(B - A + 1):
    perm = list(itertools.combinations(v, B + pcs))
    for cand in perm:
        average = float(sum(cand)) / len(cand)
        if resultValue < average:
            resultValue = average
            resultCount = 1
        elif resultValue == average:
            resultCount += 1
print(resultValue)
print(resultCount)