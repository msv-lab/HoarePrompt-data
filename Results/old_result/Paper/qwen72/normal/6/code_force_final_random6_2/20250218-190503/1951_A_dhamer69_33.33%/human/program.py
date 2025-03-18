t=int(input())
while(t>0):
    n=int(input())
    s=input()
    if n==2:
        if s=="00":
            print("YES")
        else:
            print("NO")
    else:
        count_1=s.count("1")
        if count_1%2!=0:
            print("NO")
        else:
            if s.count("11")==1:
                print("NO")
            else:
                print("YES")
    t-=1