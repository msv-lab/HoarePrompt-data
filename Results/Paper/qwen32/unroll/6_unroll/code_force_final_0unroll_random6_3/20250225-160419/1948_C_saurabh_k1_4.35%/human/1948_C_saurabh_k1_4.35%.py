for _ in range(int(input())):
    n = int(input())
    a = list(map(str , input()))
    b = list(map(str , input()))
     
    if b[n-2] == str("<"):
        print("No")
    else:
        print("Yes")