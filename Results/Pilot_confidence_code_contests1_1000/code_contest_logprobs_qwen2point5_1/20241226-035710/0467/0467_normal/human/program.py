N = input()
a = []
a.append(map(int, raw_input().split()))

a=a[0]

c=[0,0,0,0,0,0,0,0]

free=0

for i in a:
    if 1<=i and i<=399:
        c[0]=1
    elif 400<=i and i<=799:
        c[1]=1
    elif 800<=i and i<=1199:
        c[2]=1
    elif 1200<=i and i<=1599:
        c[3]=1
    elif 1600<=i and i<=1999:
        c[4]=1
    elif 2000<=i and i<=2399:
        c[5]=1
    elif 2400<=i and i<=2799:
        c[6]=1
    elif 2800<=i and i<=3199:
        c[7]=1
    elif 3200<=i:
        free+=1

ma=sum(c)+free



mi=sum(c)
if mi<1:
    mi=1


print(str(mi) + " " + str(ma))