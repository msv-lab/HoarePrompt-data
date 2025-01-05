testSNs = raw_input().split()
SCORE=int(0)
for x in range(testSNs[0]):
    if not testSNs[x]%10 is 0:
        SCORE += testSNs[x]
    else:
        continue
print(SCORE)