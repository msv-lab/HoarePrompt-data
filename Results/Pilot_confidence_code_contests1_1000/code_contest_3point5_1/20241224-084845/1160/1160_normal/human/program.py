from math import *


n = int(raw_input())
m = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    if i%2 == 0:
        for j in range(n):
            m[j][(i+j)%n] = i
    else:
        for j in range(n):
            m[j][(i-j)%n] = i
for i in range(n):
    s = ''
    for j in range(n):
        s += ' ' + str(m[i][j])
    print(s[1:])
        



"""from math import *
from Queue import *

def bfs(G, start):
    visited = set([start])
    Q = Queue()
    Ret = [start]
    Q.put(start)
    while not Q.empty():
        vertex = Q.get()
        for v in G[1][vertex]:
            if v not in visited:
                Q.put(v)
                visited.add(v)
                Ret.append(v)
    return Ret

def longest_path(G):
    l = bfs(G,G[0][0])
    marked = set()
    result = dict()
    for i in l:
        result[i] = [0,i,0,i]
    for i in range(len(l)-1, -1, -1):
        for j in G[1][l[i]]:
            if j in marked:
                if (result[j][2] > result[l[i]][2]) or ((result[j][2] == result[l[i]][2]) and (result[j][3] < result[l[i]][3])):
                    result[l[i]][2] = result[j][2]
                    result[l[i]][3] = result[j][3]
                if (result[l[i]][0] + result[j][0] + 1 > result[l[i]][2]):
                    result[l[i]][2] = result[l[i]][0] + result[j][0] + 1
                    result[l[i]][3] = min(result[l[i]][1], result[j][1])
                if ((result[l[i]][0] + result[j][0] + 1 == result[l[i]][2]) and (min(result[l[i]][1],result[j][1]) < result[l[i]][3])):
                    result[l[i]][3] = min(result[l[i]][1],result[j][1])
                if (result[j][0] + 1 > result[l[i]][0]) or ((result[j][0] + 1 == result[l[i]][0]) and (result[j][1] < result[l[i]][1])):
                    result[l[i]][0] = result[j][0] + 1
                    result[l[i]][1] = result[j][1]
        marked.add(l[i])
    return (result[l[0]][2], result[l[0]][3])

def remove(G,v):
    ver = G[0]
    ver.remove(v)
    edg = dict()
    for i in ver:
        nb = []
        for j in G[1][i]:
            if j != v:
                nb.append(j)
        edg[i] = nb
    return (ver, edg)

def harvest(G,M):
    l = bfs(G,M[0])
    seen = set()
    delete = []
    for i in range(len(l)-1, -1, -1):
        seen.add(l[i])
        if l[i] in M:
            for j in G[1][l[i]]:
                if j not in seen:
                    M.append(j)
        if l[i] not in M:
            delete.append(l[i])
    for i in delete:
        G = remove(G,i)
    return G

s = raw_input()
l = s.split(' ')
n = int(l[0])
m = int(l[1])
V = []
Adj = [[] for i in range(n+1)]
for i in range(1,n+1):
    V.append(i)
E = dict()
for i in range(n-1):
    s = raw_input()
    l = s.split(' ')
    h = int(l[0])
    t = int(l[1])
    Adj[h].append(t)
    Adj[t].append(h)
E = dict()
for i in range(1, n+1):
    E[i] = Adj[i]
G = [V,E]
s = raw_input()
l = s.split(' ')
M = []
for i in range(m):
    M.append(int(l[i]))
G = harvest(G,M)
sol = longest_path(G)
print(sol[1])
print(2*len(G[0]) - 2 - sol[0])"""
