#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input is a list of n strings, each of length n, where each character is either 'F', 'S', '?', or '.'. The character at the i-th row and j-th column is the same as the character at the j-th row and i-th column for all i and j, and the character at the i-th row and i-th column is always '.'. At most \lfloor \frac{n}{2} \rfloor transition videos are already decided, meaning at most 2\lfloor \frac{n}{2} \rfloor characters in the input are 'F' or 'S'.
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
        
    #State: The list `xx` contains `n + 1` strings, where the first string is empty and the next `n` strings are the input strings. The lists `a` and `b` are of length `n + 1`, with `a[i]` and `b[i]` containing the counts of 'F' and 'S' characters, respectively, in the i-th row (and column) of the input matrix for all 1 <= i <= n. The elements at index 0 of `a` and `b` remain 0.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: The list `sa` contains the indices of all rows (1 to n) where the count of 'F' characters is greater than 0 and the count of 'S' characters is 0. The list `sb` contains the indices of all rows (1 to n) where the count of 'S' characters is greater than 0 and the count of 'F' characters is 0. The list `xx`, and the lists `a` and `b` remain unchanged.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: The list `sa` now contains the indices of all rows (1 to n) where the count of 'F' characters is greater than 0 and the count of 'S' characters is 0, as well as the indices of all rows (1 to n) where both `a[i]` and `b[i]` are 0. The list `sb` remains unchanged. The list `xx`, and the lists `a` and `b` remain unchanged. The length of `sa` is now greater than or equal to its initial length, and `t` is still equal to the initial length of `sa`.
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
            
        #State: The list `sa` remains unchanged. The list `sb` remains unchanged. The list `xx`, and the lists `a` and `b` remain unchanged. The length of `sa` is still greater than or equal to its initial length, and `t` is still equal to the initial length of `sa`. The loop prints a string `nx` for each row `i` from 1 to `n`. Each `nx` string is constructed by iterating through the characters of the corresponding row in `xx`. If a character is not '?', it is appended to `nx`. If a character is '?', and the row index `i` or column index `j` is in the first `n // 4 - 1` elements of `sa`, 'F' is appended to `nx`. Otherwise, 'S' is appended to `nx`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: The list `sb` will contain the indices of all rows (1 to n) where the count of 'S' characters is greater than 0 and the count of 'F' characters is 0, as well as the indices of all rows (1 to n) where both `a[i]` and `b[i]` are 0. The list `sa` and the lists `xx`, `a`, and `b` will remain unchanged. The length of `sa` will still be less than the length of `sb`.
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
            
        #State: The list `sb` will contain the indices of all rows (1 to n) where the count of 'S' characters is greater than 0 and the count of 'F' characters is 0, as well as the indices of all rows (1 to n) where both `a[i]` and `b[i]` are 0. The list `sa` and the lists `xx`, `a`, and `b` will remain unchanged. The length of `sa` will still be less than the length of `sb`. After the loop, the printed output will be a series of strings `nx` where each string `nx` is constructed by replacing '?' characters in `xx[i]` with 'S' if the row index `i` or column index `j` is in the first quarter of `sb`, and with 'F' otherwise.
    #State: The list `sa` contains the indices of all rows (1 to n) where the count of 'F' characters is greater than 0 and the count of 'S' characters is 0. The list `sb` contains the indices of all rows (1 to n) where the count of 'S' characters is greater than 0 and the count of 'F' characters is 0. The lists `xx`, `a`, and `b` remain unchanged. If `len(sa) >= len(sb)`, the loop prints a string `nx` for each row `i` from 1 to `n`. Each `nx` string is constructed by iterating through the characters of the corresponding row in `xx`. If a character is not '?', it is appended to `nx`. If a character is '?', and the row index `i` or column index `j` is in the first `n // 4 - 1` elements of `sa`, 'F' is appended to `nx`. Otherwise, 'S' is appended to `nx`. If `len(sa) < len(sb)`, the list `sb` will also include the indices of all rows (1 to n) where both `a[i]` and `b[i]` are 0. The loop prints a string `nx` for each row `i` from 1 to `n`. Each `nx` string is constructed by iterating through the characters of the corresponding row in `xx`. If a character is not '?', it is appended to `nx`. If a character is '?', and the row index `i` or column index `j` is in the first quarter of `sb`, 'S' is appended to `nx`. Otherwise, 'F' is appended to `nx`.
#Overall this is what the function does:The function `func` processes a symmetric matrix of size n x n, where n is an integer between 2 and 24, and each element is one of 'F', 'S', '?', or '.', with the diagonal elements always being '.'. It reads the matrix from user input and counts the occurrences of 'F' and 'S' in each row (and column) of the matrix. The function then categorizes rows into two lists, `sa` and `sb`, where `sa` contains rows with 'F' characters but no 'S' characters, and `sb` contains rows with 'S' characters but no 'F' characters. If the length of `sa` is greater than or equal to the length of `sb`, it appends rows with no 'F' or 'S' characters to `sa`. Otherwise, it appends these rows to `sb`. Finally, it prints a modified version of the matrix, replacing '?' characters with 'F' or 'S' based on the content of `sa` or `sb` and the position of the '?' in the matrix. The function does not return any value, but it modifies and prints the matrix.

