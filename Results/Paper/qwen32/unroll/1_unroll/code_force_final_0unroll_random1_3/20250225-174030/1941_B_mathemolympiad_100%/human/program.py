numTest = int(input())
 
for _ in range (0, numTest):
    n = int(input())
    a = [int(x) for x in input().split()]
    stop = False
    for i in range (0, n-2):
        if a[i] < 0:
            print("NO")
            stop = True
            break
        opNum = a[i]
        a[i] -= opNum
        a[i+1] -= 2*opNum
        a[i+2] -= opNum
    if stop == True:
        continue
    if a[len(a)-1]!=0 or a[len(a)-2]!=0:
        print("NO")
    else:
        print("YES")