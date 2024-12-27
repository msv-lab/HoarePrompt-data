vals=[int(x) for x in raw_input().split()]
n=vals[0]
k=vals[1]
a=vals[2]
b=vals[3]

c=0
d=True
if b>a: d=False
s=''

for i in range(n):
    if c==k:
        d = not d
        c=0
    if d:
        s+='G'
        a-=1
        c+=1
        if a < b:
            d=not d
            c=0
    else:
        s+='B'
        b-=1
        c+=1
        if b<a:
            d=not d
            c=0
    if a<0 or b<0:
        print('NO')
        quit()

print(s)
