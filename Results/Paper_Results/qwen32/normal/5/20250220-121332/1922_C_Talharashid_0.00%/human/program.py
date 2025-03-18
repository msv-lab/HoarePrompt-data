from collections import defaultdict
t=int(input())
for i in range(t):
    d1=defaultdict(int)
    d2=defaultdict(int)
    n=int(input())
    lst=list(map(int,input().split()))
    start=0;end=len(lst)-1;inc=1;s=0
    while start!=end:
        mini=11111111
        if (start+1)<len(lst):
            mini=min(abs(lst[start]-lst[start+1]),mini)
        if (start-1)>-1:
            mini=min(abs(lst[start]-lst[start-1]),mini)
        if mini==abs(lst[start]-lst[start+inc]):
            s+=1
        else:
            s+=abs(lst[start]-lst[start+inc])
        start+=inc
        d1[start]=s
    start=len(lst)-1;end=0;inc=-1;s=0
    while start!=end:
        mini=11111111
        if (start+1)<len(lst):
            mini=min(abs(lst[start]-lst[start+1]),mini)
        if (start-1)>-1:
            mini=min(abs(lst[start]-lst[start-1]),mini)
        if mini==abs(lst[start]-lst[start+inc]):
            s+=1
        else:
            s+=abs(lst[start]-lst[start+inc])
        start+=inc
        d2[start]=s
    m=int(input())
    for i in range(m):
        start,end=map(int,input().split())
        start-=1;
        end-=1
        s=0
        if start<end:
            s1=abs(d1[end]-d1[start])
            s2=abs(d2[start]-d2[end])
        else:
            s1=abs(d2[end]-d2[start])
            s2=abs(d1[start]-d1[end])
        print(min(s1,s2))