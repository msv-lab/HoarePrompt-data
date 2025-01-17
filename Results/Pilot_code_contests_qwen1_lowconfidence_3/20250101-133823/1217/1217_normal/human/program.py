n = int(raw_input())
a = map(int, raw_input().split())

graph = [[] for _ in range(n)]

for i in xrange(n - 1):
    x, y = map(int, raw_input().split())
    x -= 1; y -= 1
#    print(x, y)
    graph[x].append(y)
    graph[y].append(x)
#    graph
#    a[i] = int(raw_input())
    
#n, k = map(int, raw_input().split())
#s = str(raw_input())

#a = map(int, raw_input().split())
#b = [(y,x) for x,y in enumerate(map(int,raw_input().split()))]

class Info:
    def __init__(self):
        self.gcd = 0
        self.tor1 = 0
        self.ifr1 = 0
        self.tor2 = 0
        self.ifr2 = 0

    def get(self):
        r = self.gcd
        if self.ifr1 > r:
            r = self.ifr1
        if self.ifr2 > r:
            r = self.ifr2
        return r

visited = [False] * n

gcdinfo = [Info() for _ in xrange(n)]

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def dfs(n, parent):
    if visited[n]:
        return
    visited[n] = True
    if parent != -1:
        newgcd = gcd(gcdinfo[parent].gcd, a[n])
#        print("newgcd=", newgcd)
        gcdinfo[n].gcd = newgcd
        if newgcd < gcdinfo[parent].gcd:
            # try removing self
            gcdinfo[n].tor1 = a[n]
            gcdinfo[n].ifr1 = gcdinfo[parent].gcd
            if gcdinfo[parent].ifr1 == 0:
                # alternative option
                gcdinfo[n].tor2 = gcdinfo[parent].gcd
                gcdinfo[n].ifr2 = a[n]
        else:
            # self if good, keep one of the other candidates
            if gcdinfo[parent].ifr1:
                newgcd1 = gcd(gcdinfo[parent].ifr1, a[n])
            else:
                newgcd1 = 1
            if gcdinfo[parent].ifr2:
                newgcd2 = gcd(gcdinfo[parent].ifr2, a[n])
            else:
                newgcd2 = 1
            if newgcd1 > newgcd2:
                gcdinfo[n].tor1 = gcdinfo[parent].tor1
                gcdinfo[n].ifr1 = gcdinfo[parent].ifr1
            elif newgcd2 > newgcd1:
                gcdinfo[n].tor1 = gcdinfo[parent].tor2
                gcdinfo[n].ifr1 = gcdinfo[parent].ifr2               

    for neigh in graph[n]:
        dfs(neigh, n)

gcdinfo[0].gcd = a[0]
gcdinfo[0].tor1 = a[0]
gcdinfo[0].ifr1 = 0
dfs(0, -1)

s = ""
for i in xrange(n):
    s += str(gcdinfo[i].get()) + " "
print(s)
    
