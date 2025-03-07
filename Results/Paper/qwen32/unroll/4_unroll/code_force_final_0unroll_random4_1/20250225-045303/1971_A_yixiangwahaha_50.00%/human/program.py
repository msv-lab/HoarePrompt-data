t=input()
x = []
y = []
for i in range(10):
    xylist = input().split(" ")
    x.append(int(xylist[0]))
    y.append(int(xylist[1]))
 
for i in range(10):
    if x[i] < y[i]:
        print(x[i], " ", y[i])
    else:
        print(y[i], " ", x[i])