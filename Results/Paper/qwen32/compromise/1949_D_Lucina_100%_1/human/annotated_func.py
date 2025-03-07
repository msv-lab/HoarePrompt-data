#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input consists of n lines, where each line contains n characters. The j-th character of the i-th line is either 'F' (funny), 'S' (scary), '?' (undecided), or '.' (same scenario). The i-th character of the j-th line is the same as the j-th character of the i-th line for all i and j. At most floor(n/2) characters in the input are 'F' or 'S'.
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
        
    #State: `a` is a list of length `n + 1` with counts of 'F' characters per column, `b` is a list of length `n + 1` with counts of 'S' characters per column, and `xx` is a list containing an empty string followed by the `n` lines of input.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `a` is a list of length `n + 1` with counts of 'F' characters per column, `b` is a list of length `n + 1` with counts of 'S' characters per column, `xx` is a list containing an empty string followed by the `n` lines of input, `sa` is a list containing indices `i` from 1 to `n` where `a[i] > 0` and `b[i] == 0`, and `sb` is a list containing indices `i` from 1 to `n` where `b[i] > 0` and `a[i] == 0`.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `a` is a list of length `n + 1` with counts of 'F' characters per column, `b` is a list of length `n + 1` with counts of 'S' characters per column, `xx` is a list containing an empty string followed by the `n` lines of input, `sa` is a list containing indices `i` from 1 to `n` where `a[i] > 0` and `b[i] == 0`, and additionally all indices `i` from 1 to `n` where `a[i] == 0` and `b[i] == 0`, `sb` is a list containing indices `i` from 1 to `n` where `b[i] > 0` and `a[i] == 0`, `t` is the length of `sa`.
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
            
        #State: a list of `n` strings, where each string is constructed by replacing '?' in the corresponding row of `xx` with 'F' or 'S' based on the conditions involving `sa` and `sb`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `a` is a list of length `n + 1` with counts of 'F' characters per column, `b` is a list of length `n + 1` with counts of 'S' characters per column, `xx` is a list containing an empty string followed by the `n` lines of input, `sa` is a list containing indices `i` from 1 to `n` where `a[i] > 0` and `b[i] == 0`, and `sb` is a list containing indices `i` from 1 to `n` where `b[i] > 0` and `a[i] == 0`, plus any additional indices `i` where both `a[i] == 0` and `b[i] == 0`. The length of `sa` is still less than the length of `sb`, and `n` is greater than 0.
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
            
        #State: FFF?, FSFS, FFSF, FSFF.
    #State: `a` is a list of length `n + 1` with counts of 'F' characters per column, `b` is a list of length `n + 1` with counts of 'S' characters per column, `xx` is a list containing an empty string followed by the `n` lines of input. If `len(sa) >= len(sb)`, a list of `n` strings is constructed by replacing '?' in the corresponding row of `xx` with 'F' or 'S' based on the conditions involving `sa` and `sb`. Otherwise, the list of strings is `["FFF?", "FSFS", "FFSF", "FSFF"]`. `sa` is a list containing indices `i` from 1 to `n` where `a[i] > 0` and `b[i] == 0`, and `sb` is a list containing indices `i` from 1 to `n` where `b[i] > 0` and `a[i] == 0`.
#Overall this is what the function does:The function takes an integer `n` (where 2 <= n <= 24) and a symmetric grid of `n` lines by `n` characters. Each character in the grid is either 'F' (funny), 'S' (scary), '?' (undecided), or '.' (same scenario). The function replaces each '?' in the grid with either 'F' or 'S' based on the counts of 'F' and 'S' in each row and column, ensuring that the number of 'F' and 'S' characters in the grid does not exceed floor(n/2). It then prints the modified grid.

