#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 24. The input is a list of n strings, each of length n, where each character is either 'F', 'S', '?', or '.'. The character at the i-th row and j-th column is the same as the character at the j-th row and i-th column for all i and j. The diagonal characters (i.e., where i = j) are always '.'. At most \lfloor \frac{n}{2} \rfloor transition videos are already decided, meaning at most 2\lfloor \frac{n}{2} \rfloor characters in the input are 'F' or 'S'.
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
        
    #State: After the loop executes all iterations, the list `xx` will contain `n + 1` strings, where the first string is an empty string and the remaining `n` strings are the input strings provided. The list `a` will contain the counts of 'F' characters for each row (and column) of the input matrix, and the list `b` will contain the counts of 'S' characters for each row (and column) of the input matrix. The initial state of `n` remains unchanged.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: After the loop executes all iterations, the list `xx` will contain `n + 1` strings, where the first string is an empty string and the remaining `n` strings are the input strings provided. The list `a` will contain the counts of 'F' characters for each row (and column) of the input matrix, and the list `b` will contain the counts of 'S' characters for each row (and column) of the input matrix. The initial state of `n` remains unchanged. The list `sa` will contain the indices of rows (and columns) where there is at least one 'F' character and no 'S' characters. The list `sb` will contain the indices of rows (and columns) where there is at least one 'S' character and no 'F' characters.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: The list `sa` will contain the indices of rows (and columns) where there is at least one 'F' character and no 'S' characters, as well as the indices of rows (and columns) where there are no 'F' or 'S' characters. The list `sb` will remain unchanged. The length of `sa` will be greater than or equal to the length of `sb`. The value of `t` will be equal to the length of `sa` after the loop has finished executing. The value of `n` remains unchanged.
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
            
        #State: The list `sa` remains unchanged. The list `sb` remains unchanged. The value of `t` is equal to the length of `sa`. The value of `n` remains unchanged. The loop prints a modified version of each row in `xx`, where any '?' character is replaced with 'F' if the row or column index is in the first quarter of `sa`, and with 'S' otherwise.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: The list `xx` remains unchanged. The list `a` and `b` remain unchanged. The list `sa` remains unchanged. The list `sb` will contain the indices of rows (and columns) where there is at least one 'S' character and no 'F' characters, as well as the indices of rows (and columns) where there are no 'F' characters and no 'S' characters. The value of `n` remains unchanged.
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
            
        #State: The list `xx` remains unchanged. The list `a` and `b` remain unchanged. The list `sa` remains unchanged. The list `sb` will contain the indices of rows (and columns) where there is at least one 'S' character and no 'F' characters, as well as the indices of rows (and columns) where there are no 'F' characters and no 'S' characters. The value of `n` remains unchanged.
    #State: The initial state of `n` remains unchanged. If the length of `sa` is greater than or equal to the length of `sb`, the list `sa` and `sb` remain unchanged, and the value of `t` is equal to the length of `sa`. The loop prints a modified version of each row in `xx`, where any '?' character is replaced with 'F' if the row or column index is in the first quarter of `sa`, and with 'S' otherwise. If the length of `sa` is less than the length of `sb`, the list `xx` remains unchanged, the list `a` and `b` remain unchanged, the list `sa` remains unchanged, and the list `sb` will contain the indices of rows (and columns) where there is at least one 'S' character and no 'F' characters, as well as the indices of rows (and columns) where there are no 'F' characters and no 'S' characters.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` strings, each of length `n`, where the characters are either 'F', 'S', '?', or '.'. It then processes this input to identify rows (and columns) that contain 'F' or 'S' characters, and stores these counts in lists `a` and `b` respectively. The function then determines the indices of rows (and columns) that have only 'F' characters (stored in `sa`) and those that have only 'S' characters (stored in `sb`). If the number of 'F' rows is greater than or equal to the number of 'S' rows, it appends indices of rows with no 'F' or 'S' characters to `sa` and prints a modified version of the input matrix where '?' characters are replaced with 'F' if the row or column index is in the first quarter of `sa`, and with 'S' otherwise. If the number of 'F' rows is less than the number of 'S' rows, it appends indices of rows with no 'F' or 'S' characters to `sb` and prints a modified version of the input matrix where '?' characters are replaced with 'S' if the row or column index is in the first quarter of `sb`, and with 'F' otherwise. The function does not return any value; it only prints the modified matrix.

