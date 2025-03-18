def max_points(a, n):
    count_a = {}
    for num in a:
        if num in count_a:
            count_a[num] += 1
        else:
            count_a[num] = 1
 
    # Maximum points you can gain
    max_score = 0
    
    # Iterate over the card numbers to count how many "safe" points you can get
    for num in range(1, n + 1):
        if num in count_a:
            # If you have the number and it appears more than once, you can guarantee a point
            if count_a[num] == 2:
                max_score += 1
    
    return max_score
 
# Process input cases
t = int(input())
results = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = max_points(a, n)
    results.append(result)
 
# Output all results
for res in results:
    print(res)