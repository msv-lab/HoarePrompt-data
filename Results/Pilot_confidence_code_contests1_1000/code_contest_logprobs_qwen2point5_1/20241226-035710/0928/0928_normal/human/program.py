n,m=map(int,raw_input().split())
count=0
lens=0
founder=[]
arr=[]
for i in range(n):

    row=list(raw_input())
    found=False

    for j in range(m):
        if row[j]=='B':
            arr.append(j)

            count+=1
            found=True

    if found==True:
            founder.append(i)

#founder=set(founder)
if len(arr)!=0:
        length=max(arr)-min(arr)
else:
        length=0
if length>lens:
        lens=length



if lens==0 and len(founder)==0:
    print(1)
else:
    x=lens+1
    y=founder[-1]-founder[0]+1

    ans=max(x,y)**2-count
    if max(x,y)**2 > n*m:
        print(-1)
    else:
        print(ans)

