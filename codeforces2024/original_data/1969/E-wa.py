from collections import defaultdict

# Read the number of test cases
for _ in range(int(input())):
    # Read the length of the array
    n = int(input())
    # Read the array elements
    a = list(map(int, input().split()))
    
    # Dictionary to count the frequency of each element
    d = defaultdict(int)
    
    # Count the frequency of each element in the array
    for i in a:
        d[i] += 1
    
    # Initialize the answer for the current test case
    ans = 0
    
    # Iterate over each unique element in the dictionary
    for i in d:
        # If the frequency of the element is greater than 2
        if d[i] > 2:
            # Calculate the number of replacements needed
            # We need to replace (d[i] - 2) elements to make the frequency 2
            ans += (d[i] - 2)
    
    # Output the result for the current test case
    print(ans)