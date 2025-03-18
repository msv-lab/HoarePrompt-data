#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 24. The input consists of n lines, each containing n characters. The j-th character of the i-th line represents the transition video between the i-th and j-th scenarios, and can be 'F' (funny), 'S' (scary), '?' (undecided), or '.' (same scenario, no transition). At most 2 * floor(n / 2) characters in the input will be 'F' or 'S'.
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
        
    #State: After all iterations of the loop, `n` remains an integer such that 2 ≤ n ≤ 24, `i` is `n + 1`, `xx` is a list containing an empty string followed by `n` input strings. The lists `a` and `b` are updated based on the characters in each input string `x` as follows: for each character 'F' at position `j-1` in the string `x`, both `a[i]` and `a[j]` are incremented by 1; for each character 'S' at position `j-1` in the string `x`, both `b[i]` and `b[j]` are incremented by 1.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: After all iterations of the loop, `n` remains an integer such that 2 ≤ n ≤ 24, `i` is `n + 1`, `xx` is a list containing an empty string followed by `n` input strings. The lists `a` and `b` are updated based on the characters in each input string `x` as follows: for each character 'F' at position `j-1` in the string `x`, both `a[i]` and `a[j]` are incremented by 1; for each character 'S' at position `j-1` in the string `x`, both `b[i]` and `b[j]` are incremented by 1. `sa` contains all indices `i` (from 1 to `n`) where `a[i] > 0` and `b[i] == 0`. `sb` contains all indices `i` (from 1 to `n`) where `b[i] > 0` and `a[i] == 0`.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: After the loop executes all iterations, `n` remains an integer such that 2 ≤ n ≤ 24, `i` is `n + 1`, `xx` is a list containing an empty string followed by `n` input strings. The lists `a` and `b` are updated based on the characters in each input string `x`. `sa` now contains all indices `i` (from 1 to `n`) where `a[i] > 0` and `b[i] == 0`, and `sb` contains all indices `i` (from 1 to `n`) where `b[i] > 0` and `a[i] == 0`. For any index `i` from 1 to `n`, if `a[i] == 0` and `b[i] == 0`, then `i` is appended to `sa`. The length of `sa` is still greater than or equal to the length of `sb`.
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
            
        #State: After the loop executes all iterations, `i` is `n + 1`, `n` is an integer such that 2 ≤ n ≤ 24, and `nx` is a string of length `n` for each iteration of the loop. Each `nx` string is constructed by iterating through the characters of `xx[i]` from index 0 to `n-1`. For each character at index `k` (where `0 ≤ k < n`), if the character is not `'?'`, it is appended to `nx`. If the character is `'?'`, and if `i` or `k + 1` is in the first `n // 4` elements of `sa`, then `'F'` is appended to `nx`. Otherwise, `'S'` is appended to `nx`. The final state of `xx` remains unchanged, and the lists `a` and `b` are not modified by the loop.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: After all iterations of the loop, `n` remains an integer such that 2 ≤ n ≤ 24, `i` is `n + 1`, `xx` is a list containing an empty string followed by `n` input strings, `a` and `b` are updated based on the characters in each input string `x`, `sa` contains all indices `i` (from 1 to `n`) where `a[i] > 0` and `b[i] == 0`, `sb` contains all indices `i` (from 1 to `n`) where `b[i] > 0` and `a[i] == 0`, the length of `sa` is less than the length of `sb`. For each index `i` from 1 to `n`, if `a[i]` and `b[i]` are both 0, then `sb` includes the index `i`.
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
            
        #State: After the loop executes all iterations, `i` will be `n + 1`, `j` will be `n + 1`, `nx` will contain the final concatenated string for each `i` from 1 to `n` based on the rules specified in the loop, and the other variables (`n`, `xx`, `a`, `b`, `sa`, `sb`) will remain unchanged.
    #State: *After all iterations of the loop, `n` remains an integer such that 2 ≤ n ≤ 24, `i` is `n + 1`, and `xx` is a list containing an empty string followed by `n` input strings. The lists `a` and `b` are updated based on the characters in each input string `x` as follows: for each character 'F' at position `j-1` in the string `x`, both `a[i]` and `a[j]` are incremented by 1; for each character 'S' at position `j-1` in the string `x`, both `b[i]` and `b[j]` are incremented by 1. `sa` contains all indices `i` (from 1 to `n`) where `a[i] > 0` and `b[i] == 0`. `sb` contains all indices `i` (from 1 to `n`) where `b[i] > 0` and `a[i] == 0`. If `len(sa) >= len(sb)`, for each `i` from 1 to `n`, `nx` is a string of length `n` constructed by iterating through the characters of `xx[i]` from index 0 to `n-1`. For each character at index `k` (where `0 ≤ k < n`), if the character is not `'?'`, it is appended to `nx`. If the character is `'?'`, and if `i` or `k + 1` is in the first `n // 4` elements of `sa`, then `'F'` is appended to `nx`. Otherwise, `'S'` is appended to `nx`. The final state of `xx` remains unchanged, and the lists `a` and `b` are not modified by the loop. If `len(sa) < len(sb)`, for each `i` from 1 to `n`, `nx` will contain the final concatenated string for each `i` from 1 to `n` based on the rules specified in the loop, and the other variables (`n`, `xx`, `a`, `b`, `sa`, `sb`) will remain unchanged.
#Overall this is what the function does:The function reads an integer `n` (2 ≤ n ≤ 24) and `n` lines of input, each containing `n` characters representing transitions between scenarios. These characters can be 'F' (funny), 'S' (scary), '?' (undecided), or '.' (no transition). The function processes these inputs to categorize scenarios into those that are only funny (`sa`) and those that are only scary (`sb`). It then modifies the undecided transitions ('?') based on the following rules: If the number of funny scenarios is greater than or equal to the number of scary scenarios, it replaces the first `n // 4` undecided transitions with 'F' and the rest with 'S'. If the number of scary scenarios is greater, it replaces the first `n // 4` undecided transitions with 'S' and the rest with 'F'. The function prints the modified transition matrix, one line at a time. The original input and internal state of the function remain unchanged.

