for _ in range (int(input())):
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    x4,y4=map(int,input().split())
    if x1==x2:
        print(abs((y2-y1)*(x3-x1)))
    if x1==x4:
        print(abs((y4-y1)*(x3-x1)))
    if x1==x3:
        print(abs((y3-y1)*(x2-x1)))