def min_problems_to_create(n, m, a):
    # Step 2: Initialize the count list
    count = [0] * 7
    
    # Step 3: Count the occurrences of each difficulty level
    for char in a:
        count[ord(char) - ord('A')] += 1
    
    # Step 4: Check which counters are less than m
    needed_problems = 0
    for i in range(7):
        if count[i] < m:
            needed_problems += m - count[i]
    
    return needed_problems
 
# Reading the number of test cases
t = int(input())
for _ in range(t):
    # Reading n and m for each test case
    n, m = map(int, input().split())
    # Reading the string a for each test case
    a = input()
    # Outputting the result for each test case
    print(min_problems_to_create(n, m, a))