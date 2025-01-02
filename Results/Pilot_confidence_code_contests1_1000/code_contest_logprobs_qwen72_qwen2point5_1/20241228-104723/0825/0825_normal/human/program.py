from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int,stdin.readline().split()))
    b = sorted(a)
    c = [[0,0] for i in range(100005)]
    for i in range(n):
        c[a[i]][i%2]+=1
        c[b[i]][i%2]-=1
    check = True
    for i in range(n):
        if c[a[i]][0]==0 and c[a[i]][1]==0:
            check = False
        else:
            check = True
            break
    if not check:
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")