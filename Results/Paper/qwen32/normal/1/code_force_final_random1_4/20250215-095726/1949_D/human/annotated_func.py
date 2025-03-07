#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 24. The input consists of n lines, each containing n characters. The j-th character of the i-th line is 'F' if the transition video between scenarios i and j is funny, 'S' if it is scary, '?' if it is undecided, or '.' if i = j. The i-th character of the j-th line is the same as the j-th character of the i-th line for all i and j. There are at most ⌊n/2⌋ characters in the input that are 'F' or 'S'.
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
        
    #State: `a` contains cumulative counts of 'F' transitions, `b` contains cumulative counts of 'S' transitions, `xx` contains `n + 1` elements starting with an empty string followed by the `n` input strings.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `a` contains cumulative counts of 'F' transitions, `b` contains cumulative counts of 'S' transitions, `xx` contains `n + 1` elements starting with an empty string followed by the `n` input strings, `sa` contains indices `i` where `a[i] > 0` and `b[i] == 0`, and `sb` contains indices `i` where `b[i] > 0` and `a[i] == 0`.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `a` contains cumulative counts of 'F' transitions, `b` contains cumulative counts of 'S' transitions, `xx` contains `n + 1` elements starting with an empty string followed by the `n` input strings, `sa` contains all indices `i` from 1 to `n` where `a[i] == 0` and `b[i] == 0`, and `sb` contains indices `i` where `b[i] > 0` and `a[i] == 0`.
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
            
        #State: aFbScSdSaFbScSdSaFbScSdS... (repeated n times)
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `a` contains cumulative counts of 'F' transitions, `b` contains cumulative counts of 'S' transitions, `xx` contains `n + 1` elements starting with an empty string followed by the `n` input strings, `sa` contains indices `i` where `a[i] > 0` and `b[i] == 0`, and `sb` contains indices `i` where `a[i] == 0` and `b[i] == 0`.
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
            
        #State: A list of `n` strings, each of length `n`, where each character is either directly from `xx[i][j-1]` or determined by the conditions involving `sb`.
    #State: `a` contains cumulative counts of 'F' transitions, `b` contains cumulative counts of 'S' transitions, `xx` contains `n + 1` elements starting with an empty string followed by the `n` input strings, `sa` contains indices `i` where `a[i] > 0` and `b[i] == 0`, and `sb` contains indices `i` where `b[i] > 0` and `a[i] == 0`. If the length of `sa` is greater than or equal to the length of `sb`, the sequence "aFbScSdSaFbScSdSaFbScSdS..." is repeated `n` times. Otherwise, a list of `n` strings, each of length `n`, is created where each character is either directly from `xx[i][j-1]` or determined by the conditions involving `sb`.
#Overall this is what the function does:The function reads an integer `n` and an `n x n` matrix representing the nature of transition videos between scenarios. It processes this matrix to replace '?' with either 'F' or 'S' based on certain conditions. The function then prints `n` strings, each of length `n`, where each character is either directly from the input matrix or determined by the processing rules.

