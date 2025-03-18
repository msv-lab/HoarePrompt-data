# Number of test cases
t = int(input())
 
# Loop over all test cases
for _ in range(t):
    # Read the dimensions a and b
    a, b = map(int, input().split())
    
    # If either dimension is even, we can form a different rectangle
    if a % 2 == 0 or b % 2 == 0:
        print("Yes")
    else:
        print("No")