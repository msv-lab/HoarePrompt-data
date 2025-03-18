def max_of_nth(matrix, n):
    return max(row[n-1] for row in matrix)
