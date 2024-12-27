a,b=map(int, raw_input().split())

f=1
if a<b:
    while a>1:
        f=f*a
        a=a-1
    print(f)
    
else:
    if a>b:
        while b>1:
            f=f*b
            b=b-1
        print(f)# your code goes here