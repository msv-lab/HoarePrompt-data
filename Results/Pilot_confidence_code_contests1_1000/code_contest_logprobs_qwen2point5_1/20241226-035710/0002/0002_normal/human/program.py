q = int(raw_input())
for i in range(q):
    l,r,d = raw_input().split(' ')
    l = int(l)
    r = int(r)
    d = int(d)
    if d < l or d > r:
        print(d)
    else:
        ost = r // d
        print(d*(ost+1))