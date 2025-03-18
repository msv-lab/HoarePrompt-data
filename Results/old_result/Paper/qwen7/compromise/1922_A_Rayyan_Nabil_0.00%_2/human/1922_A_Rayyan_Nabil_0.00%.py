t = int(input())
 
l = "YES"
 
for i in range(t):
    n = int(input())
    a = input()
    b = input()
    c = input()
 
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            l = "YES"
    else: l = "NO"
 
    print(l)