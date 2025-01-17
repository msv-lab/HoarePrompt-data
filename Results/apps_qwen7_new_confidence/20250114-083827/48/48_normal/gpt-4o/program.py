s = input().split()
n = int(s[0])
x = int(s[1])
a = list(map(int, input().split()))

# Initialize variables to store the best sums
max_normal = 0  # Maximum sum of any subarray without multiplication
max_multiplied = 0  # Maximum sum where a subarray is multiplied
max_combined = 0  # Maximum sum where a subarray was multiplied and then combined back

current_normal = 0
current_multiplied = 0
current_combined = 0

for value in a:
    # Update the current sums
    current_normal = max(0, current_normal + value)
    current_multiplied = max(current_multiplied + value * x, current_normal + value * x)
    current_combined = max(current_combined + value, current_multiplied)
    
    # Update the maximum sums
    max_normal = max(max_normal, current_normal)
    max_multiplied = max(max_multiplied, current_multiplied)
    max_combined = max(max_combined, current_combined)

# The result is the maximum value among the calculated maximum sums
print(max(max_normal, max_multiplied, max_combined))
