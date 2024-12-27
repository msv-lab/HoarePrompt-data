import numpy as np

H, W = map(int, raw_input().split())

S = np.zeros((H, W))

for i in range(H):
    tmp = list(raw_input())
    for j in range(W):
        if tmp[j] == "#":
            S[i, j] = 1
        else:
            S[i, j] = 0

an = [-1, 1]
d_flag = 1

for i in range(H):
    for j in range(W):
        if S[i, j] == 1:
            flag = 0
            if i>1:
                a1 = S[i-1, j]
            else:
                a1 = S[i+1, j]
            if j>1:
                a2 = S[i, j-1]
            else:
                a2 = S[i, j+1]
            if i<H-1:
                a3 = S[i+1, j]
            else:
                a3 = S[i-1, j]
            if j>W-1:
                a4 = S[i, j+1]
            else:
                a4 = S[i, j-1]
            if a1+a2+a3+a4 == 0:
                d_flag = 0
                
if d_flag == 1:
    print("Yes")
else:
    print("No")