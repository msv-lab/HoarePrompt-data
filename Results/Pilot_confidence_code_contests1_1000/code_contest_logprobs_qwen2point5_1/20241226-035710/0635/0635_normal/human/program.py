import sys,math
input=sys.stdin
write=sys.stdout.write
n=int(input.readline())
s=input.readline().split()
A=[int(a) for a in s]
A.sort()
A.append(10**12)
carry=0
num=0
i=0
sum=0
while i<n:
    j=i
    while A[i]==A[j+1]:
        j+=1
    num=j-i+1+carry
#    print num,carry
    k=0
    while num>0 and A[j+1]>k+A[i]:
        sum+=(num%2)
        num=(num-(num%2))//2
        k+=1
    if num>0:
        carry=num
    i=j+1
write(str(sum))
