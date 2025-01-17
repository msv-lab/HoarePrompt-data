import math

t = int(input()) 
results = []
for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split())) 
    a.sort() 
    median_index = (n - 1) // 2  
    median = a[median_index]
    operations = 0
    for i in range(median_index, n): 
        if a[i] < median + 1:
            operations += (median + 1 - a[i])
    results.append(operations)
print("\n".join(map(str, results)))