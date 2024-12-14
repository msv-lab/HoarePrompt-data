n, k = map(str, input().split())
k = int(k)

count_zeros = 0
to_remove = 0

# Iterate from the end of the number to the beginning
for digit in reversed(n):
    if digit == '0':
        count_zeros += 1
    else:
        to_remove += 1
    # If we have enough zeros, we can stop
    if count_zeros == k:
        break

# If we have enough zeros, print the number of digits removed
if count_zeros == k:
    print(to_remove)
else:
    # If not enough zeros, we need to remove all digits except one
    print(len(n) - 1)
