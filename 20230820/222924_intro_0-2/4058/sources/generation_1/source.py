n, r = map(int, input().split()) # taking n and r inputs
a = list(map(int, input().split())) # taking array input

# Initializing variables
count = 0
i = 0

# Looping through the array
while i < n:
    # If the current element is not warmed up
    if a[i] == 0:
        # Variable to check if a heater can warm up the current element
        checked = False
        # Looping through the range [i - r + 1; i + r - 1]
        for j in range(max(0, i - r + 1), min(n, i + r)):
            # If a heater is present in the range and has not been checked yet
            if a[j] == 1 and not checked:
                # Increment count as a heater can warm up the current element
                count += 1
                # Set checked to True to prevent checking the same heater again
                checked = True
    # Increment i
    i += 1

# Checking if all the elements have been warmed up
for i in range(n):
    # If any element is not warmed up, print -1
    if a[i] == 0:
        print(-1)
        break
else:
    # Print the minimum number of heaters needed
    print(count)