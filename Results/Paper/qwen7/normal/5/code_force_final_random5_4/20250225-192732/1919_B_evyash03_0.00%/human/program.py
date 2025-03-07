def solve(expression, length):
    count = 0
    balance = 0
 
    for char in expression:
        if char == '+':
            balance += 1
        elif char == '-':
            balance -= 1
        
        if balance < 0:
            count += 1
            balance = 0
 
    return count + (balance > 0)
 
# Read the number of test cases
t = int(input())
 
# Process each test case
for _ in range(t):
    length = int(input())
    expression = input().strip()
    
    # Split expression by '-' to get the length of the final result
    parts = expression.split('-')
    result_length = sum(len(part) for part in parts)
    
    print(solve(expression, result_length))