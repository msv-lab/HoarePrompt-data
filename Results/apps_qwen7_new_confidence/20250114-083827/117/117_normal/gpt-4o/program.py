# Read the input values
l1, r1, l2, r2, k = map(int, input().split())

# Calculate the overlapping interval
start = max(l1, l2)
end = min(r1, r2)

# Determine the number of minutes they can spend together
if start > end:
    print(0)
else:
    overlap = end - start + 1
    if start <= k <= end:
        overlap -= 1
    print(overlap)
