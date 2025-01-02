import math
def length(x1,y1,x2,y2):
    return sqrt(pow((x2-x1),2.0)+pow((y2-y1),2.0))

    t=0;
    n=input()
    k=input()
    x=input()
    y=input()
    n=n-1
    for i in range(0,n):
        z=input()
        l=input()
        t+=(length(x,y,z,l))
        x=z 
        y=l
    
    print (t*k)/50.0