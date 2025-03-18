def determine_winner(s):
    # Count the number of 'U' characters in the string
    num_up = s.count('U')
    
    # Determine the winner based on the parity of the number of 'U' characters
    if num_up % 2 == 1:
        return "YES"
    else:
        return "NO"
 
# Read input
import sys
input = sys.stdin.read
data = input().split()
 
# Parse the number of test cases
t = int(data[0])
 
# Iterate over each test case
for _ in range(t):
    # Read the number of coins
    n = int(data[1])
    
    # Read the string representation of the coins
    s = data[2]
    
    # Determine and print the result
    print(determine_winner(s))