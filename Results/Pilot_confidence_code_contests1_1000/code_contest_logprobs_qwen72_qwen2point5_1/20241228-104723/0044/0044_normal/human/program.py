def trace(a,n) :
    li=[]
    for i in xrange(n):
        li.append(str(a[i]))
    print(" ".join(li))
    
def selectionsort(a,n):
    ct=0
    for i in xrange(n):
        if i==n-1:
            break
        else :
            mini=i
            for j in xrange(i,n,1):
                if a[j]<a[mini]:
                    mini=j
            if i!=mini:
                keep=a[i]
                a[i]=a[mini]
                a[mini]=keep
                ct+=1
    return ct
            
            
n=input()
a=map(int,raw_input().split())
ct=selectionsort(a,n)
trace(a,n)
print(ct)
                