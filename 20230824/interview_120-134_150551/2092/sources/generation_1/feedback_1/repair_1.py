m, n, k, t = map(int, input().split())
soldiers = sorted(list(map(int, input().split())), reverse=True)
traps = []
for _ in range(k):
    traps.append(list(map(int, input().split())))
traps.sort(key=lambda x: x[2], reverse=True)

maxSoldiers = 1
remainingTime = t
curPos = 0
curTime = 0

for i in range(m):
    if curPos+1 > n or curTime+curPos+1 > remainingTime:
        break
    
    if curPos+1 <= n and curPos+1 <= remainingTime and curTime+curPos+1-max(curPos, curPos) <= remainingTime:
        maxSoldiers = i+1

    remainingTime -= soldiers[i]
    curPos += 1
    curTime += 1
    
    for j in range(k):
        if curPos+1 > n or curTime+curPos+1 > remainingTime:
            break

        if curPos+1 < traps[j][0] or curPos+1 > traps[j][1] or soldiers[i] < traps[j][2]:
            curPos += 1
            curTime += 1

        else:
            curPos += 1

print(maxSoldiers)