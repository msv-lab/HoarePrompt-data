t = int(input())
 
 
def solve():
    for j in range(n // 2, 0, -1):
        count = 0
        for k in range(0, n - j):
            if s[k] == '?' or s[k + j] == '?' or s[k] == s[k + j]:
                count += 1
            else:
                count = 0
            if count == j:
                print(count * 2)
                return
    return 0
 
for i in range(t):
    s = list(input())
    n = len(s)
 
    solve()