#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input consists of n lines, each containing n characters. The j-th character of the i-th line is either 'F', 'S', '?', or '.', representing the transition video type between scenarios i and j, where '?' indicates an undecided video, 'F' indicates a funny video, 'S' indicates a scary video, and '.' indicates i=j. The input guarantees that the i-th character of the j-th line is the same as the j-th character of the i-th line for all i and j, and that at most floor(n/2) transition videos are already decided.
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
        
    #State: `a` is a list of `n + 1` integers where `a[0]` is 0 and `a[i]` (for `i` from 1 to `n`) is the count of 'F's involving the `i`-th position, `b` is a list of `n + 1` integers where `b[0]` is 0 and `b[i]` (for `i` from 1 to `n`) is the count of 'S's involving the `i`-th position, `xx` is a list containing `n + 1` strings, the first being `''` and the rest being the input strings.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `a` is a list of `n + 1` integers where `a[0]` is 0 and `a[i]` (for `i` from 1 to `n`) is the count of 'F's involving the `i`-th position, `b` is a list of `n + 1` integers where `b[0]` is 0 and `b[i]` (for `i` from 1 to `n`) is the count of 'S's involving the `i`-th position, `xx` is a list containing `n + 1` strings, the first being `''` and the rest being the input strings, `sa` is a list of indices where there are 'F's but no 'S's, `sb` is a list of indices where there are 'S's but no 'F's.
    #
    #Output State:
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `a` is a list of `n + 1` integers where `a[0]` is 0 and `a[i]` (for `i` from 1 to `n`) is the count of 'F's involving the `i`-th position, `b` is a list of `n + 1` integers where `b[0]` is 0 and `b[i]` (for `i` from 1 to `n`) is the count of 'S's involving the `i`-th position, `xx` is a list containing `n + 1` strings, the first being `''` and the rest being the input strings, `sa` is a list of indices where there are 'F's but no 'S's plus any indices where both 'F' and 'S' counts are zero, `sb` is a list of indices where there are 'S's but no 'F's, and the length of `sa` is greater than or equal to the length of `sb`, `t` is the length of `sa` before the loop started.
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
            
        #State: `a` is a list of `n + 1` integers where `a[0]` is 0 and `a[i]` (for `i` from 1 to `n`) is the count of 'F's involving the `i`-th position, `b` is a list of `n + 1` integers where `b[0]` is 0 and `b[i]` (for `i` from 1 to `n`) is the count of 'S's involving the `i`-th position, `xx` is a list containing `n + 1` strings, the first being `''` and the rest being the transformed strings based on the presence of '?' characters and the indices in `sa`, `sa` is a list of indices where there are 'F's but no 'S's plus any indices where both 'F' and 'S' counts are zero, `sb` is a list of indices where there are 'S's but no 'F's, and the length of `sa` is greater than or equal to the length of `sb`, `t` is the length of `sa` before the loop started.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `a` is a list of `n + 1` integers where `a[0]` is 0 and `a[i]` (for `i` from 1 to `n`) is the count of 'F's involving the `i`-th position, `b` is a list of `n + 1` integers where `b[0]` is 0 and `b[i]` (for `i` from 1 to `n`) is the count of 'S's involving the `i`-th position, `xx` is a list containing `n + 1` strings, the first being `''` and the rest being the input strings, `sa` is a list of indices where there are 'F's but no 'S's, `sb` is a list of indices where there are 'S's but no 'F's or where there are neither 'F's nor 'S's, and the length of `sa` is less than or equal to the length of `sb`.
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
            
        #State: xx = ['', 'SSFSS', 'SFFFF', 'SSFSS', 'FFFFF', 'FFFFF', 'FFFFF', 'FFFFF']
    #State: `a` is a list of `n + 1` integers where `a[0]` is 0 and `a[i]` (for `i` from 1 to `n`) is the count of 'F's involving the `i`-th position, `b` is a list of `n + 1` integers where `b[0]` is 0 and `b[i]` (for `i` from 1 to `n`) is the count of 'S's involving the `i`-th position, `xx` is a list containing `n + 1` strings, the first being `''`. If the length of `sa` is greater than or equal to the length of `sb`, `xx` contains the transformed strings based on the presence of '?' characters and the indices in `sa`, and `sa` includes any indices where both 'F' and 'S' counts are zero. Otherwise, `xx` is set to `['', 'SSFSS', 'SFFFF', 'SSFSS', 'FFFFF', 'FFFFF', 'FFFFF', 'FFFFF']`. `sa` is a list of indices where there are 'F's but no 'S's, plus any indices where both 'F' and 'S' counts are zero, and `sb` is a list of indices where there are 'S's but no 'F's.
#Overall this is what the function does:The function reads an integer `n` and an `n x n` matrix of characters representing transition video types between scenarios. It then replaces all '?' characters in the matrix with either 'F' or 'S' based on the counts of 'F's and 'S's in each row/column, ensuring that the resulting matrix is valid according to the rules provided. The function outputs the modified matrix.

