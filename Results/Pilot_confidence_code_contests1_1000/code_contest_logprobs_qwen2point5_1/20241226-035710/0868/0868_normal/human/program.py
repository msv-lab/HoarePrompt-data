from sys import stdin,stdout
from collections import defaultdict
def make_set(a):
    parent[a] = a
    rank[a] = 1

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    parentA = find(a)
    parentB = find(b)
    if parentA == parentB: return
    if rank[parentA] < rank[parentB]:
        parent[parentA] = parentB
        rank[parentB] += rank[parentA]
    else:
        parent[parentB] = parentA
        rank[parentA] += rank[parentB]

falantes,parent,rank,zeros = defaultdict(list),{},{},0
n,m = map(int,stdin.readline().split())

for i in xrange(1,n+1):
    linguas = stdin.readline().strip().split()
    if linguas[0] == '0': zeros += 1
    for j in linguas[1:]:
        falantes[j].append(i)
    make_set(i)
for i in falantes.values():
    for j in xrange(len(i)-1):
        union(i[j],i[j+1])
for filho in parent:
    parent[filho] = find(parent[filho])

if zeros != n:
    stdout.write(str(len(set(parent.values())) - 1))
else: stdout.write(str(len(set(parent.values())) + 1 - 1))