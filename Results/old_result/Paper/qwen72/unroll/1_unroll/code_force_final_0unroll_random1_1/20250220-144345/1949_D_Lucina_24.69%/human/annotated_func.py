#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input is a list of n strings, each of length n, where each string represents a row in the transition video plan. The characters in these strings are either 'F' for funny, 'S' for scary, '?' for undecided, or '.' for the diagonal (i.e., the transition from a scenario to itself). It is guaranteed that the matrix is symmetric and that at most \lfloor \frac{n}{2} \rfloor transition videos are already decided, meaning at most 2\lfloor \frac{n}{2} \rfloor characters in the input will be 'F' or 'S'.
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
        
    #State: The list `a` will contain the count of 'F' (funny) transitions for each row and column, the list `b` will contain the count of 'S' (scary) transitions for each row and column, and the list `xx` will contain the input strings, with the first element being an empty string. The variable `n` and the input matrix will remain unchanged.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: The list `sa` will contain the indices of rows and columns where there are 'F' (funny) transitions but no 'S' (scary) transitions. The list `sb` will contain the indices of rows and columns where there are 'S' (scary) transitions but no 'F' (funny) transitions. The lists `a`, `b`, `xx`, and the variable `n` will remain unchanged.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: The list `sa` will now contain the indices of rows and columns where there are 'F' (funny) transitions but no 'S' (scary) transitions, as well as any additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0. The list `sb` will remain unchanged. The lists `a`, `b`, `xx`, and the variable `n` will also remain unchanged.
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
            
        #State: Output State: The list `sa` will now contain the indices of rows and columns where there are 'F' (funny) transitions but no 'S' (scary) transitions, as well as any additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0. The list `sb` will remain unchanged. The lists `a`, `b`, `xx`, and the variable `n` will also remain unchanged. The loop will print a series of strings `nx` for each row `i` from 1 to `n`, where each string `nx` is constructed by replacing '?' characters in `xx[i]` with 'F' if the row or column index is in the first quarter of `sa`, and with 'S' otherwise.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: The list `sa` will remain unchanged. The list `sb` will contain the indices of rows and columns where there are 'S' (scary) transitions but no 'F' (funny) transitions, as well as any additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0. The lists `a`, `b`, and `xx`, and the variable `n` will remain unchanged.
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
            
        #State: The list `sa` remains unchanged. The list `sb` remains unchanged. The lists `a`, `b`, and `xx`, and the variable `n` remain unchanged. The loop prints a series of strings `nx` for each row `i` from 1 to `n`. Each string `nx` is constructed by iterating through the columns `j` from 1 to `n`. If the element `xx[i][j - 1]` is not '?', it is appended to `nx`. If `xx[i][j - 1]` is '?' and `i` or `j` is in the first quarter of `sb`, 'S' is appended to `nx`. Otherwise, 'F' is appended to `nx`.
    #State: The lists `a`, `b`, `xx`, and the variable `n` remain unchanged. The lists `sa` and `sb` will also remain unchanged. If `len(sa) >= len(sb)`, the list `sa` will now contain the indices of rows and columns where there are 'F' (funny) transitions but no 'S' (scary) transitions, as well as any additional indices `i` from 1 to `n` where both `a[i]` and `b[i]` are 0. The loop will print a series of strings `nx` for each row `i` from 1 to `n`, where each string `nx` is constructed by replacing '?' characters in `xx[i]` with 'F' if the row or column index is in the first quarter of `sa`, and with 'S' otherwise. If `len(sa) < len(sb)`, the loop prints a series of strings `nx` for each row `i` from 1 to `n`. Each string `nx` is constructed by iterating through the columns `j` from 1 to `n`. If the element `xx[i][j - 1]` is not '?', it is appended to `nx`. If `xx[i][j - 1]` is '?' and `i` or `j` is in the first quarter of `sb`, 'S' is appended to `nx`. Otherwise, 'F' is appended to `nx`.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` strings, each of length `n`, representing a transition video plan. It processes this plan to determine the counts of 'F' (funny) and 'S' (scary) transitions for each row and column. The function then identifies rows and columns that have only 'F' transitions or only 'S' transitions. Based on the counts, it either adds undecided rows and columns to the list of 'F' transitions or to the list of 'S' transitions. Finally, it prints a modified transition video plan where '?' characters are replaced with 'F' or 'S' based on the identified rows and columns. The function does not return any value.

