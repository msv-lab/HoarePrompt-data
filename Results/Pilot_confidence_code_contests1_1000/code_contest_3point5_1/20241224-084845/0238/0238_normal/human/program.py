import sys
a=map(int,raw_input().split())
n=a[0]
x=float(a[1])
y=float(a[2])
monstor=[]
for i in xrange(0,n):
    monstor.append(int(raw_input()))
MaxMonstor=max(monstor)
order=[]
x_pointer=1/x
y_pointer=1/y
i=0

while(i<MaxMonstor):
    if(x_pointer==y_pointer):
        order.append("Both")
        order.append("Both")
        x_pointer=x_pointer+1/x
        y_pointer=y_pointer+1/y
        i=i+2
        continue
    if(x_pointer<y_pointer):
        order.append("Vanya")
        x_pointer=x_pointer+1/x
        i=i+1
    if(x_pointer>y_pointer):
        order.append("Vova")
        y_pointer=y_pointer+1/y
        i=i+1
        
for i in xrange(0,n):
    print(order[monstor[i]-1])
    
