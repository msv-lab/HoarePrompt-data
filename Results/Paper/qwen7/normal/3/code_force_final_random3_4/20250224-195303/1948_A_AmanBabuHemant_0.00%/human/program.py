t = int(input())
 
for _ in range(t):
    n = int(input())
    if n % 2:
        print("NO")
    else:
        s = "110"*(n//2)
        if len(s) < 200:
            print("YES")
            print(s)
        else:
            print("NO")