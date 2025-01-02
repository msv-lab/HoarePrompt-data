#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 100, and matrix is a 2D list of strings where each string contains m lowercase Latin letters.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 100, `m` is a positive integer such that 1 ≤ `m` ≤ 100, `matrix` is a list containing `n` elements, each of which is a list of characters read from `raw_input` calls, `selected_words` is an empty string, `row` is a list of characters read from the `raw_input` call in the corresponding iteration.
    for i in range(n):
        for j in range(m):
            if not func_2(matrix, i, j):
                selected_words += matrix[i][j]
        
    #State of the program after the  for loop has been executed: `j` is equal to `m`, `m` is a positive integer such that \(1 \leq m \leq 100\), `n` is a positive integer such that \(1 \leq n \leq 100\), `matrix` is a list containing `n` elements, each of which is a list of characters, `selected_words` is a string containing all characters from the rows of `matrix` where `func_2(matrix, i, j)` returns `False` for all \(0 \leq j < m\) in every row `i` for which `not func_2(matrix, i, j)` evaluates to `True` for at least one \(j\), and `row` is a list of characters read from the `raw_input` call in the corresponding iteration.
    print(selected_words)
#Overall this is what the function does:The function accepts two positive integers `n` and `m`, representing the dimensions of a 2D list `matrix` where each row contains `m` lowercase Latin letters. The function iterates over each element in the matrix and constructs a string `selected_words` by concatenating characters from the matrix based on the result of calling `func_2(matrix, i, j)` for each element. Specifically, if `func_2(matrix, i, j)` returns `False`, the character at position `(i, j)` is added to `selected_words`. After processing all elements, the function prints `selected_words`.

#State of the program right berfore the function call: matrix is a 2D list of characters representing the crossword grid, i and j are integers such that 0 <= i < len(matrix) and 0 <= j < len(matrix[0]), and the function is called for each cell in the matrix to determine if the letter at that cell should be crossed out.
def func_2(matrix, i, j):
    letter = matrix[i][j]
    matrix[i][j] = '_'
    result = letter in matrix[i] or letter in zip(*matrix)[j]
    matrix[i][j] = letter
    return result
    #The program returns result which is either True or False depending on whether '_' is found in matrix[i] or zip(*matrix)[j]
#Overall this is what the function does:The function `func_2` accepts a 2D list `matrix` and two integers `i` and `j`, representing the row and column indices of a cell in the matrix. It checks whether the character at position `(i, j)` or the character at position `(j, i)` in the transposed matrix is `'_'`. If either condition is true, the function returns `True`; otherwise, it returns `False`. After the function executes, the original character at position `(i, j)` in the matrix is temporarily replaced with `'_'` and then restored to its original value. The function does not handle edge cases where the matrix is empty or indices are out of bounds, but it ensures that the character at the specified position is checked in both the original and transposed matrix for the presence of `'_'`.

