# Read the number of test cases
num_test_cases = int(input())

for _ in range(num_test_cases):
    # Read the length of the list
    list_length = int(input())
    
    # Read the elements of the list
    list_elements = list(map(int, input().split()))
    
    # Sort the list
    list_elements.sort()
    
    # Initialize the maximum difference
    max_difference = 0
    
    # Calculate the maximum difference between consecutive elements
    for i in range(1, list_length):
        difference = list_elements[i] - list_elements[i - 1]
        if difference > max_difference:
            max_difference = difference
    
    # Print the result
    print(max_difference)
