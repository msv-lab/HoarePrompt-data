n, r = map(int, input().split()) # taking n and r inputs
a = list(map(int, input().split())) # taking array input

# Initializing variables
count = 0

# Looping through the array
for i in range(n):
    # If the current element is not warmed up
    if a[i] == 0:
        # Variable to check if any heater can warm up the current element
        can_warm = False
        # Looping through the range [i - r + 1; i + r - 1]
        for j in range(max(0, i - r + 1), min(n, i + r)):
            # If a heater is present in the range
            if a[j] == 1:
                can_warm = True
                break
        # If no heater can warm up the current element, output -1
        if not can_warm:
            print(-1)
            break
    # If the current element is warmed up, increment count
    else:
        count += 1
else:
    # Print the minimum number of heaters needed
    print(count)