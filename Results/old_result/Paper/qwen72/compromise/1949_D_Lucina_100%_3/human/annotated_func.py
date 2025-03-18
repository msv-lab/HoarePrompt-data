#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input consists of n lines, each containing n characters, where each character is either 'F', 'S', '?', or '.'. The character at the i-th row and j-th column is the same as the character at the j-th row and i-th column for all i and j, and the character at the i-th row and i-th column is always '.'. At most \lfloor \frac{n}{2} \rfloor transition videos are already decided, meaning at most 2\lfloor \frac{n}{2} \rfloor characters in the input are 'F' or 'S'.
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
        
    #State: `n` is an integer provided by the user such that 2 <= n <= 24, `i` is `n + 1`, `xx` is a list containing `n + 1` strings, where each string corresponds to one of the input lines. The values of `a` and `b` at positions 1 to `n` reflect the cumulative increments based on the characters 'F' and 'S' in the input lines from the first to the `n`-th character.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `n` is an integer provided by the user such that 2 <= n <= 24, `i` is `n + 1`, `xx` is a list containing `n + 1` strings. `sa` is a list containing the indices of all positions from 1 to `n` where `a[i]` is greater than 0 and `b[i]` is 0. `sb` is a list containing the indices of all positions from 1 to `n` where `b[i]` is greater than 0 and `a[i]` is 0.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `i` is `n + 1`, `n` is an integer such that 2 <= n <= 24, `a[1]` to `a[n]` and `b[1]` to `b[n]` are unchanged. `sa` is a list that includes all indices from 1 to `n` where both `a[i]` and `b[i]` are 0.
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
            
        #State: `i` is `n + 1`, `n` is an integer such that 2 <= n <= 24, `a[1]` to `a[n]` and `b[1]` to `b[n]` are unchanged, `sa` is a list that includes all indices from 1 to `n` where both `a[i]` and `b[i]` are 0, and `nx` is a string of length `n` for each `i` from 1 to `n`. For each `i` and `j` from 1 to `n`, if `xx[i][j - 1]` is not a question mark (`?`), `nx` contains the character at `xx[i][j - 1]`. If `xx[i][j - 1]` is a question mark (`?`), `nx` contains 'F' if either `i` or `j` is in the first `n // 4 - 1` elements of `sa`, otherwise it contains 'S'.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `n` is an integer provided by the user such that 2 <= n <= 24, `i` is `n + 1`, `xx` is a list containing `n + 1` strings, `sa` is a list containing the indices of all positions from 1 to `n` where `a[i]` is greater than 0 and `b[i]` is 0, `sb` is a list containing the indices of all positions from 1 to `n` where `b[i]` is greater than 0 and `a[i]` is 0, and the length of `sa` is less than or equal to the length of `sb`. For each position `i` from 1 to `n`, if `a[i]` and `b[i]` are both 0, `sb` now includes the index `i`. Otherwise, the values of `a[i]` and `b[i]` remain unchanged.
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
            
        #State: `n` is an integer such that 2 <= n <= 24, `i` is `n + 1`, `xx` is a list containing `n + 1` strings, `sa` is a list containing the indices of all positions from 1 to `n` where `a[i]` is greater than 0 and `b[i]` is 0, `sb` is a list containing the indices of all positions from 1 to `n` where `b[i]` is greater than 0 and `a[i]` is 0, the length of `sa` is less than or equal to the length of `sb`, for each position `i` from 1 to `n`, if `a[i]` and `b[i]` are both 0, `sb` now includes the index `i`, otherwise the values of `a[i]` and `b[i]` remain unchanged, `j` is `n + 1`, and `nx` is a string of length `n` constructed for each `i` from 1 to `n` by iterating through `xx[i]` from index 0 to `n - 1`. For each character in `xx[i]`, if it is not `?`, it is appended to `nx`. If it is `?` and either `i` or `j` is in the first `n // 4 - 1` elements of `sb`, 'S' is appended to `nx`. Otherwise, 'F' is appended to `nx`.
    #State: *`n` is an integer such that 2 <= n <= 24, `i` is `n + 1`, `xx` is a list containing `n + 1` strings, `sa` is a list containing the indices of all positions from 1 to `n` where `a[i]` is greater than 0 and `b[i]` is 0, `sb` is a list containing the indices of all positions from 1 to `n` where `b[i]` is greater than 0 and `a[i]` is 0. If `len(sa) >= len(sb)`, `nx` is a string of length `n` for each `i` from 1 to `n`. For each `i` and `j` from 1 to `n`, if `xx[i][j - 1]` is not a question mark (`?`), `nx` contains the character at `xx[i][j - 1]`. If `xx[i][j - 1]` is a question mark (`?`), `nx` contains 'F' if either `i` or `j` is in the first `n // 4 - 1` elements of `sa`, otherwise it contains 'S'. If `len(sa) < len(sb)`, for each position `i` from 1 to `n`, if `a[i]` and `b[i]` are both 0, `sb` now includes the index `i`, otherwise the values of `a[i]` and `b[i]` remain unchanged. `nx` is a string of length `n` constructed for each `i` from 1 to `n` by iterating through `xx[i]` from index 0 to `n - 1`. For each character in `xx[i]`, if it is not `?`, it is appended to `nx`. If it is `?` and either `i` or `j` is in the first `n // 4 - 1` elements of `sb`, 'S' is appended to `nx`. Otherwise, 'F' is appended to `nx`.
#Overall this is what the function does:The function `func` reads an integer `n` and a list of `n` strings, each containing `n` characters. The characters can be 'F', 'S', '?', or '.', and the input matrix is symmetric with the diagonal always being '.'. The function processes the input matrix to determine the positions of 'F' and 'S' based on the cumulative counts of these characters in each row and column. It then updates the '?' characters in the matrix based on the following rules: If the number of positions with 'F' (but no 'S') is greater than or equal to the number of positions with 'S' (but no 'F'), the '?' characters in the first `n // 4 - 1` positions of the 'F' list are replaced with 'F', and the rest are replaced with 'S'. Otherwise, the '?' characters in the first `n // 4 - 1` positions of the 'S' list are replaced with 'S', and the rest are replaced with 'F'. The function prints the updated matrix.

