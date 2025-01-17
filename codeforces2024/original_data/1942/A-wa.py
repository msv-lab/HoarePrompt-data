for i in range(int(input())):
    n,k=[int(x) for x in input().split(" ")]
    s = "1"
    if k==0 and n>2:
        for j in range(2,n+1):
            s = str(j) + " " + s
    elif k==1:
        for j in range(n-2):
            s = s + " 1"
        s = s + " 2"
    elif k==n:
        for j in range(n-1):
            s = s + " 1"
    else:
        s = "-1"
    print(s)