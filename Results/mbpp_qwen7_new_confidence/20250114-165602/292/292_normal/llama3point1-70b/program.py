def maxAverageOfPath(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_avg = float('-inf')

    def dfs(row, col, total, count):
        nonlocal max_avg
        if row == rows - 1 and col == cols - 1:
            max_avg = max(max_avg, total / count)
            return
        if row < rows - 1:
            dfs(row + 1, col, total + matrix[row + 1][col], count + 1)
        if col < cols - 1:
            dfs(row, col + 1, total + matrix[row][col + 1], count + 1)

    dfs(0, 0, matrix[0][0], 1)
    return round(max_avg, 1)
