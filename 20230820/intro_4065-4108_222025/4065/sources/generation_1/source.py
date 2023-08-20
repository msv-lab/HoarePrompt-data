n = int(input())
difficulties = list(map(int, input().split()))

# Initialize the count of valid contests to 1 since a contest with only one problem is always valid
valid_contests = 1

# Iterate through each problem in the problemset
for i in range(n-1):
    # Check if there is a problem with difficulty greater than the current problem but not greater than twice the difficulty
    if difficulties[i+1] <= difficulties[i] * 2:
        # Increment the count of valid contests
        valid_contests += 1
    else:
        # If the condition is not satisfied, break the loop since we can't form any more valid contests
        break

print(valid_contests)