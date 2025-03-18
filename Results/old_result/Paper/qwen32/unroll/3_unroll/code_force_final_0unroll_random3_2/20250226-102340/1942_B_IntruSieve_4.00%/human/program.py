def what_the_mex():
    n = int(input())
    arr = list(map(int , input().split()))
    mex = []
    minn = 0
    maxx = 0
    for i in range(n):
        if arr[i] > 0:
            mex.append(minn)
            minn += 1
            if minn == maxx:
                minn = maxx + 1
        else:
            mex.append(abs(arr[i] - minn))
            if abs(arr[i] - minn)  > maxx:
               maxx = abs(arr[i] - minn)
        
    for itm in mex:
        print(itm , end = ' ')
    print()
 
for _ in range(int(input())):
    what_the_mex()