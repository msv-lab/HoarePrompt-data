from collections import Counter
 
def solve(n, m, nums):
    if n == 1: return 'Sasha' if len(str(min(n, int(str(n)[::-1]))))>=m+1 else 'Anna'
    
    def zerocnts(num):
        num = str(num)
        tot = 0
        for i in range(len(num)-1,-1,-1):
            if num[i] != '0': break
            tot += 1
        return tot
    
    tot = sum(len(val) for val in map(str, nums))
    cntvals = sorted((zerocnts(val) for val in nums), reverse=True)
    for i in range(0, len(cntvals), 2): tot -= cntvals[i]
    
    # print(cntvals, tot)
    
    return 'Sasha' if tot >= m+1 else 'Anna'
 
for _ in range(int(input())):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    
    print(solve(n, m, nums))