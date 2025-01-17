def can_form_non_increasing_sequence(n, k, a, b):
    # Sort b in descending order
    b.sort(reverse=True)
    
    # Fill the zeros in a with the elements from b
    b_index = 0
    for i in range(n):
        if a[i] == 0:
            a[i] = b[b_index]
            b_index += 1
    
    # Check if the resulting sequence is non-increasing
    for i in range(1, n):
        if a[i] > a[i-1]:
            return "Yes"
    
    return "No"

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Print the result
print(can_form_non_increasing_sequence(n, k, a, b))
