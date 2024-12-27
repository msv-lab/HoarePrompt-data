n = int(raw_input())
a = []
b = map(int,raw_input().split())
j = 0
t=1
while (t==1):
    t=0
    a=b
    b=[]
    j=0
    while (j<(len(a)-1)):
        if a[j]==a[j+1] and t!=1:
            b.append(a[j]+1)
            j+=1
            t=1
        else:
            b.append(a[j])
        j+=1
    
    if j<len(a):
        b.append(a[j])
    #print(b)

st = ''
for bb in b:
    st += str(bb)+' '

print(st)