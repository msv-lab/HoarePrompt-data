from sys import stdout

def query(a, b, c, d):
    # This function sends a query to the interactor and returns the result.
    print('?', a, b, c, d)
    stdout.flush()
    x = input().strip()
    return x

for _ in range(int(input())):
    n = int(input())
    
    # Initialize variables to track the smallest and largest indices
    smallest_index = 0
    largest_index = 0
    
    # Step 1: Find the smallest element's index
    for i in range(1, n):
        # Compare the current smallest with the i-th element
        result = query(smallest_index, smallest_index, i, i)
        if result == '<':
            # If the i-th element is smaller, update the smallest_index
            smallest_index = i
    
    # Step 2: Find the largest element's index
    # We use the smallest_index found to help find the largest
    for i in range(n):
        if i == smallest_index:
            continue
        # Compare the current largest with the i-th element
        result = query(largest_index, smallest_index, i, smallest_index)
        if result == '<':
            # If the i-th element is larger, update the largest_index
            largest_index = i
    
    # Output the indices of the smallest and largest elements
    print("!", smallest_index, largest_index)
    stdout.flush()