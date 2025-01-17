def can_win(matrix):
    # Check horizontal lines
    for i in range(10):
        count = 0
        for j in range(10):
            if matrix[i][j] == 'X':
                count += 1
            elif matrix[i][j] == '.':
                if count >= 4:
                    return True
                count = 0
            else:
                count = 0
        if count >= 4:
            return True

    # Check vertical lines
    for j in range(10):
        count = 0
        for i in range(10):
            if matrix[i][j] == 'X':
                count += 1
            elif matrix[i][j] == '.':
                if count >= 4:
                    return True
                count = 0
            else:
                count = 0
        if count >= 4:
            return True

    # Check diagonal lines (top-left to bottom-right)
    for k in range(-9, 10):
        count = 0
        for i in range(10):
            j = i + k
            if j >= 0 and j < 10:
                if matrix[i][j] == 'X':
                    count += 1
                elif matrix[i][j] == '.':
                    if count >= 4:
                        return True
                    count = 0
                else:
                    count = 0
        if count >= 4:
            return True

    # Check diagonal lines (bottom-left to top-right)
    for k in range(-9, 10):
        count = 0
        for i in range(10):
            j = 9 - i + k
            if j >= 0 and j < 10:
                if matrix[i][j] == 'X':
                    count += 1
                elif matrix[i][j] == '.':
                    if count >= 4:
                        return True
                    count = 0
                else:
                    count = 0
        if count >= 4:
            return True

    return False

matrix = [input() for _ in range(10)]
print('YES' if can_win(matrix) else 'NO')
