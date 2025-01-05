x=int(input())
m1=[1,3,5,6,10]
m2=[2,4,7,8,9,11,12,13]
m3=[14]
for i in range(x):
    y=int(input())
    

    if y%15==0:
        print(y/15)
    else:
        if y==5 or y==8:
            print(3)
        elif y%15 in m1:
            print((y//15)+1)
        elif y%15 in m2:
            print((y//15)+2)
        else:
            print((y//15)+3)