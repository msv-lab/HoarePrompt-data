from collections import Counter

# Read input data
for s in [*open(0)][2::2]:
    # Count the occurrences of each number in your hand
    a = Counter(s.split())
    
    # Calculate the initial score: half of the count of numbers that appear twice
    initial_score = sum(v // 2 for v in a.values())
    
    # Calculate the maximum score you can achieve
    # This is the initial score plus the count of numbers that appear twice
    max_score = initial_score + sum(v == 2 for v in a.values())
    
    # Print the result for each test case
    print(max_score)