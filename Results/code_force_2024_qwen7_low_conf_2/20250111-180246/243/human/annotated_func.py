#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 24, and the input consists of n lines where each line contains n characters representing the transition videos between scenarios. The characters can be F (funny), S (scary), ?, . (no transition video yet decided). At most 2⌊n/2⌋ characters in the input are F or S.
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
        
    #State of the program after the  for loop has been executed: `n` is a positive integer; `i` is `n + 1`; `xx` is a list of length `n + 1` where `xx[0]` is `['']` and `xx[k]` (for `k` from `1` to `n`) is the `k`-th input string; `a` is a list of length `n + 1` where each element `a[k]` is the total count of 'F' at position `k-1` in any of the input strings; `b` is a list of length `n + 1` where each element `b[k]` is the total count of 'S' at position `k-1` in any of the input strings.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n + 1`, `xx` is a list of length `n + 1` where `xx[0]` is `['']` and for `k` from `1` to `n`, `xx[k]` is the `k`-th input string, `a` is a list of length `n + 1` where each element `a[k]` is the total count of 'F' at position `k-1` in any of the input strings, `b` is a list of length `n + 1` where each element `b[k]` is the total count of 'S' at position `k-1` in any of the input strings, `sa` is a list containing all indices `k` where `b[k] > 0` and `a[k] == 0`, and `sb` is a list containing all indices `k` where `a[k] > 0` and `b[k] == 0`.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State of the program after the  for loop has been executed: `n` is a positive integer, `i` is `n + 1`, `xx` is a list of length `n + 1` where `xx[0] = ['']` and for `k` from `1` to `n`, `xx[k]` is the `k`-th input string, `a` is a list of length `n + 1` where each element `a[k]` is the total count of 'F' at position `k-1` in any of the input strings, `b` is a list of length `n + 1` where each element `b[k]` is the total count of 'S' at position `k-1` in any of the input strings, `sa` is a list of all indices `i` from `1` to `n` for which `a[i] == 0` and `b[i] == 0`, and `t` is the length of `sa`.
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
            
        #State of the program after the  for loop has been executed: `i` is `n + 1`, `j` is `n + 1`, `nx` is a string constructed by processing each character in `xx[i][j-1]` for all `i` and `j` according to the specified rules, and `nx` is printed for each iteration. `sa` remains unchanged and `t` is the length of `sa`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State of the program after the  for loop has been executed: - `n` is a positive integer.
        #- `i` is `n + 1`.
        #- `xx` is a list of length `n + 1` where `xx[0]` is `['']`.
        #- `a` and `b` are lists of length `n + 1` where the values of `a[i]` and `b[i]` remain unchanged.
        #- `sa` is an empty list.
        #- `sb` is a list containing all indices from `1` to `n` if the loop executes for all iterations, otherwise `sb` is an empty list.
        #- `(len(sa) < len(sb))` still holds true if the loop executes for all iterations, otherwise `(len(sa) == 0 and len(sb) == 0)`.
        #
        #Thus, the final output state is:
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
            
        #State of the program after the  for loop has been executed: `i` is `n + 1`, `j` is `n + 1`, `xx` is a list of length `n + 1` where `xx[0]` is `['']`, `a` and `b` are lists of length `n + 1` with unchanged values, `sa` is an empty list, `sb` is a list containing all indices from `1` to `n`, `(len(sa) < len(sb))` still holds true, and `nx` is a string consisting of 'S' and 'F' based on the condition that if `i` or `j` is in the first quarter of `sb`, then 'S' is appended, otherwise 'F' is appended. `nx` is printed.
    #State of the program after the if-else block has been executed: *`i` is `n + 1`, `j` is `n + 1`, `xx` is a list of length `n + 1` where `xx[0]` is `['']`, `a` and `b` are lists of length `n + 1` with unchanged values, `sa` and `sb` are lists of indices based on the conditions given, and `nx` is a string constructed as follows: 
    #- If `len(sa) >= len(sb)`, `nx` is constructed by processing each character in `xx[i][j-1]` for all `i` and `j` according to the specified rules, and `nx` is printed for each iteration. `sa` remains unchanged and `t` is the length of `sa`.
    #- If `len(sa) < len(sb)`, `nx` is a string consisting of 'S' and 'F' based on the condition that if `i` or `j` is in the first quarter of `sb`, then 'S' is appended, otherwise 'F' is appended. `nx` is printed.
#Overall this is what the function does:The function `func` accepts a matrix of characters representing transitions between scenarios, where each line contains `n` characters and `n` is an integer such that 2 ≤ n ≤ 24. The characters can be 'F' (funny), 'S' (scary), '?', or '.' (no transition video yet decided). At most 2⌊n/2⌋ characters in the input are 'F' or 'S'. The function processes this input to determine if certain conditions are met and constructs a new matrix of characters based on these conditions.

