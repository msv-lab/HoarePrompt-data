n=int(raw_input())
a=map(int,raw_input().split())
maxa=max(a)
cmaxa=a.count(maxa)
ca=[0]*(maxa+1)
for i in xrange(n):
    ca[a[i]]+=1
if maxa%2==1:
    l=maxa/2+1
    if a.count(l)==2:
        for i in xrange(n):
            if a[i]<l:
                print("Impossible")
                exit()
        for i in xrange(l+1,maxa+1):
            if ca[i]<2:
                print("Impossible")
                exit()
        print("Possible")
    else:
        print("Impossible")
else:
    l=maxa/2
    if a.count(l)==1:
        for i in xrange(n):
            if a[i]<l:
                print("Impossible")
                exit()
        for i in xrange(l+1,maxa+1):
            if ca[i]<2:
                print("Impossible")
                exit()
        print("Possible")
    else:
        print("Impossible")