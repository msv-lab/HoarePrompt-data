import sys
import copy

d=[0,2,5,5,4,5,6,3,7,6]
b=[]

n = map(int, raw_input().split())
a = map(int, raw_input().split())

for x in a:
    b.append(d[x])

def max_num(x, a, b):
    results=[]
    max=0
    for z, y in enumerate(b):
        if x==y:
            results.append([a[z], [a[z]]])
        elif x>y:
            if max_num(x-y, a, b)!=None:
                t=0
                result=max_num(x-y, a, b)
                result[1].append(a[z])
                result[1].sort()
                for num, res in enumerate(result[1]):
                    t+=res*(10**num)
                results.append([t, result[1]])
            else:
                continue
    if results==[]:
        return
    results.sort()
    results.reverse()
    return results[0][0], results[0][1]

def final(x, a, b):
    results=[]
    minimum=a[b.index(min(b))]
    m=1
    t=0
    max=0
    if x%min(b)==0:
        for y in range(x/min(b)):
            results.append(minimum)
        for num, res in enumerate(results):
            t+=res*(10**num)
        return t
    elif x>min(b):
        b_org=copy.deepcopy(b)
        a.pop(b.index(min(b)))
        b.pop(b.index(min(b)))
        while max_num(x%min(b_org)+m*min(b_org), a, b)==None:
            print(x%min(b_org)+m*min(b_org))
            m+=1
            print(m)
        for i in range(4):
            t=0
            result = max_num(x%min(b_org)+(m+i)*min(b_org), a, b)
            results=result[1]
            for y in range(x/min(b_org)-m):
                results.append(minimum)
            results.sort()
            for num, res in enumerate(results):
                t+=res*(10**num)
            if t>max:
                max=t
            return max
    if results==[]:
        return


print(final(n[0], a, b))
