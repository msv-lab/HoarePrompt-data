#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input consists of n lines, each containing n characters. The j-th character of the i-th line is either 'F' (funny), 'S' (scary), '?' (undecided), or '.' (same scenario). The j-th character of the i-th line is the same as the i-th character of the j-th line for all i and j. At most floor(n/2) characters in the input are 'F' or 'S'.
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
        
    #State: - `a` will contain the count of 'F' relationships for each node (including self-loops).
    #   - `b` will contain the count of 'S' relationships for each node (including self-loops).
    #   - `xx` will contain the initial empty string followed by the `n` lines of input.
    #
    #Given the initial state and the processing, the output state can be described as follows:
    #
    #- `a` will have counts of 'F' relationships.
    #- `b` will have counts of 'S' relationships.
    #- `xx` will have the initial empty string plus the `n` lines of input.
    #
    #Output State:
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `a` will contain the count of 'F' relationships for each node (including self-loops); `b` will contain the count of 'S' relationships for each node (including self-loops); `xx` will contain the initial empty string followed by the `n` lines of input; `sa` will contain the indices of nodes that have 'F' relationships but no 'S' relationships; `sb` will contain the indices of nodes that have 'S' relationships but no 'F' relationships.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `a` will contain the count of 'F' relationships for each node (including self-loops); `b` will contain the count of 'S' relationships for each node (including self-loops); `xx` will contain the initial empty string followed by the `n` lines of input; `sa` will contain the indices of nodes that have 'F' relationships but no 'S' relationships, plus any additional indices where both `a[i]` and `b[i]` are zero; `sb` will contain the indices of nodes that have 'S' relationships but no 'F' relationships; the length of `sa` is greater than or equal to the length of `sb`; `t` is the length of `sa`.
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
            
        #State: `a` will contain the count of 'F' relationships for each node (including self-loops); `b` will contain the count of 'S' relationships for each node (including self-loops); `xx` will contain the initial empty string followed by `n` lines of input with '?' characters replaced by 'F' or 'S' based on the conditions involving `sa`; `sa` will contain the indices of nodes that have 'F' relationships but no 'S' relationships, plus any additional indices where both `a[i]` and `b[i]` are zero; `sb` will contain the indices of nodes that have 'S' relationships but no 'F' relationships; the length of `sa` is greater than or equal to the length of `sb`; `t` is the length of `sa`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `a` will contain the count of 'F' relationships for each node (including self-loops); `b` will contain the count of 'S' relationships for each node (including self-loops); `xx` will contain the initial empty string followed by the `n` lines of input; `sa` will contain the indices of nodes that have 'F' relationships but no 'S' relationships; `sb` will contain the indices of nodes that have 'S' relationships but no 'F' relationships, plus any indices of nodes that have neither 'F' nor 'S' relationships.
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
            
        #State: `xx` will be a matrix where each '?' character has been replaced by 'F' or 'S' based on the conditions specified in the loop. Variables `a`, `b`, `sa`, and `sb` remain unchanged.
    #State: `a` will contain the count of 'F' relationships for each node (including self-loops); `b` will contain the count of 'S' relationships for each node (including self-loops); `xx` will contain the initial empty string followed by `n` lines of input. If the length of `sa` is greater than or equal to the length of `sb`, `xx` will have '?' characters replaced by 'F' or 'S' based on the conditions involving `sa`, `sa` will include additional indices where both `a[i]` and `b[i]` are zero, and `t` will be the length of `sa`. Otherwise, `xx` will be a matrix where each '?' character has been replaced by 'F' or 'S' based on the conditions specified in the loop, while `a`, `b`, `sa`, and `sb` remain unchanged.
#Overall this is what the function does:The function processes an n x n grid of characters ('F', 'S', '?', '.'), where 'F' and 'S' represent specific attributes, '?' are undecided, and '.' indicates the same scenario as another cell. It counts the occurrences of 'F' and 'S' for each row/column, then replaces '?' with 'F' or 'S' based on the counts and specific conditions, ensuring that the number of 'F' and 'S' does not exceed certain limits. The function outputs the modified grid.

