from __future__ import division,print_function
#from sortedcontainers import SortedList
import sys
#sys.__stdout__.flush()
le=sys.__stdin__.read().split("\n")
le.pop()
le=le[::-1]
n,m,ka=list(map(int,le.pop().split()))
sp=list(map(lambda k:int(k)-1,le.pop().split()))
ar=[[] for k in range(n)]
for k in range(m):
    a,b=list(map(lambda k:int(k)-1,le.pop().split()))
    ar[a].append(b)
    ar[b].append(a)
fil=[0]*n
d1=[n+1]*n
d1[0]=0
tfil=1
for k in range(n-1):
    for i in ar[fil[k]]:
        if d1[i]==n+1:
            d1[i]=d1[fil[k]]+1
            fil[tfil]=i
            tfil+=1
fil=[0]*n
fil[0]=n-1
df=[n+1]*n
df[n-1]=0
tfil=1

for k in range(n-1):
    for i in ar[fil[k]]:
        if df[i]==n+1:
            df[i]=df[fil[k]]+1
            fil[tfil]=i
            tfil+=1
#print(fil)
co=sorted([(d1[k],df[k]) for k in sp])
co=co[::-1]
m1=[0]*(ka)
m2=[0]*(ka)
for k in range(ka):
    m1[k],m2[k]=m1[k-1],m2[k-1]
    if co[k][1]>m2[k]:
        if co[k][1]>m1[k]:
            m1[k],m2[k]=co[k][1],m1[k]
        else:
            m2[k]=co[k][1]
po=ka-1
m=0
"""print(co)
print(m1)
print(m2)"""
for k in range(ka):
    doub=co[k][1]
    #print(m1[po],m2[po],co[k][0],co[po][0])
    while po>0 and (m1[po] if (po<k or (m1[po]!=doub)) else m2[po])+co[k][0]<co[k][1]+co[po][0]:
        po-=1
    ma=min((m1[po] if po<k or (m1[po]!=doub) else m2[po])+co[k][0],co[k][1]+co[po][0])
    #print(ma,'ar')
    #print(po)
    if po!=ka-1:
        po+=1
    #print(min((m1[po] if po<k or (m1[po]!=doub) else m2[po])+co[k][0],co[k][1]+co[po][0]))
    ma=max(ma,min((m1[po] if po<k or (m1[po]!=doub) else m2[po])+co[k][0],co[k][1]+co[po][0]))
    m=max(m,ma)

if False:
    """print(df)
    print(d1)
    m11=0
    m12=0
    mf1=0
    mf2=0
    for k in sp:
        if d1[k]>m12:
            if d1[k]>m11:
                m11,m12=d1[k],m11
            else:
                m12=d1[k]
        if df[k]>mf2:
            if df[k]>mf1:
                mf1,mf2=df[k],mf1
            else:
                mf2=df[k]
    print(m11,m12,mf1,mf2)
    m=0
    for k in sp:
        mf=mf1 if df[k]!=mf1 else mf2
        m1=m11 if d1[k]!=m11 else m12
        print(k,d1[k]+mf,df[k]+m1,d1[k],mf,df[k],m1)
        m=max(min(d1[k]+mf,df[k]+m1),m)"""
print(min(m+1,d1[-1]))
