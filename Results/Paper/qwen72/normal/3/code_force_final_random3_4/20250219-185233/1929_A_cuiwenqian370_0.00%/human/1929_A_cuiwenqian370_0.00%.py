def max_beauty_of_array(n, arr):
    arr.sort()
    # Create a new array with largest and smallest elements alternating
    new_arr = []
    left = 0
    right = n - 1
    while left <= right:
        if left == right:
            new_arr.append(arr[left])
        else:
            new_arr.append(arr[right])
            new_arr.append(arr[left])
        left += 1
        right -= 1
    
    # Calculate the sum of absolute differences
    max_beauty = 0
    for i in range(1, n):
        max_beauty += abs(new_arr[i] - new_arr[i - 1])
    
    return max_beauty
 
# Read number of test cases
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = max_beauty_of_array(n, arr)
    results.append(result)
 
for result in results:
    print(result)