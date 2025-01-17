# Reading input
n, k = map(int, input().split())

# If there are no inhabited apartments, no apartment can be good
if k == 0:
    print(0, 0)
else:
    # The minimum number of good apartments
    min_good = 1 if n != k else 0
    
    # The maximum number of good apartments
    max_good = min(2 * k, n - k)
    
    print(min_good, max_good)
