for _ in range(int(input())):
    a=int(input())
    b=input()
    c=str(b[-1::-1])
    if c.count("B")>1:
        print(a-c.index("B")-b.index("B"))
    else:
        print(a)
