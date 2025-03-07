#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input consists of n lines, each containing n characters. The j-th character of the i-th line is either 'F', 'S', '?', or '.', where 'F' denotes a funny transition video, 'S' denotes a scary transition video, '?' denotes an undecided transition video, and '.' denotes the same scenario (i.e., i=j). The input is symmetric, meaning the j-th character of the i-th line is the same as the i-th character of the j-th line. There are at most floor(n/2) characters in the input that are either 'F' or 'S'.
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
        
    #State: - The list `a` will have counts of 'F' characters for each node (1 to n) and an extra element (0) at index 0.
    #   - The list `b` will have counts of 'S' characters for each node (1 to n) and an extra element (0) at index 0.
    #   - The list `xx` will contain an initial empty string and then all the lines of input.
    #
    #Given these rules, the output state can be described as follows:
    #
    #Output State:
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: `sa` is a list of nodes that have 'F' characters but no 'S' characters; `sb` is a list of nodes that have 'S' characters but no 'F' characters; `a` and `b` lists remain as they were initially with counts of 'F' and 'S' respectively; `xx` remains unchanged.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `sa` is a list of nodes that have 'F' characters but no 'S' characters, plus any indices `i` from `1` to `n` where both `a[i]` and `b[i]` are `0`; `sb` is a list of nodes that have 'S' characters but no 'F' characters; `a` and `b` lists remain unchanged; `xx` remains unchanged.
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
            
        #State: The output state will consist of the printed strings `nx` for each `i` from `1` to `n`. The exact content of these strings depends on the initial values of `xx`, `sa`, and `sb`. However, the structure of the output will be a series of strings, each corresponding to an `i` from `1` to `n`, where '?' characters in `xx` are replaced according to the rules involving `sa`.
        #
        #Since the exact values of `xx`, `sa`, and `sb` are not provided, we can't specify the exact printed strings. However, we can describe the output state in a general manner.
        #
        #Output State:
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `sa` is a list of nodes that have 'F' characters but no 'S' characters; `sb` is a list of nodes that have 'S' characters but no 'F' characters, and additionally includes nodes `i` from 1 to `n` where both `a[i]` and `b[i]` are 0; `a` and `b` lists remain as they were initially with counts of 'F' and 'S' respectively; `xx` remains unchanged; the length of `sa` is less than or equal to the length of `sb`.
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
            
        #State: The variable `xx` remains unchanged. The lists `sa`, `sb`, `a`, and `b` remain unchanged. The loop prints a new string `nx` for each `i` from 1 to `n`, where each character in `nx` is determined by the conditions specified in the loop.
    #State: `sa` is a list of nodes that have 'F' characters but no 'S' characters; `sb` is a list of nodes that have 'S' characters but no 'F' characters; `a` and `b` lists remain as they were initially with counts of 'F' and 'S' respectively; `xx` remains unchanged. If the length of `sa` is greater than or equal to the length of `sb`, the loop prints a new string `nx` for each `i` from 1 to `n`, where '?' characters in `xx` are replaced according to the rules involving `sa`. Otherwise, the variable `xx` remains unchanged, and the lists `sa`, `sb`, `a`, and `b` remain unchanged, and the loop prints a new string `nx` for each `i` from 1 to `n`, where each character in `nx` is determined by the conditions specified in the loop.
#Overall this is what the function does:The function reads a symmetric matrix of size n x n, where each element is 'F', 'S', '?', or '.', and replaces '?' with 'F' or 'S' based on the counts of 'F' and 'S' in each row. It prints the modified matrix, ensuring that '?' characters are replaced according to specific rules involving nodes with only 'F' or only 'S'.

