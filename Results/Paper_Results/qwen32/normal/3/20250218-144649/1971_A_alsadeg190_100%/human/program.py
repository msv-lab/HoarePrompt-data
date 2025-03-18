x = int(input())
 
for i in range(x):
    x , y = list(map(int, input().split()))
    if x < y : print(x , y)
    else: print(y , x)