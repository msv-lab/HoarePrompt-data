def solve(expression, length):
    count = 0
 
    for char in expression:
        if char == '+':
          count += 1
    sub = length-count
    return abs(sub-count)
 
t = int(input())
 
for i in range(t):
    length = int(input())
    expression = input().strip()
    print(solve(expression, length))