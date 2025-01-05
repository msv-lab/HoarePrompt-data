from collections import deque 
from sys import stdin
a=raw_input()
b=raw_input()
i=0 
j=0 
allen=len(a)
bllen=len(b)
while i<allen and a[i]=='0' : i+=1 
while j<bllen  and b[j]=='0': j+=1 

alen=allen-i 
blen=bllen-j 
#print(alen,blen)
m=min(alen,blen)
def cmp(a,b,i,j):
    #print(alen,blen)
    if alen>blen:
        return '>'
    elif alen<blen:
        return '<'
    while i<allen and j<bllen:
        if a[i]<b[j]:
            return '<'
        elif a[i]>b[j]:
            return '>'
        i+=1 
        j+=1 
    return '='
#print(a,b)
print(cmp(a,b,i,j))