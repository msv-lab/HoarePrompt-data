t = int(input())
 
for i in range(t):
    n = int(input())
    print("1 1")
    print("1 2")
    if n == 3:
        print("2 3")
    elif n >= 4:
        print("2 4")
        for j in range(4, n+1):
            print(str(j) + " " + str(j))