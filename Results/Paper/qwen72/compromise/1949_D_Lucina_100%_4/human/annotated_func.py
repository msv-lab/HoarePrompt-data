#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input is a list of n strings, each of length n, where each character is either 'F', 'S', '?', or '.'. The character at position (i, j) is the same as the character at position (j, i), and the character at position (i, i) is always '.'. At most \lfloor \frac{n}{2} \rfloor transition videos are already decided, meaning at most 2\lfloor \frac{n}{2} \rfloor characters in the input are 'F' or 'S'.
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
        
    #State: The list `xx` contains `n + 1` strings, where the first string is empty and the next `n` strings are the inputs provided by the user. The list `a` contains the counts of 'F' characters for each row and column, and the list `b` contains the counts of 'S' characters for each row and column. The initial state of `n` remains unchanged.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: The list `xx` remains unchanged, containing `n + 1` strings where the first string is empty and the next `n` strings are the inputs provided by the user. The list `a` and `b` also remain unchanged, containing the counts of 'F' and 'S' characters for each row and column, respectively. The list `sa` now contains the indices of the rows or columns where the count of 'F' characters is greater than 0 and the count of 'S' characters is 0. The list `sb` now contains the indices of the rows or columns where the count of 'S' characters is greater than 0 and the count of 'F' characters is 0. The value of `n` remains unchanged.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: The list `xx` remains unchanged, containing `n + 1` strings where the first string is empty and the next `n` strings are the inputs provided by the user. The list `a` and `b` also remain unchanged, containing the counts of 'F' and 'S' characters for each row and column, respectively. The list `sa` now contains the indices of the rows or columns where the count of 'F' characters is greater than 0 and the count of 'S' characters is 0, as well as the indices of the rows or columns where both the count of 'F' and 'S' characters are 0. The list `sb` remains unchanged, containing the indices of the rows or columns where the count of 'S' characters is greater than 0 and the count of 'F' characters is 0. The value of `n` remains unchanged. The variable `t` is assigned the value of the length of `sa` after the loop has executed.
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
            
        #State: The list `xx` remains unchanged. The list `a` and `b` remain unchanged. The list `sa` remains unchanged. The list `sb` remains unchanged. The value of `n` remains unchanged. The variable `t` is assigned the value of the length of `sa` after the loop has executed. The loop prints a modified version of each row in `xx` where '?' characters are replaced with 'F' if the row or column index is in the first `n // 4 - 1` elements of `sa`, and with 'S' otherwise.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: The list `xx` remains unchanged. The list `a` and `b` remain unchanged. The list `sa` remains unchanged. The list `sb` now contains the indices of the rows or columns where the count of 'S' characters is greater than 0 and the count of 'F' characters is 0, as well as the indices of the rows or columns where both the count of 'F' and 'S' characters are 0. The value of `n` remains unchanged. Additionally, the length of `sa` is still less than the length of `sb`.
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
            
        #State: The list `xx` remains unchanged. The list `a` and `b` remain unchanged. The list `sa` remains unchanged. The list `sb` now contains the indices of the rows or columns where the count of 'S' characters is greater than 0 and the count of 'F' characters is 0, as well as the indices of the rows or columns where both the count of 'F' and 'S' characters are 0. The value of `n` remains unchanged. Additionally, the length of `sa` is still less than the length of `sb`. The loop prints the modified rows of `xx` where '?' characters are replaced with 'S' if the row or column index is in the first quarter of `sb`, and with 'F' otherwise.
    #State: The list `xx` remains unchanged, containing `n + 1` strings where the first string is empty and the next `n` strings are the inputs provided by the user. The list `a` and `b` also remain unchanged, containing the counts of 'F' and 'S' characters for each row and column, respectively. The value of `n` remains unchanged. If the length of `sa` is greater than or equal to the length of `sb`, the variable `t` is assigned the value of the length of `sa` after the loop has executed, and the loop prints a modified version of each row in `xx` where '?' characters are replaced with 'F' if the row or column index is in the first `n // 4 - 1` elements of `sa`, and with 'S' otherwise. If the length of `sa` is less than the length of `sb`, the list `sb` now contains the indices of the rows or columns where the count of 'S' characters is greater than 0 and the count of 'F' characters is 0, as well as the indices of the rows or columns where both the count of 'F' and 'S' characters are 0. The loop prints the modified rows of `xx` where '?' characters are replaced with 'S' if the row or column index is in the first quarter of `sb`, and with 'F' otherwise.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` strings, each of length `n`, from the user. It processes the input to count the occurrences of 'F' and 'S' characters in each row and column, storing these counts in lists `a` and `b`, respectively. The function then identifies rows or columns where 'F' or 'S' characters are exclusively present and stores their indices in lists `sa` and `sb`. If the number of indices in `sa` is greater than or equal to those in `sb`, it modifies and prints each row of the input list by replacing '?' characters with 'F' for the first `n // 4 - 1` elements of `sa`, and with 'S' otherwise. If the number of indices in `sa` is less than those in `sb`, it modifies and prints each row by replacing '?' characters with 'S' for the first `n // 4 - 1` elements of `sb`, and with 'F' otherwise. The original input list and the counts in `a` and `b` remain unchanged throughout the function.

