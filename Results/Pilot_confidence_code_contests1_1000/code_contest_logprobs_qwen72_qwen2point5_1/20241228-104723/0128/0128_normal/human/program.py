n=map(int,str(raw_input()).split(" "))
k=int(raw_input())
modu=pow(10,n[1])
k=k%modu
k=list(str(k))
counter=0
for i in k:
    if(i=="1"):
        counter+=1
if(k[len(k)-n[2]]=="1"):
    counter-=1
else:
    counter+=1
print(counter)
