import os
import Queue

n = 0
k = 0
t = 0
P = {}
Q = Queue.PriorityQueue()
M = []

def solve():
    # read data
    global n, k, t, P
    read = reader()
    n, k, t = list(map(int, next(read).split()))
    t -= 1
    if t == 0:
        print(0)
        return
    for i in range(n):
        P[i] = []
    for i in range(k):
        m = tuple(map(int, next(read).split()))
        m = (m[0] - 1, m[1] - 1, m[2])
        M.append(m)
        Q.put((m[2], m, [set(), set()]))
    
    # solve
    step = 0
    points = -1
    print("{0}: {1} {2} {3}".format(1, 0, (-1, -1, 0), ()))
    while not Q.empty():
        step += 1
        if step >= t:
            break
        points, m, used = Q.get()
        print("{0}: {1} {2} {3}".format(step+1, points, m, used))
        usedA, usedB = set(used[0]), set(used[1])
        usedA.add(m[0])
        usedB.add(m[1])
        for possibleM in M:
            if possibleM[0] in usedA or possibleM[1] in usedB or possibleM > m:
                continue
            Q.put((points + possibleM[2], possibleM, [usedA, usedB]))
    print(points)
    

def reader():
    if False:
        with open("F.in", "r") as fin:
            while True:
                yield next(fin)
    else:
        try: input = raw_input
        except: pass
        while True:
            yield input()

solve()