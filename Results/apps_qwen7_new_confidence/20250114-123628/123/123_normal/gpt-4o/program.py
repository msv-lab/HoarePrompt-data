# Read the input
n = int(input())
a = list(map(int, input().split()))

# Function to check if an array can be split into two parts with equal sum
def can_be_split_after_moving_element(n, a):
    total_sum = sum(a)
    prefix_sum = 0
    
    # Iterate through the array
    for i in range(n):
        current_element = a[i]
        # Calculate the new sum after removing the current element
        new_total_sum = total_sum - current_element
        
        # If the new total sum is odd, we cannot split it into two equal parts
        if new_total_sum % 2 != 0:
            continue
        
        target_sum = new_total_sum // 2
        prefix_sum = 0
        
        # Check if we can split the array into two parts with the target_sum
        for j in range(n):
            if j != i:
                prefix_sum += a[j]
            if prefix_sum == target_sum:
                return "YES"
    return "NO"

# Print the result
print(can_be_split_after_moving_element(n, a))
