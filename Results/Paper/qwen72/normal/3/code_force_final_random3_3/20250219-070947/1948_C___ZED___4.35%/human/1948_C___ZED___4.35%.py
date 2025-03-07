for i in range(int(input())):
    n=int(input())
    a=input()
    b=input()
    if b[-2]!=">":
        print("NO")
    elif n==1:
        print("YES")
    else:
        no_path=True
        for k in range(0,n,2):
            
            if b[k]!=">":
                no_path=False
        if not no_path:
            no_path=True
            for k in range(1,n-1,2):
                print(k)
                if a[k]!=">":
                    no_path=False
        if no_path:
            print("YES")
        else:
            print("NO")