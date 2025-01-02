import math
input = raw_input

def score(s):
    n = len(s)
    ans = 0
    for i in range(n):
        if s[i] == "L" and i >= 1 and s[i-1] == "L":
            ans += 1
        elif s[i] == "R" and i <= n-2 and s[i+1] =="R":
            ans += 1
    return ans

N,K = map(int, input().split(" "))
S = list(input())

if S=="RL":
    print(0)
    exit()
if S=="LR":
    print(0)
    exit()
if S=="RLR" or S=="LRL":
    if K == 1:
        print(1)
        exit()
    else:
        print(2)
        exit()

s = score(S)
k = 0
lr = 0
rl = 0
for i in range(N-1):
    if S[i] == "L" and S[i+1] =="R":
        lr += 1
    if S[i] == "R" and S[i+1] =="L":
        rl += 1
lrl = 0
rlr = 0
for i in range(N-2):
    if S[i] == "L" and S[i+1] =="R" and S[i+2] =="L":
        lrl += 1
    if S[i] == "R" and S[i+1] =="L" and S[i+2] =="R":
        rlr += 1

if (lrl == 1 and rl == 1 and lr == 1) or (rlr == 1 and rl == 1 and lr == 1):
    if K >= 2:
        print(s+2)
        exit()
    elif K == 1:
        print(s+1)
        exit()
    else:
        print(s)
        exit()

#print(s)
#print(lr, rl)
c = min(K, lr, rl)
s += 2 * c
if K > min(lr, rl):
    if S[0] == "L" and rl > lr:
        s += 1
    elif S[-1] == "R" and rl < lr:
        s += 1
print(s)
