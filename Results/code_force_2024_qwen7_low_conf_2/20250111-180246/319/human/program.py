def maximize_difference(n, q, encrypted_values):
    # Initialize the array a
    a = []
    # Initialize the last value
    last = 0
    # Initialize the result list
    results = []

    for i in range(q):
        # Decrypt the value
        v = (encrypted_values[i] + last) % n
        # Append v to the array a
        a.append(v)
        # Calculate f(a)
        f_a = calculate_f(a)
        # Update the last value
        last = f_a
        # Append the result
        results.append(f_a)

    return results

def calculate_f(b):
    # Calculate the maximum and minimum values of b_i | x for all possible x
    max_val = max(b)
    min_val = min(b)
    # Calculate the maximum difference
    return max_val - min_val

# Input reading
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    encrypted_values = list(map(int, input().split()))
    # Process the queries
    results = maximize_difference(n, q, encrypted_values)
    # Print the results
    print(' '.join(map(str, results)))