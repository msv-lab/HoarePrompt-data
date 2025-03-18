#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input is a list of n strings, each of length n, where each character is either 'F', 'S', '?', or '.'. The character at the i-th row and j-th column is the same as the character at the j-th row and i-th column for all i and j, and the character at the i-th row and i-th column is always '.'. At most 2 * floor(n / 2) characters in the input are 'F' or 'S'.
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
        
    #State: After the loop executes all iterations, `n` remains an integer such that 2 <= n <= 24. The list `xx` contains `n + 1` elements, where the first element is an empty string and the subsequent `n` elements are the `n` input strings. The lists `a` and `b` are updated such that for each row `i` and column `j` in the input grid, if the character at position (i, j) is 'F', then `a[i]` and `a[j]` are incremented by 1. Similarly, if the character at position (i, j) is 'S', then `b[i]` and `b[j]` are incremented by 1. The values of `a` and `b` at index 0 remain 0.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `n` remains an integer such that 2 <= n <= 24, `i` is `n`, `xx` contains `n + 1` elements where the first element is an empty string and the subsequent `n` elements are the `n` input strings. `sa` is a list containing the indices of all elements in `a` where `a[i] > 0` and `b[i] == 0`. `sb` is a list containing the indices of all elements in `b` where `b[i] > 0` and `a[i] == 0`.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `i` is `n + 1`, `n` remains an integer such that 2 <= n <= 24, `xx` contains `n + 1` elements where the first element is an empty string and the subsequent `n` elements are the `n` input strings, `sa` is a list containing the indices of all elements in `a` where `a[i] > 0` and `b[i] == 0` as well as any indices `i` where `a[i] == 0` and `b[i] == 0` for `1 <= i <= n`, `sb` is a list containing the indices of all elements in `b` where `b[i] > 0` and `a[i] == 0`, and the length of `sa` is greater than or equal to the length of `sb`.
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
            
        #State: `i` is `n + 1`, `n` is an integer such that 2 <= n <= 24, and `nx` is a string that has been constructed for each `i` from 1 to `n` by iterating over the first `n` characters of the string `xx[i]`. For each character in `xx[i]` at position `j - 1` (where `j` ranges from 1 to `n`), if the character is not '?', it is appended to `nx`. If the character is '?', and either `i` or `j` is in the first `n // 4 - 1` elements of `sa`, 'F' is appended to `nx`. Otherwise, 'S' is appended to `nx`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `i` is `n + 1`, `n` remains an integer such that 2 <= n <= 24, `xx` contains `n + 1` elements where the first element is an empty string and the subsequent `n` elements are the `n` input strings, `sa` is a list containing the indices of all elements in `a` where `a[i] > 0` and `b[i] == 0`, `sb` is a list containing the indices of all elements in `b` where `b[i] > 0` and `a[i] == 0`, and for each index `i` from 1 to `n` where `a[i] == 0` and `b[i] == 0`, `sb` now includes the index `i`. The length of `sa` is less than or equal to the length of `sb`.
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
            
        #State: `i` is `n + 1`, `n` remains an integer such that 2 <= n <= 24, `xx` contains `n + 1` elements where the first element is an empty string and the subsequent `n` elements are the `n` input strings, `sa` is a list containing the indices of all elements in `a` where `a[i] > 0` and `b[i] == 0`, `sb` is a list containing the indices of all elements in `b` where `b[i] > 0` and `a[i] == 0`, and for each index `i` from 1 to `n` where `a[i] == 0` and `b[i] == 0`, `sb` now includes the index `i`. The length of `sa` is less than or equal to the length of `sb`. `j` is `n + 1`. `nx` is a string of length `n` that has been constructed for each `i` from 1 to `n` by iterating through the string `xx[i]` from the 0th index to the `n-1`th index. For each character in `xx[i]` at index `j-1` (where `j` ranges from 1 to `n`), if the character is not '?', it is appended to `nx`. If the character is '?', and if either `i` or `j` is in the first `n // 4 - 1` elements of `sb`, 'S' is appended to `nx`. Otherwise, 'F' is appended to `nx`.
    #State: `i` is `n + 1`, `n` remains an integer such that 2 <= n <= 24, and `xx` contains `n + 1` elements where the first element is an empty string and the subsequent `n` elements are the `n` input strings. `sa` is a list containing the indices of all elements in `a` where `a[i] > 0` and `b[i] == 0`, and `sb` is a list containing the indices of all elements in `b` where `b[i] > 0` and `a[i] == 0`. If `len(sa) >= len(sb)`, `nx` is a string of length `n` constructed for each `i` from 1 to `n` by iterating through the first `n` characters of `xx[i]`. For each character in `xx[i]` at position `j - 1` (where `j` ranges from 1 to `n`), if the character is not '?', it is appended to `nx`. If the character is '?', and either `i` or `j` is in the first `n // 4 - 1` elements of `sa`, 'F' is appended to `nx`. Otherwise, 'S' is appended to `nx`. If `len(sa) < len(sb)`, for each index `i` from 1 to `n` where `a[i] == 0` and `b[i] == 0`, `sb` now includes the index `i`. `nx` is a string of length `n` constructed for each `i` from 1 to `n` by iterating through the string `xx[i]` from the 0th index to the `n-1`th index. For each character in `xx[i]` at index `j-1` (where `j` ranges from 1 to `n`), if the character is not '?', it is appended to `nx`. If the character is '?', and if either `i` or `j` is in the first `n // 4 - 1` elements of `sb`, 'S' is appended to `nx`. Otherwise, 'F' is appended to `nx`.
#Overall this is what the function does:The function reads an integer `n` (2 <= n <= 24) and a list of `n` strings, each of length `n`, forming a symmetric matrix where the diagonal characters are always '.' and each character is either 'F', 'S', '?', or '.'. It then processes the matrix to identify indices where 'F' or 'S' are present and categorizes them into two lists, `sa` and `sb`. Depending on the lengths of `sa` and `sb`, it constructs a new matrix by replacing '?' characters with 'F' or 'S' based on the conditions: if `len(sa) >= len(sb)`, '?' is replaced with 'F' for the first `n // 4 - 1` elements of `sa` and with 'S' otherwise; if `len(sa) < len(sb)`, '?' is replaced with 'S' for the first `n // 4 - 1` elements of `sb` and with 'F' otherwise. The function prints the new matrix row by row.

