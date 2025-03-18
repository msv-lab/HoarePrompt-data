t = int(input())
for i in range(t):   
    s = input() 
    a = int(list(s.split())[0])
    b = int(list(s.split())[1])
    
    if (a+b)%2==0:
        print("Bob")
    else:
        print("Alice")