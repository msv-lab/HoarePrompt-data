# Function to resolve the k-th element query
def resolve_query(x):
    x = int(x)  # Convert the query index to an integer
    if x in b:
        return b[x]  # If the index is already in the dictionary, return the value
    # Iterate over the operations in reverse order
    for i in a:
        # Calculate the effective index in the original array
        x = (x - 1) % i + 1
        if x in b:
            return b[x]  # Return the value if found in the dictionary

# Read the number of test cases
for _ in range(int(input())):
    a = [0]  # Initialize the list to store the size of the array after each operation
    b = {}   # Dictionary to map indices to their values in the array
    c, d = map(int, input().split())  # Read the number of operations and queries

    # Process each operation
    for i in range(c):
        d, e = map(int, input().split())  # Read the operation type and the integer x
        if a[-1] > 10**19:
            continue  # Skip if the size of the array exceeds 10^19
        if d & 1:  # If the operation type is 1 (append integer x)
            a[-1] += 1  # Increment the size of the array
            b[a[-1]] = e  # Map the new index to the integer x
        else:  # If the operation type is 2 (append x copies of the array)
            a.append(a[-1] * (e + 1))  # Update the size of the array

    a = a[::-1]  # Reverse the list to process operations in reverse order
    # Read the queries, resolve each query, and print the results
    print(str(list(map(resolve_query, input().split())))[1:-1].replace(',', ''))