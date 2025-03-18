#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input is a list of n strings, each of length n, where each character is either 'F', 'S', '?', or '.'. The character at the i-th row and j-th column is the same as the character at the j-th row and i-th column for all i and j, and at most 2 * floor(n / 2) characters in the input are 'F' or 'S'.
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
        
    #State: The list `a` will contain the count of 'F' characters in each row (and column) of the input matrix, the list `b` will contain the count of 'S' characters in each row (and column) of the input matrix, and the list `xx` will contain `n + 1` strings, where the first string is empty and the next `n` strings are the rows of the input matrix. The values of `n` and the input matrix remain unchanged.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: The list `sa` will contain the indices of rows (and columns) where there is at least one 'F' character and no 'S' characters. The list `sb` will contain the indices of rows (and columns) where there is at least one 'S' character and no 'F' characters. The values of `a`, `b`, `xx`, `n`, and the input matrix remain unchanged.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: The list `sa` will contain the indices of rows (and columns) where there is at least one 'F' character and no 'S' characters, as well as any additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0. The list `sb` will remain unchanged. The values of `a`, `b`, `xx`, and `n` remain unchanged. The length of `sa` will be greater than or equal to its initial length, and `t` will be equal to the new length of `sa`.
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
            
        #State: The list `sa` will contain the indices of rows (and columns) where there is at least one 'F' character and no 'S' characters, as well as any additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0. The list `sb` will remain unchanged. The values of `a`, `b`, `xx`, and `n` remain unchanged. The length of `sa` will be greater than or equal to its initial length, and `t` will be equal to the new length of `sa`. The loop will print a string `nx` for each row `i` from 1 to `n`, where each character in `nx` is either the original character from `xx[i][j-1]` if it is not '?', 'F' if `i` or `j` is in the first `n // 4 - 1` elements of `sa`, or 'S' otherwise.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: The list `sb` will contain the indices of rows (and columns) where there is at least one 'S' character and no 'F' characters, as well as any additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0. The list `sa` remains unchanged. The values of `a`, `b`, `xx`, and `n` remain unchanged.
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
            
        #State: The list `sb` will remain unchanged. The list `sa` will also remain unchanged. The values of `a`, `b`, `xx`, and `n` will remain unchanged. The loop will print a series of strings `nx`, where each string `nx` is constructed by iterating over the rows of `xx` from 1 to `n`. For each row, if the character at position `j-1` is not '?', it will be added to `nx`. If the character is '?', and the row index `i` or column index `j` is in the first quarter of the `sb` list (up to `n // 4 - 1`), 'S' will be added to `nx`. Otherwise, 'F' will be added to `nx`.
    #State: The list `sa` will contain the indices of rows (and columns) where there is at least one 'F' character and no 'S' characters. The list `sb` will contain the indices of rows (and columns) where there is at least one 'S' character and no 'F' characters. The values of `a`, `b`, `xx`, and `n` remain unchanged. If `len(sa) >= len(sb)`, `sa` will also contain additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0, and `t` will be equal to the new length of `sa`. The loop will print a string `nx` for each row `i` from 1 to `n`, where each character in `nx` is either the original character from `xx[i][j-1]` if it is not '?', 'F' if `i` or `j` is in the first `n // 4 - 1` elements of `sa`, or 'S' otherwise. If `len(sa) < len(sb)`, both `sa` and `sb` will remain unchanged, and the loop will print a series of strings `nx`, where each string `nx` is constructed by iterating over the rows of `xx` from 1 to `n`. For each row, if the character at position `j-1` is not '?', it will be added to `nx`. If the character is '?', and the row index `i` or column index `j` is in the first quarter of the `sb` list (up to `n // 4 - 1`), 'S' will be added to `nx`. Otherwise, 'F' will be added to `nx`.
#Overall this is what the function does:The function reads an integer `n` (2 <= n <= 24) and a list of `n` strings, each of length `n`, forming a symmetric matrix. It counts the occurrences of 'F' and 'S' characters in each row (and column) and identifies rows (and columns) where only 'F' or only 'S' characters are present. The function then modifies and prints the matrix by replacing '?' characters: if there are more or equal rows with 'F' (no 'S') than rows with 'S' (no 'F'), it replaces '?' with 'F' for the first `n // 4 - 1` rows and columns in the 'F' list, and with 'S' otherwise. If there are more rows with 'S' (no 'F') than rows with 'F' (no 'S'), it replaces '?' with 'S' for the first `n // 4 - 1` rows and columns in the 'S' list, and with 'F' otherwise. The original input matrix and its symmetry are preserved, and the function does not return any value.

