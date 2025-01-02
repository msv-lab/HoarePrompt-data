k=[]
for t in range(int(raw_input())):
    l1=0
    s=""
    p=int(raw_input())
    n=[int(i) for i in raw_input().split()]
    x=n.index(max(n))
    y=n.index(min(n))
    if n[1]<max(n)-min(n):
        l1=2
        s = str(y + 1) + " " + str(l1) + " " + str(x + 1)
        k.append(s)
    else:
        s=-1

        k.append(s)

for t1 in k:
    print(t1)