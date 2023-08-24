n, m = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(m):
    l, r = map(int, input().split())
    subsegment = a[l-1:r]
    
    # Check if subsegment is non-decreasing
    if subsegment == sorted(subsegment):
        print("Yes")
    # Check if subsegment is non-increasing
    elif subsegment == sorted(subsegment, reverse=True):
        print("Yes")
    # Check if subsegment is a ladder
    else:
        print("No")