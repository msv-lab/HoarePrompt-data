#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input is a list of n strings, each of length n, where each string represents a row in the transition video plan. Each character in the string is either 'F' (funny), 'S' (scary), '?' (undecided), or '.' (diagonal, no transition). The matrix is symmetric, and the number of 'F' and 'S' characters does not exceed 2 * floor(n / 2).
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
        
    #State: After the loop executes all iterations, `xx` will be a list containing `n + 1` elements, where the first element is an empty string and the next `n` elements are the `n` input strings. The lists `a` and `b` will each have `n + 1` elements, where each element at index `i` (1 ≤ i ≤ n) will represent the count of 'F' and 'S' characters, respectively, in the i-th row and the i-th column of the input matrix. The initial state of `a` and `b` being all zeros will be updated accordingly.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `xx` remains unchanged, `a` and `b` retain their counts of 'F' and 'S' characters, `sa` contains indices of rows with at least one 'F' and no 'S' in the corresponding column, `sb` contains indices of columns with at least one 'S' and no 'F' in the corresponding row.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Output State: `xx` remains unchanged, `a` and `b` retain their counts of 'F' and 'S' characters, `sa` contains indices of rows with at least one 'F' and no 'S' in the corresponding column, and also includes indices of rows where both `a[i]` and `b[i]` are 0, `sb` contains indices of columns with at least one 'S' and no 'F' in the corresponding row, and the length of `sa` is greater than or equal to the length of `sb`.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sa[:n // 4] or j in sa[:n // 4]:
                    nx += 'F'
                else:
                    nx += 'S'
            
            print(nx)
            
        #State: The `xx` matrix is modified such that for each row `i` and column `j` where `xx[i][j - 1]` is '?', the character is replaced with 'F' if `i` or `j` is in the first `n // 4` elements of `sa`. Otherwise, the character is replaced with 'S'. The variables `a`, `b`, `sa`, and `sb` remain unchanged.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: `xx` remains unchanged, `a` and `b` retain their counts of 'F' and 'S' characters, `sa` contains indices of rows with at least one 'F' and no 'S' in the corresponding column, `sb` contains indices of columns with at least one 'S' and no 'F' in the corresponding row, and the length of `sa` is less than or equal to the length of `sb`.
        for i in range(1, n + 1):
            nx = ''
            
            for j in range(1, n + 1):
                if xx[i][j - 1] != '?':
                    nx += xx[i][j - 1]
                elif i in sb[:n // 4] or j in sb[:n // 4]:
                    nx += 'S'
                else:
                    nx += 'F'
            
            print(nx)
            
        #State: `xx` remains unchanged, `a` and `b` retain their counts of 'F' and 'S' characters, `sa` contains indices of rows with at least one 'F' and no 'S' in the corresponding column, `sb` contains indices of columns with at least one 'S' and no 'F' in the corresponding row, and the length of `sa` is less than or equal to the length of `sb`. The loop prints a modified version of each row in `xx` where any '?' character is replaced with 'S' if the row index or column index is in the first quarter of `sb`, otherwise it is replaced with 'F'.
    #State: *`xx` remains unchanged, `a` and `b` retain their counts of 'F' and 'S' characters, `sa` contains indices of rows with at least one 'F' and no 'S' in the corresponding column, and `sb` contains indices of columns with at least one 'S' and no 'F' in the corresponding row. If `len(sa) >= len(sb)`, the `xx` matrix is modified such that for each row `i` and column `j` where `xx[i][j - 1]` is '?', the character is replaced with 'F' if `i` or `j` is in the first `n // 4` elements of `sa`. Otherwise, the character is replaced with 'S'. If `len(sa) < len(sb)`, the `xx` matrix is modified such that for each row `i` and column `j` where `xx[i][j - 1]` is '?', the character is replaced with 'S' if `i` or `j` is in the first `n // 4` elements of `sb`. Otherwise, the character is replaced with 'F'.
#Overall this is what the function does:The function reads an integer `n` (2 ≤ n ≤ 24) and a list of `n` strings, each of length `n`, representing a symmetric transition video plan matrix. Each character in the matrix can be 'F' (funny), 'S' (scary), '?' (undecided), or '.' (diagonal, no transition). The function processes this matrix to identify rows and columns with specific characteristics and then modifies the '?' characters in the matrix. Specifically, it counts the number of 'F' and 'S' characters in each row and column, and based on these counts, it creates two lists: `sa` for rows with at least one 'F' and no 'S' in the corresponding column, and `sb` for columns with at least one 'S' and no 'F' in the corresponding row. If the length of `sa` is greater than or equal to the length of `sb`, the function replaces '?' characters in the first quarter of `sa` with 'F' and the rest with 'S'. If the length of `sa` is less than the length of `sb`, the function replaces '?' characters in the first quarter of `sb` with 'S' and the rest with 'F'. The function then prints the modified matrix. The original matrix `xx` remains unchanged, and the lists `a`, `b`, `sa`, and `sb` retain their final states.

