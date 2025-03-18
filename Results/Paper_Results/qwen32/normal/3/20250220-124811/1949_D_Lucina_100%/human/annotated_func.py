#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input consists of n lines, each containing n characters. Each character in the i-th line and j-th column is either 'F', 'S', '?', or '.', where '.' occurs only when i = j, 'F' and 'S' denote pre-decided funny and scary transition videos respectively, and '?' denotes an undecided transition video. It is guaranteed that the input matrix is symmetric (i.e., the character at position (i, j) is the same as the character at position (j, i)) and there are at most floor(n/2) pre-decided transition videos ('F' or 'S').
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
        
    #State: `n` is an integer such that 2 <= n <= 24, `a` is a list of length `n + 1` where `a[i]` for `i` from 1 to `n+1` is the total number of 'F' characters in all input strings up to the `i-1` position, `b` is a list of length `n + 1` where `b[i]` for `i` from 1 to `n+1` is the total number of 'S' characters in all input strings up to the `i-1` position, `xx` is a list containing an empty string and all `n` input strings, `i` is `n+1`.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `n` is an integer such that 2 <= n <= 24, `a` is a list of length `n + 1`, `b` is a list of length `n + 1`, `xx` is a list containing an empty string and all `n` input strings, `i` is `n+1`, `sa` is a list of indices where `a[i] > 0` and `b[i] == 0`, and `sb` is a list of indices where `b[i] > 0` and `a[i] == 0`.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `n` is an integer such that 2 <= n <= 24, `a` is a list of length `n + 1`, `b` is a list of length `n + 1`, `xx` is a list containing an empty string and all `n` input strings, `i` is `n + 1`, `sa` is a list of indices where `a[i] > 0` and `b[i] == 0` plus any indices from `1` to `n` where both `a[i] == 0` and `b[i] == 0`, `sb` is a list of indices where `b[i] > 0` and `a[i] == 0`. The length of `sa` is greater than or equal to the length of `sb`. `t` is the length of `sa` before any potential appending of `i`.
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
            
        #State: A sequence of `n + 1` strings, where each string `nx` is of length `n` and constructed by iterating through each character position `j` from `1` to `n` in the string `xx[i]` for `i` from `1` to `n + 1`. Each character in `nx` is determined by the rules provided: if `xx[i][j - 1]` is not `'?'`, then `nx[j - 1]` is `xx[i][j - 1]`; if `xx[i][j - 1]` is `'?'`, then `nx[j - 1]` is `'F'` if either `i` or `j` is in `sa[:n // 4 - 1]`; otherwise, it is `'S'`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `n` is an integer such that 2 <= n <= 24, `a` is a list of length `n + 1`, `b` is a list of length `n + 1`, `xx` is a list containing an empty string and all `n` input strings, `i` is `n+1`, `sa` is a list of indices where `a[i] > 0` and `b[i] == 0`, and `sb` is a list of indices where `b[i] > 0` and `a[i] == 0`. If `a[i] == 0` and `b[i] == 0` for any `i` from 1 to `n`, then those indices are appended to `sb`. The length of `sa` is less than the length of `sb`.
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
            
        #State: After all iterations, `nx` will be a string constructed for each `xx[i]` from `i = 1` to `i = n`. For each `xx[i]`, `nx` will be formed by iterating over each character in `xx[i]` and replacing '?' characters with 'S' or 'F' based on the conditions involving `sb`. The variable `i` will be `n + 1` after the loop completes, and `j` will be `n + 1` at the end of the last iteration. The lists `a`, `b`, `xx`, `sa`, and `sb` will remain unchanged as per the precondition.
    #State: `n` is an integer such that 2 <= n <= 24, `a` is a list of length `n + 1`, `b` is a list of length `n + 1`, `xx` is a list containing an empty string and all `n` input strings, `i` is `n+1`, `sa` is a list of indices where `a[i] > 0` and `b[i] == 0`, and `sb` is a list of indices where `b[i] > 0` and `a[i] == 0`. If the length of `sa` is greater than or equal to the length of `sb`, a sequence of `n + 1` strings, where each string `nx` is of length `n`, is constructed by iterating through each character position `j` from `1` to `n` in the string `xx[i]` for `i` from `1` to `n + 1`. Each character in `nx` is determined by the rules: if `xx[i][j - 1]` is not `'?'`, then `nx[j - 1]` is `xx[i][j - 1]`; if `xx[i][j - 1]` is `'?'`, then `nx[j - 1]` is `'F'` if either `i` or `j` is in `sa[:n // 4 - 1]`; otherwise, it is `'S'`. Otherwise, after all iterations, `nx` will be a string constructed for each `xx[i]` from `i = 1` to `i = n`. For each `xx[i]`, `nx` will be formed by iterating over each character in `xx[i]` and replacing '?' characters with 'S' or 'F' based on the conditions involving `sb`. The variable `i` will be `n + 1` after the loop completes, and `j` will be `n + 1` at the end of the last iteration. The lists `a`, `b`, `xx`, `sa`, and `sb` will remain unchanged as per the precondition.
#Overall this is what the function does:The function accepts an integer `n` and a symmetric `n x n` matrix where each element is either 'F', 'S', '?', or '.', with '.' only on the diagonal. It processes the matrix to replace '?' characters with 'F' or 'S' based on the counts of 'F' and 'S' in each row and column, ensuring that the number of 'F' and 'S' does not exceed `floor(n/2)`. The function then outputs the modified matrix.

