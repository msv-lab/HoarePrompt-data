n = int(input())
a = list(map(int, input().split()))

# Sort the array
a.sort()

# Initialize the target mex value
mex = 1

# Iterate through the sorted array
for num in a:
    if num >= mex:
        mex += 1

# Print the maximum possible value of mex
print(mex)
