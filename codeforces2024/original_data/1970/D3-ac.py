n = int(input())
 
w = []
q = {}
i = -1
 
def f(a,b):
    return (a+2)*(b+4)-1 if a >= b else (a+5)*(b+1)-1
 
while len(w) < n:
    i += 1
    if f(i,i) in q:
        continue
    if any(f(i,j) in q for j in w):
        continue
    if any(f(j,i) in q for j in w):
        continue
    q1 = {f(i,i): (len(w),len(w))}
    ok = True
    for r,j in enumerate(w):
        v = f(i,j)
        if v in q1:
            ok = False
            break
        q1[v] = len(w),r
    if not ok:
        continue
    for r,j in enumerate(w):
        v = f(j,i)
        if v in q1:
            ok = False
            break
        q1[v] = r,len(w)
    if not ok:
        continue
    q.update(q1)
    w.append(i)
 
for i in w:
    print("XO"+i*"X")
    
t = int(input())
for _ in range(t):
    x = int(input())
    u,v = q[x]
    print(u+1, v+1)
    