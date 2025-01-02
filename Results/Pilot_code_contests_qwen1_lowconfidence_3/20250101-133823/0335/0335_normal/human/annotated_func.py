#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 100, and matrix is an n × m 2D list where each element is a lowercase Latin letter.
def func_1():
    n, m = list(map(int, raw_input('').split()))
    matrix = []
    selected_words = ''
    for i in range(n):
        letters = raw_input('')
        
        row = []
        
        for letter in letters:
            row.append(letter)
        
        matrix.append(row)
        
    #State of the program after the  for loop has been executed: `n` is the number of rows in the matrix, `m` is the length of each row, `matrix` is a list of `n` lists where each list contains `m` characters, `selected_words` is an empty string.
    for i in range(n):
        for j in range(m):
            if not func_2(matrix, i, j):
                selected_words += matrix[i][j]
        
    #State of the program after the  for loop has been executed: `n` is the number of rows in the matrix, `m` is the length of each row (must be greater than 0 and at least 1), `matrix` is a list of `n` lists where each list contains `m` characters, `selected_words` is the concatenation of all characters in the matrix where `func_2(matrix, i, j)` returns `False`.
    print(selected_words)
#Overall this is what the function does:The function processes an n × m 2D list (matrix) where each element is a lowercase Latin letter. It iterates through each character in the matrix and appends it to the `selected_words` string if `func_2(matrix, i, j)` returns `False`. After processing all characters, it prints the `selected_words` string. If `func_2(matrix, i, j)` is not defined or does not return a boolean value for any element, it will still iterate through the entire matrix and concatenate all characters into `selected_words`. Potential edge cases include when the matrix is empty (i.e., n or m is zero), which would result in an empty `selected_words` string. Additionally, if `func_2(matrix, i, j)` is undefined or does not exist, the function will still execute without error, but the behavior regarding which characters are appended to `selected_words` might not be as intended.

#State of the program right berfore the function call: matrix is a 2D list of characters representing the crossword grid, i and j are non-negative integers such that 0 <= i < len(matrix) and 0 <= j < len(matrix[0]), and letter is a character stored in matrix[i][j].
def func_2(matrix, i, j):
    letter = matrix[i][j]
    matrix[i][j] = '_'
    result = letter in matrix[i] or letter in zip(*matrix)[j]
    matrix[i][j] = letter
    return result
    #The program returns True
#Overall this is what the function does:The function `func_2` takes a 2D list `matrix` and two non-negative integers `i` and `j` as input. It checks if the character at `matrix[i][j]` appears either in the same row (excluding the character itself) or in the same column (excluding the character itself). If the character meets this condition, the function returns `True`; otherwise, it returns `False`. After performing the check, the original character at `matrix[i][j]` is restored.

