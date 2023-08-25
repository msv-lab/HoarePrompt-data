n = int(input())
a = list(map(int, input().split()))

# Find the distinct values in the array
distinct_vals = set(a)


# Check the number of distinct values
num_vals = len(distinct_vals)

# If there is only one unique value, return 0
if num_vals == 1:
    print(0)

# If there are two unique values, find the difference and check if it's even or odd
elif num_vals == 2:
    diff = max(distinct_vals) - min(distinct_vals)
    if diff % 2 == 0:
        print(diff // 2)
    else:
        print(-1)

# If there are three unique values, check if the differences between consecutive sorted values are equal
elif num_vals == 3:
    sorted_vals = sorted(distinct_vals)
    if sorted_vals[1] - sorted_vals[0] == sorted_vals[2] - sorted_vals[1]:
        print(sorted_vals[1] - sorted_vals[0])
    else:
        print(-1)

# If there are more than three unique values, it's not possible to choose a value of D
else:
    print(-1)