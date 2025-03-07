#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 24. The input consists of n lines, where each line contains n characters. The j-th character of the i-th line represents the transition video between the i-th and j-th scenarios and can be 'F' (funny), 'S' (scary), '?' (undecided), or '.' (i=j). It is guaranteed that the i-th character of the j-th line is the same as the j-th character of the i-th line for all i and j. At most ⌊n/2⌋ transition videos are already decided (i.e., at most 2⌊n/2⌋ characters in the input are 'F' or 'S').
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
        
    #State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length `n + 1` with elements incremented based on the number of 'F' connections in the input strings, `b` is a list of length `n + 1` with elements incremented based on the number of 'S' connections in the input strings, and `xx` is a list containing an empty string followed by all `n` input strings.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length `n + 1` with elements incremented based on the number of 'F' connections in the input strings, `b` is a list of length `n + 1` with elements incremented based on the number of 'S' connections in the input strings, and `xx` is a list containing an empty string followed by all `n` input strings. `sa` is a list containing all indices `i` (1 ≤ i ≤ n) where `a[i] > 0` and `b[i] == 0`. `sb` is a list containing all indices `i` (1 ≤ i ≤ n) where `b[i] > 0` and `a[i] == 0`.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length `n + 1` with elements incremented based on the number of 'F' connections in the input strings, `b` is a list of length `n + 1` with elements incremented based on the number of 'S' connections in the input strings, `xx` is a list containing an empty string followed by all `n` input strings, `sa` is a list containing all indices `i` (1 ≤ i ≤ n) where `a[i] > 0` and `b[i] == 0`, or `a[i] == 0` and `b[i] == 0`, and `sb` is a list containing all indices `i` (1 ≤ i ≤ n) where `b[i] > 0` and `a[i] == 0`. The length of `sa` is greater than or equal to the length of `sb`.
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
            
        #State: ['FFSF', 'FFFF', 'SFFF', 'SSSS']
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length `n + 1` with elements incremented based on the number of 'F' connections in the input strings, `b` is a list of length `n + 1` with elements incremented based on the number of 'S' connections in the input strings, and `xx` is a list containing an empty string followed by all `n` input strings. `sa` is a list containing all indices `i` (1 ≤ i ≤ n) where `a[i] > 0` and `b[i] == 0`. `sb` is a list containing all indices `i` (1 ≤ i ≤ n) where `b[i] > 0` and `a[i] == 0`, or where both `a[i]` and `b[i]` are zero. The length of `sa` is less than the length of `sb`.
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
            
        #State: n strings, each of length n, constructed by replacing '?' in xx[i] with 'S' or 'F' based on the conditions involving sb[:n // 4].
    #State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length `n + 1` with elements incremented based on the number of 'F' connections in the input strings, `b` is a list of length `n + 1` with elements incremented based on the number of 'S' connections in the input strings, and `xx` is a list containing an empty string followed by all `n` input strings. `sa` is a list containing all indices `i` (1 ≤ i ≤ n) where `a[i] > 0` and `b[i] == 0`. `sb` is a list containing all indices `i` (1 ≤ i ≤ n) where `b[i] > 0` and `a[i] == 0`. If the length of `sa` is greater than or equal to the length of `sb`, the program processes the input strings as specified in the if part. Otherwise, the program constructs `n` strings, each of length `n`, by replacing '?' in `xx[i]` with 'S' or 'F' based on the conditions involving `sb[:n // 4]`.
#Overall this is what the function does:The function reads an integer `n` and an `n x n` matrix representing transition videos between scenarios. Each element in the matrix can be 'F' (funny), 'S' (scary), '?' (undecided), or '.' (no transition needed when i=j). It then outputs a modified version of the matrix where all '?' are replaced with either 'F' or 'S' to ensure that at most ⌊n/2⌋ transitions are either 'F' or 'S', while maintaining symmetry and consistency across the matrix.

