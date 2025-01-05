from collections import defaultdict
#n = int(raw_input())
n,b = [int(x) for x in raw_input().split()]
#arr = [int(x) for x in raw_input().split()]

s = 0
d_osn = defaultdict(int)
cur = 2
while b > 1:
    if b % cur == 0:
        d_osn[cur] += 1
        b /= cur
        continue
    else:
        if cur == 2:
            cur = 3
        else:
            cur += 2
    if cur >= b ** (0.5) :
        break
if b > 2:
    d_osn[b] += 1
izv = defaultdict(int)

res = -1
for k in d_osn:
    izv = 0
    newk = k
    newn = n
    i = 0
    while True and i < 10:
        st = 0
        i += 1
        newizv = 0
        newnewk = newk
        while newnewk <= newn:
            newnewk *= newk
            st += 1
        if st == 0:
            break
        for i in range(st):
            newizv = newizv * 2 + 1
        while newn > newk ** st:
            izv += newizv
            newn = newn - newk ** st
    mlt = izv // d_osn[k]
    if res == -1:
        res = mlt
    elif mlt < res:
        res = mlt
print(res)