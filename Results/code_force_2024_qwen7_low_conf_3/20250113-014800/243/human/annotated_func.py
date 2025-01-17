#State of the program right berfore the function call: n is an integer where 2 ≤ n ≤ 24, and the input consists of n lines, each containing n characters. The j-th character of the i-th line represents the transition video between the i-th and the j-th scenarios, where F means funny, S means scary, ? means undecided, and . means no transition video (i=j). At most \lfloor \frac{n}{2} \rfloor transition videos are already decided (i.e., at most 2\lfloor \frac{n}{2} \rfloor characters are F or S).
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 24 inclusive, `a` is a list of length `n + 1` where `a[j]` (for `j` from 1 to `n`) is the total count of 'F' at position `j-1` across all inputs, and `a[n+1]` is the total count of 'F' in all inputs; `b` is a list of length `n + 1` where `b[j]` (for `j` from 1 to `n`) is the total count of 'S' at position `j-1` across all inputs, and `b[n+1]` is the total count of 'S' in all inputs; `xx` is a list containing all input strings including the initial `['']`, and `x` is the last input string.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State of the program after the  for loop has been executed: `i` is `n + 1`, `n` is an integer between 2 and 24 inclusive, `a` is a list of integers, `b` is a list of integers, `sa` is a list containing the indices `j` for which `a[j] > 0` and `b[j] == 0`, `sb` is a list containing the indices `j` for which `b[j] > 0` and `a[j] == 0`. If the loop executes `n` times, then `sa` and `sb` will contain all valid indices as described, otherwise, the lists will remain as they were initialized (empty).
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State of the program after the  for loop has been executed: `i` is `n + 1`, `n` is an integer between 2 and 24 inclusive, `a` is a list of integers, `b` is a list of integers, `sa` is a list containing the indices `j` for which `a[j] == 0` and `b[j] == 0`, `sb` is a list containing the indices `j` for which `b[j] > 0` and `a[j] == 0`, `t` is the length of `sa`.
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
            
        #State of the program after the  for loop has been executed: `nx` is a string of length `n`, constructed based on the rules described: if `xx[i][j - 1]` is not `'?'`, it is directly added to `nx`. If `xx[i][j - 1]` is `'?'`, `nx` is appended with `'F'` if either `i` or `j` is in `sa[:n // 4 - 1]`, otherwise it is appended with `'S'`. `i` is `n + 1`, `j` is `n + 1`, and the loop does not execute any more iterations since `i` exceeds `n`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State of the program after the  for loop has been executed: `i` is `n + 1`, `n` is an integer between 2 and 24 inclusive, `a` is a list of integers, `b` is a list of integers, `sa` is a list containing the indices `j` for which `a[j] > 0` and `b[j] == 0`, `sb` is a list containing the indices `j` for which `b[j] > 0` and `a[j] == 0`, the length of `sa` is less than the length of `sb`. After all iterations of the loop, `sa` will contain all indices `j` for which `a[j] > 0` and `b[j] == 0`, and `sb` will contain all indices `j` for which `b[j] > 0` and `a[j] == 0`. If no such indices exist, `sa` will remain an empty list.
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
            
        #State of the program after the  for loop has been executed: `i` is `n + 1`, `j` is `n + 1`, `n` is a positive integer between 2 and 24 inclusive, `xx[i][j - 1]` is either `val` or `?`, and `nx` is the final string constructed based on the conditions within the loop for all iterations.
    #State of the program after the if-else block has been executed: *`i` is `n + 1`, `j` is `n + 1`. If the length of `sa` is greater than or equal to the length of `sb`, then `nx` is constructed according to the specified rules: if `xx[i][j - 1]` is not `'?'`, it is directly added to `nx`. If `xx[i][j - 1]` is `'?'`, `nx` is appended with `'F'` if either `i` or `j` is in `sa[:n // 4 - 1]`, otherwise it is appended with `'S'`. If the length of `sa` is less than the length of `sb`, then `i` and `j` remain unchanged, and `nx` is the final string constructed based on the conditions within the loop for all iterations.
#Overall this is what the function does:The function processes an \(n \times n\) grid of characters representing transition videos between scenarios (F for funny, S for scary, ? for undecided, and . for no transition video). It ensures at most \(\lfloor \frac{n}{2} \rfloor\) transition videos are already decided. The function determines two sets of indices, `sa` and `sb`, which represent indices where only 'F' or only 'S' videos are present, respectively. If the number of indices in `sa` is greater than or equal to the number in `sb`, the function sets the undecided videos ('?') to 'F' under certain conditions. Otherwise, it sets them to 'S'. Finally, it prints the modified grid, where undecided videos have been replaced by 'F' or 'S' according to the conditions described. The function handles the case where \(2 \leq n \leq 24\) and ensures the grid is processed correctly even if no indices in `sa` or `sb` meet the specified conditions. If neither set `sa` nor `sb` contains valid indices, the undecided videos remain unchanged.

