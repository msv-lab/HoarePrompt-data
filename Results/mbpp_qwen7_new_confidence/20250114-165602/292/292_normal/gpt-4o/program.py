def maxAverageOfPath(matrix):
    N = len(matrix)
    
    # Create a dp table to store the maximum sum to reach each cell
    dp = [[0] * N for _ in range(N)]
    
    # Initialize the top-left cell
    dp[0][0] = matrix[0][0]
    
    # Fill in the first row (can only come from the left)
    for j in range(1, N):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
    
    # Fill in the first column (can only come from above)
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    
    # Fill in the rest of the dp table
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    # The maximum sum to reach the bottom-right cell
    max_sum = dp[N-1][N-1]
    
    # The number of cells in the path is always 2N - 1
    num_cells = 2 * N - 1
    
    # Return the average
    return max_sum / num_cells

# Test cases
assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8
