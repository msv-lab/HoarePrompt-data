s=raw_input().split()
n=int(s[0])
m=int(s[1])
k=int(s[2])
i=0
rectangular=[]
while i<n:
    x =raw_input()
    rectangular.append(x)
    i=i+1
j=0
while j<m:
    contador=0
    i=1
    while i<n:
        if (j+i)< m and rectangular [i][j+i]=="L":
            contador =contador+1
        if (j-i)>= 0 and rectangular [i][j-i]=="R":
            contador =contador+1
        if (i+i)< n and rectangular [i+i][j]=="U":
             contador =contador+1
        i=i+1
    print (contador)
    j=j+1
