# Read input values
n, m, min_temp, max_temp = map(int, input().split())
temperatures = list(map(int, input().split()))

# Check if min_temp and max_temp are already in the list of temperatures
contains_min = min_temp in temperatures
contains_max = max_temp in temperatures

# Calculate how many additional temperatures we need to add
additional_needed = n - m

# Check if we can add the necessary temperatures to meet the min and max requirements
if contains_min and contains_max:
    print("Correct")
elif additional_needed >= 2 or (additional_needed == 1 and (contains_min or contains_max)):
    print("Correct")
else:
    print("Incorrect")
