# Note that this problem was helped by many Youtbers and classmates to help me solve and understand Python and this problem
 
from collections import defaultdict
 
def count_beautiful_pairs(t, test_cases):
    results = []
    
    # Process each test case
    for case in test_cases:
        n, x, y = case['params']
        a = case['array']
        
        # Dictionary 
        freq = defaultdict(int)
        beautiful_count = 0
        
        # Define each part
        for num in a:
            mod_x = num % x
            mod_y = num % y
            
            # The requirements for this test
            required_mod_x = (x - mod_x) % x
            required_mod_y = mod_y
            
            # beauttiful pairs
            if (required_mod_x, required_mod_y) in freq:
                beautiful_count += freq[(required_mod_x, required_mod_y)]
            
            # mod,x and mod,y
            freq[(mod_x, mod_y)] += 1
        
        # Store the result test
        results.append(beautiful_count)
    
    return results
 
t = int(input())  # Number of test cases
test_cases = []
 
for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append({'params': (n, x, y), 'array': a})
 
results = count_beautiful_pairs(t, test_cases)
 
 
for result in results:
    print(result)