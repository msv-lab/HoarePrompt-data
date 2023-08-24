n, s = map(int, input().split())
v = list(map(int, input().split()))

# Sort the kegs in non-decreasing order of their volumes
v.sort()

# Calculate the total volume of kvass in all the kegs
total_kvass = sum(v)

# If the total volume of kvass is less than s, it is not possible to pour s liters of kvass
if total_kvass < s:
    print(-1)
else:
    # Calculate the minimum kvass level in the kegs
    min_kvass = min(v)

    # If the total kvass volume is already greater than or equal to s,
    # the minimum kvass level can be 0
    if total_kvass >= s:
        min_kvass = 0
    else:
        # Calculate the remaining kvass volume needed to pour s liters
        remaining_kvass = s - total_kvass

        # Calculate the minimum kvass level in the kegs considering the remaining kvass volume
        min_kvass = min(min_kvass, remaining_kvass // n)

    print(min_kvass)