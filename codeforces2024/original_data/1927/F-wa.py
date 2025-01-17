import sys
input = sys.stdin.readline
from collections import *

t = 0

def find(n) :
    D = []
    while U[n] != n : D.append(n) ; n = U[n]
    for num in D : U[num] = n

    return n


for _ in range(int(input())) :
    N, M = map(int,input().split()) ; U = [i for i in range(1+N)]
    Dic = [[] for _ in range(1+N)] ; A = []
    
    t += 1

    for _ in range(M) :
        a, b, c = map(int,input().split()) ; A.append((a, b, c))
        
        if t == 10:
            print(a, b, c, end=" ")
        
        Dic[a].append(b) ; Dic[b].append(a)

    A.sort(key = lambda x : x[2])

    while A :
        a, b, c = A.pop() ; p, q = find(a), find(b)

        if p == q : x, y, z = a, b, c
        elif p > q : U[p] = q
        else : U[q] = p

    V = [0] * (1+N) ; Dic[y].remove(x) ; D = deque() ; D.append(y) ; V[y] = 1

    while D :
        n = D.popleft()
        if n == x : break

        for num in Dic[n] :
            if V[num] == 0 : V[num] = V[n]+1 ; D.append(num)

    Ans = [x]

    while Ans[-1] != y :
        n = Ans[-1]

        for num in Dic[n] :
            if V[num] == V[n]-1 : Ans.append(num) ; break

    print(z, len(Ans)) ; print(*Ans)