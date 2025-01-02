import numpy as np
n = int(input())
SP=[]
SPs=[]
for i in range(n):
    SP=[i]
    for j in input().split():
        
        SP.append(j)
    SPs.append(SP)

SPs=np.array(SPs)
SPs2=SPs[SPs[:,2].astype(int).argsort()[::-1],:]
SPs3=SPs2[SPs2[:,1].argsort(),:][:,0]

for i in range(n):
    print(int(SPs3[i])+1)
