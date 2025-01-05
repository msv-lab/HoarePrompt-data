'''
from collections import Counter
t = int(input())  
for _ in range(t):
    n = int(input())
    ans = 0
    prob = list(map(int,input().split()))
    if len(prob) == 1 or len(prob) == 2:
        print(-1)
        continue

    freq = Counter(prob)
    max_count = max(freq.values())

    if max_count == n:
        print(-1)
        continue
    else:
        yes = True
        while yes == True:
            if prob[0] == prob[-1]:
               prob.pop()
               ans += 1
            else:
               yes = False
        print(ans)
'''
def is_palindrome(s):
    return s == s[::-1]

t = int(input())  
for _ in range(t):
    n, q = map(int, input().split())
    s = input()

    for _ in range(q):
        ans = 0
        l, r = map(int, input().split())
        l -= 1  
        r -= 1  

        for i in range(l, r+1):  
            if not is_palindrome(s[i:r+1]):  
                ans += len(s[i:r+1])  

        print(ans)


