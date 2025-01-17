def magic_square_test(matrix):
    # Calculate the sum of the first row
    target_sum = sum(matrix[0])
    
    # Check rows
    for row in matrix:
        if sum(row) != target_sum:
            return False
    
    # Check columns
    for col in range(len(matrix[0])):
        if sum(matrix[row][col] for row in range(len(matrix))) != target_sum:
            return False
    
    # Check diagonals
    if sum(matrix[i][i] for i in range(len(matrix))) != target_sum:
        return False
    if sum(matrix[i][len(matrix) - i - 1] for i in range(len(matrix))) != target_sum:
        return False
    
    return True
