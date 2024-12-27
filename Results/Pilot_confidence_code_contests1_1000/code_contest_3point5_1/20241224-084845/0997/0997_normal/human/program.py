t = int(input())

for i in range(t):
    
    a,b = raw_input().split()
    a =int(a)
    b = int(b)
    c = int(a%b)
    
    if(c==0):
        print("0")
    else:
        print(b-c)