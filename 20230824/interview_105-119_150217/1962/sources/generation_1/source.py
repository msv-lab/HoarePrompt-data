n, k, l = map(int, input().split())
staves = list(map(int, input().split()))

# Sort the staves in ascending order
staves.sort()

# Check if it's possible to construct n barrels with the given staves
if staves[k-1] - staves[0] > l:
    print(0)
else:
    # Find the maximum total sum of volumes
    max_sum = 0
    for i in range(n):
        # Calculate the volume for each barrel in the partition
        volume = staves[i*k : (i+1)*k]
        max_sum += min(volume)
    print(max_sum)