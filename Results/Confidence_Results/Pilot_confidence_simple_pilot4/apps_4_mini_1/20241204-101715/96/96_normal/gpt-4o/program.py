# Use Standard Input format

n = int(input())
a = list(map(int, input().split()))

def is_unimodal(arr):
    i = 0
    n = len(arr)
    
    # Increasing phase
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
    
    # Constant phase
    while i + 1 < n and arr[i] == arr[i + 1]:
        i += 1
    
    # Decreasing phase
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
    
    # If we have traversed the entire array, it's unimodal
    return i == n - 1

if is_unimodal(a):
    print("YES")
else:
    print("NO")
