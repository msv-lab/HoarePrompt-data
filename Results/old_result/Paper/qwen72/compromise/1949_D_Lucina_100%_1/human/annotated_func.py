#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input consists of n lines, each containing n characters. The characters are either 'F' (funny), 'S' (scary), '?' (undecided), or '.' (same scenario). The matrix is symmetric, and the number of 'F' and 'S' characters does not exceed 2 * floor(n / 2).
def func():
    n = int(input())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    xx = ['']
    for i in range(1, n + 1):
        x = input()
        
        for j in range(1, n + 1):
            if x[j - 1] == 'F':
                a[i] += 1
                a[j] += 1
            elif x[j - 1] == 'S':
                b[i] += 1
                b[j] += 1
        
        xx.append(x)
        
    #State: After the loop executes all the iterations, `n` remains an integer provided by the user such that 2 <= n <= 24. The list `xx` now contains `n` strings, each string being one of the `n` lines of input. The list `a` has its elements at indices 1 to `n` incremented by 1 for each 'F' encountered in the corresponding positions (0 to `n-1`) of the input lines. The list `b` has its elements at indices 1 to `n` incremented by 1 for each 'S' encountered in the corresponding positions (0 to `n-1`) of the input lines.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `n` remains an integer provided by the user such that 2 <= n <= 24, `i` is `n`, `xx` contains `n` strings, each string being one of the `n` lines of input, `a` has its elements at indices 1 to `n` incremented by 1 for each 'F' encountered in the corresponding positions (0 to `n-1`) of the input lines, `b` has its elements at indices 1 to `n` incremented by 1 for each 'S' encountered in the corresponding positions (0 to `n-1`) of the input lines. `sa` is a list containing the indices from 1 to `n` where the corresponding element in `a` is greater than 0 and the corresponding element in `b` is 0. `sb` is a list containing the indices from 1 to `n` where the corresponding element in `b` is greater than 0 and the corresponding element in `a` is 0.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `n` remains an integer provided by the user such that 2 <= n <= 24, `i` is `n + 1`, and `sa` is a list that includes all indices from 1 to `n` where the corresponding element in `a` is 0 and the corresponding element in `b` is 0. The values of `a`, `b`, `sb`, and `t` remain unchanged.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sa[:n // 4 - 1] or j in sa[:n // 4 - 1]:
                    nx += 'F'
                else:
                    nx += 'S'
            
            print(nx)
            
        #State: `n` remains an integer provided by the user such that 2 <= n <= 24, `i` is `n + 1`, `sa` is a list that includes all indices from 1 to `n` where the corresponding element in `a` is 0 and the corresponding element in `b` is 0, `j` is `n + 1`, and `nx` is a string of length `n` for each iteration `i` from 1 to `n`. Each `nx` string is constructed based on the conditions in the loop: if the character at `xx[i][j - 1]` is not '?', it is appended directly to `nx`. If the character is '?', and either `i` or `j` is in the first `n // 4 - 1` elements of `sa`, 'F' is appended to `nx`. Otherwise, 'S' is appended to `nx`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `n` remains an integer such that 2 <= n <= 24, `i` is `n`. `sb` contains the indices from 1 to `n` where the corresponding elements in `a` and `b` are both 0. The lists `a`, `b`, `sa`, and `sb` are updated based on the conditions specified in the loop.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sb[:n // 4 - 1] or j in sb[:n // 4 - 1]:
                    nx += 'S'
                else:
                    nx += 'F'
            
            print(nx)
            
        #State: `n` remains an integer such that 2 <= n <= 24, `i` is `n + 1`, `sb` contains the indices from 1 to `n` where the corresponding elements in `a` and `b` are both 0, and `nx` is a string of length `n` for each `i` from 1 to `n`, where each character is determined by the conditions in the loop: if `xx[i][j - 1]` is not '?', the character is the corresponding character from `xx[i][j - 1]`; if `xx[i][j - 1]` is '?', the character is 'S' if either `i` or `j` is in the first `n // 4 - 1` elements of `sb`, or 'F' otherwise.
    #State: `n` remains an integer provided by the user such that 2 <= n <= 24, `i` is `n + 1`, and `nx` is a string of length `n` for each `i` from 1 to `n`. If `len(sa) >= len(sb)`, `sa` is a list that includes all indices from 1 to `n` where the corresponding element in `a` is 0 and the corresponding element in `b` is 0, and `j` is `n + 1`. Each `nx` string is constructed such that if the character at `xx[i][j - 1]` is not '?', it is appended directly to `nx`. If the character is '?', and either `i` or `j` is in the first `n // 4 - 1` elements of `sa`, 'F' is appended to `nx`. Otherwise, 'S' is appended to `nx`. If `len(sa) < len(sb)`, `sb` is a list that includes all indices from 1 to `n` where the corresponding elements in `a` and `b` are both 0. Each `nx` string is constructed such that if the character at `xx[i][j - 1]` is not '?', it is appended directly to `nx`. If the character is '?', and either `i` or `j` is in the first `n // 4 - 1` elements of `sb`, 'S' is appended to `nx`. Otherwise, 'F' is appended to `nx`.
#Overall this is what the function does:The function `func` processes a symmetric matrix of characters ('F', 'S', '?', or '.') provided by the user. It reads an integer `n` (2 <= n <= 24) and `n` lines of input, each containing `n` characters. The function then counts the occurrences of 'F' and 'S' in each row and column of the matrix. It identifies indices where 'F' or 'S' are exclusively present and appends these indices to lists `sa` and `sb`, respectively. If the length of `sa` is greater than or equal to `sb`, the function appends indices where both 'F' and 'S' are absent to `sa` and updates the matrix by replacing '?' with 'F' for the first `n // 4 - 1` elements in `sa`, and with 'S' otherwise. If the length of `sa` is less than `sb`, it appends such indices to `sb` and updates the matrix by replacing '?' with 'S' for the first `n // 4 - 1` elements in `sb`, and with 'F' otherwise. The function prints the updated matrix.

