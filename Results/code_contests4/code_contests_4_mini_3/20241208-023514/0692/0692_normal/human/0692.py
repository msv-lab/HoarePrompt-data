def badDays(arr):
    
    days = 0
    
    for i in range(len(arr)-1):
        for j in range(1, len(arr)):
            
            if arr[i] > arr[j]:
                days += 1
                break
            
            


t = int(raw_input())

for _ in range(t):
    
    n = int(raw_input())
    
    arr = map(int, raw_input().split())
    
    badDays(arr)
    
