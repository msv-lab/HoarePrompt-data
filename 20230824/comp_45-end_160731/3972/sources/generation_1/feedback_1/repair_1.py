def count_sequences(n):
    # Initialize an array to store the count of sequences for each value of n
    dp = [0] * (n + 1)
    # Set the base cases
    dp[1] = 1
    dp[2] = 2
    # Iterate from 3 to n
    for i in range(3, n + 1):
        # If the current element is even
        if i % 2 == 0:
            # The count of sequences is equal to i times the count of sequences for the previous element
            dp[i] = i * dp[i - 1] % (10**9 + 7)
        # If the current element is odd
        else:
            # The count of sequences is equal to the sum of the counts of sequences for the previous element and all even numbers less than or equal to i
            dp[i] = dp[i - 1] + sum(dp[2:i:2])
    # Return the count of sequences for n
    return dp[n]

# Read the input value of n from Standard Input
n = int(input())

# Call the count_sequences function and print the result
print(count_sequences(n))