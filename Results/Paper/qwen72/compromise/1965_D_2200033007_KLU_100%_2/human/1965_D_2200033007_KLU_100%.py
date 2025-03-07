def getSubarraySums(a):
 
    cts = []
    for i in range(len(a)):
        sm = 0
        for j in range(i, len(a)):
            sm = sm + a[j]
            cts.append(sm)
 
    cts.sort()
    return cts
 
def getOddOccurringElements(cts):
 
    odds = []
 
    for ct in cts:
        if len(odds) > 0 and ct == odds[-1]:
            odds.pop()
        else:
            odds.append(ct)
    return odds
 
def getPalindrome(odds, n):
 
    a = [0] * n
    prev = 0
    idx = (n - 1) // 2
    
    for x in odds:
        if idx == n - 1 - idx:
            a[idx] = x
        else:
            a[idx] = (x - prev) // 2
            a[n - 1 - idx] = (x - prev) // 2
        prev = x
        idx = idx - 1
    
    return a
 
def getLargestExcluded(bigList, smallList):
 
    while len(smallList) > 0 and bigList[-1] == smallList[-1]:
        bigList.pop()
        smallList.pop()
    return bigList[-1]
 
t = int(input())
 
for tc in range(t):
 
    n = int(input())
    
    subarraySums = list(map(int, input().split()))
    subarraySums.sort()
    odds = getOddOccurringElements(subarraySums)
    
    missingSum = -1
    
    if len(odds) > (n + 1) // 2:
    
        oddvals = []
        evenvals = []
        for x in odds:
            if x % 2 == 1:
                oddvals.append(x)
            else:
                evenvals.append(x)
 
        if len(evenvals) > 0 and len(oddvals) > 0:
 
            missingSum = evenvals[0] if len(evenvals) == 1 else oddvals[0]
 
        else:
 
            b = getPalindrome(odds, n + 2)
            bSums = getSubarraySums(b)
            y = bSums[-1]
            x = getLargestExcluded(bSums, subarraySums)
            missingSum = 2 * x - y
    
    else:
        
        b = getPalindrome(odds, n - 2)
        bSums = getSubarraySums(b)
        y = bSums[-1]
        x = getLargestExcluded(subarraySums, bSums)
        missingSum = 2 * x - y
 
    odds.append(missingSum)
    odds.sort()
    odds = getOddOccurringElements(odds)
    
    ans = getPalindrome(odds, n)
    print(*ans)