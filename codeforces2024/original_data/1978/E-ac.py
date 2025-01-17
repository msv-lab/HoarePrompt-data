def solution():
    def f(i):
        return int(a[i] == 0 and (((i-1 >= 0 and b[i-1] == 1) or (i-2 >= 0 and a[i-2] == 0)) and ((i+1 < n and b[i+1] == 1) or i+2 < n and a[i+2] == 0)))
 
    n = int(input())
    a = list(map(int, list(input())))
    b = list(map(int, list(input())))
    q = int(input())
    l_r = [list(map(lambda x: int(x)-1, input().split()))for _ in range(q)]
    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i]+(a[i]+f(i))
    result = [(prefix[r+1]-prefix[l])-sum(i == l or (i == l+1 and b[l] == 0) or (i == r-1 and b[r] == 0) or i == r for i in {l, l+1, r-1, r} if l <= i <= r and f(i)) for l, r in l_r]
    return "\n".join(map(str, result))
 
for _ in range(int(input())):
    print(solution())