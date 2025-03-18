#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input is a list of n strings, where each string has n characters. The j-th character of the i-th string is either 'F', 'S', '?', or '.', and the i-th character of the j-th string is the same as the j-th character of the i-th string for all i and j. The number of 'F' and 'S' characters in the input is at most floor(n/2).
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
        
    #State: - `a` will be a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'F' characters in the i-th row (or column) of the input matrix.
    #- `b` will be a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'S' characters in the i-th row (or column) of the input matrix.
    #- `xx` will be a list containing an empty string followed by all the strings from the input list.
    #
    #Output State:
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `a` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'F' characters in the i-th row (or column) of the input matrix; `b` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'S' characters in the i-th row (or column) of the input matrix; `xx` is a list containing an empty string followed by all the strings from the input list; `sa` is a list of indices of rows (or columns) with 'F' characters but no 'S' characters; `sb` is a list of indices of rows (or columns) with 'S' characters but no 'F' characters.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `a` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'F' characters in the i-th row (or column) of the input matrix; `b` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'S' characters in the i-th row (or column) of the input matrix; `xx` is a list containing an empty string followed by all the strings from the input list; `sa` is a list of indices of rows (or columns) with 'F' characters but no 'S' characters, plus any additional indices of rows (or columns) that have neither 'F' nor 'S' characters; `sb` is a list of indices of rows (or columns) with 'S' characters but no 'F' characters. The length of `sa` is still greater than or equal to the length of `sb`.
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
            
        #State: `a` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'F' characters in the i-th row (or column) of the input matrix; `b` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'S' characters in the i-th row (or column) of the input matrix; `xx` is a list containing an empty string followed by all the strings from the input list; `sa` is a list of indices of rows (or columns) with 'F' characters but no 'S' characters, plus any additional indices of rows (or columns) that have neither 'F' nor 'S' characters; `sb` is a list of indices of rows (or columns) with 'S' characters but no 'F' characters. The length of `sa` is still greater than or equal to the length of `sb`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `a` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'F' characters in the i-th row (or column) of the input matrix; `b` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'S' characters in the i-th row (or column) of the input matrix; `xx` is a list containing an empty string followed by all the strings from the input list; `sa` is a list of indices of rows (or columns) with 'F' characters but no 'S' characters; `sb` is a list of indices of rows (or columns) with 'S' characters but no 'F' characters, updated to include indices where both `a[i]` and `b[i]` are 0.
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
            
        #State: `a` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'F' characters in the i-th row (or column) of the input matrix; `b` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'S' characters in the i-th row (or column) of the input matrix; `xx` is a list containing an empty string followed by all the strings from the input list with '?' characters replaced by 'S' or 'F' based on the conditions in the loop; `sa` is a list of indices of rows (or columns) with 'F' characters but no 'S' characters; `sb` is a list of indices of rows (or columns) with 'S' characters but no 'F' characters, updated to include indices where both `a[i]` and `b[i]` are 0.
    #State: `a` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'F' characters in the i-th row (or column) of the input matrix; `b` is a list of `n + 1` integers where the i-th element (for i from 1 to n) is the total number of 'S' characters in the i-th row (or column) of the input matrix; `xx` is a list containing an empty string followed by all the strings from the input list, with '?' characters replaced by 'S' or 'F' based on the conditions in the loop if `len(sa) < len(sb)`, otherwise `xx` remains unchanged; `sa` is a list of indices of rows (or columns) with 'F' characters but no 'S' characters, plus any additional indices of rows (or columns) that have neither 'F' nor 'S' characters if `len(sa) >= len(sb)`, otherwise it includes indices where both `a[i]` and `b[i]` are 0; `sb` is a list of indices of rows (or columns) with 'S' characters but no 'F' characters, updated to include indices where both `a[i]` and `b[i]` are 0 if `len(sa) < len(sb)`, otherwise it remains unchanged. If `len(sa) >= len(sb)`, the length of `sa` is still greater than or equal to the length of `sb`.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` strings, each of length `n`, containing characters 'F', 'S', '?', or '.', and prints a modified version of the list where '?' characters are replaced by 'F' or 'S' based on specific rules involving the counts of 'F' and 'S' characters in each row and column.

