def is_Monotonic(arr):
    increasing = decreasing = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            increasing = False
        if arr[i] < arr[i + 1]:
            decreasing = False
            
    return increasing or decreasing
