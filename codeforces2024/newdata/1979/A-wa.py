t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    mini = 0
    maxi = -1
    for i in range(1,n):
        if arr[i] < arr[mini]:
            mini = i
  
    for i in range(mini,-1,-1):
        if arr[i] > arr[mini]:
            maxi = arr[i] - 1
            break
    
    for i in range(mini +1, n):
        if (maxi < 0 or arr[i] < maxi) and arr[i] > arr[mini]:
            maxi = arr[i] - 1
            break
    if maxi < 0:
        maxi = arr[mini] - 1
    print(maxi)