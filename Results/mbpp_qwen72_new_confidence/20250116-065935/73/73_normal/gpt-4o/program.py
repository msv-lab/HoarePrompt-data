def magic_square_test(matrix):
    n = len(matrix)
    if n == 0:
        return False

    # Calculate the sum of the first row to use as the target sum
    target_sum = sum(matrix[0])

    # Check the sum of each row
    for row in matrix:
        if sum(row) != target_sum:
            return False

    # Check the sum of each column
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != target_sum:
            return False

    # Check the sum of the main diagonal
    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False

    # Check the sum of the anti-diagonal
    if sum(matrix[i][n - 1 - i] for i in range(n)) != target_sum:
        return False
    
    return True

# Tests
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True
assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]]) == False
