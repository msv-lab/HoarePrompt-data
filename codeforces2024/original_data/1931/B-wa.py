t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int , input().split()))
    sum1 = 0
    sum2 = (sum(arr))//2
    sm3  = sum(arr)//n
    if n==1 or sum(arr)==0:
        print("yes")
        continue
    
    for i in range(n//2):
        sum1+=arr[i]
 
    if sum1>sum2 and arr[0]>sm3 and arr[n-1]<=sm3:
        print("yes")
    else:
        print("no")
