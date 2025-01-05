import numpy as np

a=raw_input()

b=[]
for k in range(len(a)):
    b.append(a[k])

b=np.array(b)

alp='abcdefghijklmnopqrstuvwxyz'

al=[]
for k in range(len(alp)):
    al.append(alp[k])

res=[]
for aa in al:
    if aa in b:
        res.append(np.where(b==aa))

m=[]
for k in range(len(res)):
    zz=np.hstack([np.array([0]),res[k][0],np.array([len(a)])])
    z=np.diff(zz)
    
    if len(z)>0:
        m.append(np.max(z))
if len(m)>0:
    ans=np.min(m)
else:
    ans=len(a)

ans-=1

print(ans)