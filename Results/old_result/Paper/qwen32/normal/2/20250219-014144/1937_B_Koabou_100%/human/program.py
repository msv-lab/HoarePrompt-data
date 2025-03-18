def solve():
    a = []
    n = int(input())
 
    for _ in range(2):
        a.append(input())
 
    s = []
    x = 0
    y = 0
    for i in range(n-1):
        if a[0][i+1] == '0' and a[1][i] == '1':
            y = i
        if a[0][i+1] == '1' and a[1][i] == '0':
            s = a[0][:i+1:] + a[1][i::]
            x = i
            break
    else:
        s = a[0] + a[1][n-1]
        x = n-1
 
    t = 1
 
    for i in range(y, x):
        if a[1][i:x:] == s[i+1:x+1:]:
            t = x-i+1
            break
 
    print(s, sep="")
    print(t)
 
for _ in range(int(input())):
    solve()