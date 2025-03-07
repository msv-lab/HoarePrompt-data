#State of the program right berfore the function call: n is an integer where 2 ≤ n ≤ 24. The input consists of n lines, each containing n characters representing the partial transition video plan between scenarios. Characters can be F (funny), S (scary), ?, or . (no transition video specified). It is guaranteed that at most \lfloor \frac{n}{2} \rfloor transition videos are already decided (i.e., at most 2\lfloor \frac{n}{2} \rfloor characters are F or S).
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
        
    #State: Output State: After the loop executes all its iterations, the value of `i` will be `n + 1` because the loop runs from `1` to `n` inclusive. The list `xx` will contain `n` strings, each corresponding to the input provided during each iteration of the loop. The list `a` will have elements where `a[j]` is the total count of 'F' characters encountered in the `j-th` position across all input strings. Similarly, the list `b` will have elements where `b[j]` is the total count of 'S' characters encountered in the `j-th` position across all input strings. The initial values of `a` and `b` (all zeros) will be updated based on the input provided during each iteration of the loop.
    #
    #In summary, after the loop completes, `i` will be `n + 1`, `xx` will contain `n` input strings, `a[j]` will represent the total occurrences of 'F' at the `j-th` position across all inputs, and `b[j]` will represent the total occurrences of 'S' at the `j-th` position across all inputs.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: `i` is `n + 1`, `xx` contains `n` input strings, `a` and `b` are lists where `a[j]` represents the total occurrences of 'F' at the `j-th` position across all inputs and `b[j]` represents the total occurrences of 'S' at the `j-th` position across all inputs, `sa` is a list containing all integers from `1` to `i-1` (inclusive) that satisfy the condition `a[i] > 0 and b[i] == 0`, `sb` is a list containing all integers from `1` to `i-1` (inclusive) that satisfy the condition `b[i] > 0 and a[i] == 0`.
    #
    #In simpler terms, after the loop has executed all its iterations, `i` will be `n + 1` (since the loop runs from `1` to `n`), `xx` will still contain `n` input strings, and `a` and `b` will retain their original structure with counts of 'F' and 'S' respectively. The lists `sa` and `sb` will each contain a series of integers from `1` to `n` based on whether the corresponding conditions in the loop were met during each iteration. Specifically, `sa` will include indices where there are more 'F's than 'S's, and `sb` will include indices where there are more 'S's than 'F's.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: After the loop executes all iterations, `i` will be `n + 1`, and `sa` will contain all integers from `1` to `n` (inclusive) that satisfy the condition `a[i] == 0 and b[i] == 0`.
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
            
        #State: A string `nx` of length `n` consisting of characters 'F' and 'S', where for each `j` from 1 to `n`, if `xx[i][j-1]` is not '?', then `nx[j-1]` is equal to `xx[i][j-1]`. If `xx[i][j-1]` is '?', then `nx[j-1]` is 'F' if either `i` or `j` is in the first quarter of `sa` (i.e., `sa[:n//4]`), otherwise `nx[j-1]` is 'S'.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: `i` is `n + 1`, `n` remains the same, `xx` contains `n` input strings, `a` and `b` are lists where `a[j]` represents the total occurrences of 'F' at the `j-th` position across all inputs and `b[j]` represents the total occurrences of 'S' at the `j-th` position across all inputs, `sa` is a list containing all integers from `1` to `i-1` (inclusive) that satisfy the condition `a[i] > 0 and b[i] == 0`, `sb` is a list containing all integers from `1` to `i-1` (inclusive) that satisfy the condition `b[i] > 0 and a[i] == 0`, and the length of `sa` is less than the length of `sb`.
        #
        #Explanation: After the loop completes all its iterations, `i` will be incremented to `n + 1`. The loop iterates from `1` to `n`, and for each iteration, it checks if `a[i] == 0` and `b[i] == 0`. If both conditions are met, the integer `i` is appended to `sb`. Since the loop runs `n` times, `sb` will contain all integers from `1` to `n` that meet the specified condition, and `sa` will be empty because no element satisfies the condition `a[i] > 0 and b[i] == 0` within the given constraints. Therefore, `sa` will be an empty list, and the length of `sa` will always be less than the length of `sb`, which will be `n`.
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
            
        #State: nx is a string of length n-1 consisting of 'S' and 'F', `i` is n + 1, `j` is n + 1, and `n` is exactly the value it had after the last iteration of the loop.
    #State: `i` is `n + 1`, `xx` contains `n` input strings, `a` and `b` are lists where `a[j]` represents the total occurrences of 'F' at the `j-th` position across all inputs and `b[j]` represents the total occurrences of 'S' at the `j-th` position across all inputs, `sa` is a list containing all integers from `1` to `n-1` (inclusive) that satisfy the condition `a[i] > 0 and b[i] == 0`, `sb` is a list containing all integers from `1` to `n-1` (inclusive) that satisfy the condition `b[i] > 0 and a[i] == 0`, and `nx` is a string of length `n` (or `n-1` if the else part is executed) consisting of characters 'F' and 'S'. If `len(sa) >= len(sb)`, then for each `j` from 1 to `n`, if `xx[i][j-1]` is not '?', then `nx[j-1]` is equal to `xx[i][j-1]`. If `xx[i][j-1]` is '?', then `nx[j-1]` is 'F' if either `i` or `j` is in the first quarter of `sa` (i.e., `sa[:n//4]`), otherwise `nx[j-1]` is 'S'. If `len(sa) < len(sb)`, then `nx` is a string of length `n-1` consisting of 'S' and 'F', `i` is `n + 1`, `j` is `n + 1`, and `n` is the same as after the last iteration of the loop.
#Overall this is what the function does:The function processes a square grid of size \( n \times n \) where \( n \) is an integer between 2 and 24. Each cell in the grid can contain 'F' (funny), 'S' (scary), '?' (unknown), or '.' (no transition video specified). The function calculates the total number of 'F' and 'S' characters in each column. Based on these counts, it generates two lists: one for columns with more 'F' than 'S', and another for columns with more 'S' than 'F'. Depending on the comparison of these lists' lengths, it fills in the unknown cells ('?') with either 'F' or 'S' and prints the resulting grid.

