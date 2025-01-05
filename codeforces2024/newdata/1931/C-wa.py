iinp = lambda: int(input())
uinp = lambda: [int(i) for i in input().split()]
 
 
def solve():
    n = iinp()
    l = uinp()
    freq = {}
    for i in l:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
 
 
    fl = []
    for i in freq:
        if(freq[i]>=2):
            fl.append(i)
            freq[i] //=2
 
 
    su =0
    for i in fl:
        su+=freq[i]
    if(su<4):
        print("NO")
        return
 
 
 
    fl.sort()
    shortlist= []
    a,b,c,d = 0,0,0,0
    if(freq[fl[0]]>1):
        a = fl[0]
        b = fl[0]
    else:
        a = fl[0]
        b = fl[1]
 
 
    if(freq[fl[-1]]>1):
        d = fl[-1]
        c = fl[-1]
    else:
        d= fl[-1]
        c = fl[-2]
 
    if((d-a)*(c-b) > (d-b)*(c-a)):
        print("YES")
        print(a,b,d,c , d,b,a,c)
    else:
        print("YES")
        print(b, a, d, c, d, a, b, c)
 
 
 
for _ in range(iinp()):
    solve()