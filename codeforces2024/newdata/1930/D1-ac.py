import sys
from decimal import Decimal, getcontext

# Set the precision for Decimal operations
getcontext().prec = 15

def solve():
    # Read the number of test cases
    num_cases = int(input().strip())
    
    # Process each test case
    for _ in range(num_cases):
        # Read the length of the binary string
        length = int(input().strip())
        # Read the binary string
        input_string = input().strip()
        
        # Initialize a DP array with extra space to avoid index errors
        dp = [0] * (length + 10)
        # Initialize the result for the current test case
        result = 0
        
        # Iterate over the string from the end to the beginning
        for i in range(length - 1, -1, -1):
            if input_string[i] == '1':
                # If the character is '1', calculate its contribution
                dp[i] = length - i + dp[i + 3]
            elif input_string[i] == '0':
                # If the character is '0', carry forward the previous DP value
                dp[i] = dp[i + 1]
        
        # Sum up all values in the DP array to get the result
        for i in dp:
            result += i
        
        # Print the result for the current test case
        print(Decimal(result))

if __name__ == "__main__":
    solve()