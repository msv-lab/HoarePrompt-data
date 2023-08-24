n, k = map(int, input().split())
a = list(map(int, input().split()))

min_val = min(a)
max_val = max(a)

if k == 0:
    print(max_val - min_val)
else:
    min_diff = max_val - min_val
    
    if min_diff > k:
        print(min_diff - k)
    else:
        print(0)