'''
Approach:
1. Sort the soldiers in descending order of their agility.
2. Initialize a variable 'remainingTime' with t.
3. Initialize a variable 'maxSoldiers' with 0.
4. Initialize a list 'traps' to store the traps.
5. Iterate over the range(1, k+1):
    - Read trap details: l, r, d
    - Append [l, r, d] to traps.
6. Sort the traps based on their danger level 'd' in descending order.
7. Iterate over the range(m):
    - Initialize 'cnt' as 1.
    - Initialize 'curTime' as 0.
    - Initialize 'curPos' as 0.
    - Initialize 'squadPos' as 0.
    - Iterate over the range(k):
        - If curPos+1 > n or curPos+1 > remainingTime:
            - Break the loop
        - If squadPos+1 < traps[j][0] or squadPos+1 > traps[j][1] or soldiers[i] < traps[j][2]:
            - curTime += 1
            - curPos += 1
        - else:
            - squadPos += 1
    - If curPos+1 <= n and curPos+1 <= remainingTime and curTime+curPos+1-max(curPos, squadPos) >= remainingTime:
        - maxSoldiers = max(maxSoldiers, cnt)
    - remainingTime -= soldiers[i]
8. Print maxSoldiers.
'''

m, n, k, t = map(int, input().split())
soldiers = sorted(list(map(int, input().split())), reverse=True)
traps = []
for _ in range(k):
    traps.append(list(map(int, input().split())))
traps.sort(key=lambda x: x[2], reverse=True)

maxSoldiers = 0
for i in range(m):
    cnt = 1
    curTime = 0
    curPos = 0
    squadPos = 0

    for j in range(k):
        if curPos+1 > n or curPos+1 > t:
            break
        
        if squadPos+1 < traps[j][0] or squadPos+1 > traps[j][1] or soldiers[i] < traps[j][2]:
            curTime += 1
            curPos += 1
        else:
            squadPos += 1
            cnt += 1
    
    if curPos+1 <= n and curPos+1 <= t and curTime+curPos+1-max(curPos, squadPos) >= t:
        maxSoldiers = max(maxSoldiers, cnt)
    
    t -= soldiers[i]

print(maxSoldiers)