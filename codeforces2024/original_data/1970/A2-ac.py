s = input()
p = [[]]
prv = 0
c = 0
cur = 0
for i in range(len(s)):
    if s[i] == '(':
        c += 1
        p[cur].append('(')
    else:
        if prv == 0:
            cur += 1
            p.append([])
            p[cur].append(')')
            prv = c-1
            c = 0
        else:
            prv -= 1
            p[cur].append(')')
 
 
cur = 0
while len(p[cur]) > 0:
    x = p[cur].pop()
    if x == '(':
        cur += 1
    else:
        cur -= 1
    print(x,end="")