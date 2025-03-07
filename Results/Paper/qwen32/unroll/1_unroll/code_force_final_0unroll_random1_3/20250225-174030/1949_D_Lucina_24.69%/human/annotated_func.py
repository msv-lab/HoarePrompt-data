#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input consists of n lines, each containing n characters. The j-th character of the i-th line is either 'F' (funny), 'S' (scary), '?' (undecided), or '.' if i=j. The i-th character of the j-th line is the same as the j-th character of the i-th line for all i and j. There are at most floor(n/2) 'F' or 'S' characters in the input.
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
        
    #State: `a` is a list where each element at index `i` (1 to n) contains the count of 'F' characters in the i-th row and column, `b` is a list where each element at index `i` (1 to n) contains the count of 'S' characters in the i-th row and column, and `xx` is a list containing an empty string followed by all the input lines.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `a` is a list where each element at index `i` (1 to n) contains the count of 'F' characters in the i-th row and column, `b` is a list where each element at index `i` (1 to n) contains the count of 'S' characters in the i-th row and column, `xx` is a list containing an empty string followed by all the input lines, `sa` is a list containing indices where there are 'F' characters but no 'S' characters, `sb` is a list containing indices where there are 'S' characters but no 'F' characters.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `a` is a list where each element at index `i` (1 to n) contains the count of 'F' characters in the i-th row and column, `b` is a list where each element at index `i` (1 to n) contains the count of 'S' characters in the i-th row and column, `xx` is a list containing an empty string followed by all the input lines, `sa` is a list containing indices where there are 'F' characters but no 'S' characters, plus any additional indices where there are neither 'F' nor 'S' characters, and `sb` is a list containing indices where there are 'S' characters but no 'F' characters.
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
            
        #State: `a` is a list where each element at index `i` (1 to n) contains the count of 'F' characters in the i-th row and column, `b` is a list where each element at index `i` (1 to n) contains the count of 'S' characters in the i-th row and column, `xx` is a list containing an empty string followed by all the input lines, `sa` is a list containing indices where there are 'F' characters but no 'S' characters, plus any additional indices where there are neither 'F' nor 'S' characters, and `sb` is a list containing indices where there are 'S' characters but no 'F' characters.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `a` is a list where each element at index `i` (1 to n) contains the count of 'F' characters in the i-th row and column, `b` is a list where each element at index `i` (1 to n) contains the count of 'S' characters in the i-th row and column, `xx` is a list containing an empty string followed by all the input lines, `sa` is a list containing indices where there are 'F' characters but no 'S' characters, `sb` is a list containing indices where there are 'S' characters but no 'F' characters, extended by indices where both `a[i]` and `b[i]` are zero.
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
            
        #State: `xx` list with '?' characters replaced by 'S' in the first `n // 4` rows or columns specified in `sb`, and by 'F' elsewhere; `a`, `b`, `sa`, and `sb` lists remain unchanged.
    #State: `a` is a list where each element at index `i` (1 to n) contains the count of 'F' characters in the i-th row and column, `b` is a list where each element at index `i` (1 to n) contains the count of 'S' characters in the i-th row and column, `xx` is a list containing an empty string followed by all the input lines. If `len(sa) >= len(sb)`, then `sa` includes additional indices where there are neither 'F' nor 'S' characters. Otherwise, `xx` has '?' characters replaced by 'S' in the first `n // 4` rows or columns specified in `sb`, and by 'F' elsewhere. `sa` and `sb` remain unchanged in the else case.
#Overall this is what the function does:The function reads an integer `n` and an `n x n` matrix where each cell is either 'F' (funny), 'S' (scary), '?' (undecided), or '.' (if the row index equals the column index). It processes the matrix to replace '?' with 'F' or 'S' based on the counts of 'F' and 'S' in each row and column, and prints the modified matrix. If there are more or equal 'F' counts without 'S' compared to 'S' counts without 'F', it prioritizes 'F' for undecided cells in the first `n // 4` rows or columns identified as having only 'F'. Otherwise, it prioritizes 'S'.

