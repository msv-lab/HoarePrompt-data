#State of the program right berfore the function call: n is an integer where 2 ≤ n ≤ 24. The input consists of n lines, each containing n characters representing the partial transition video plan. The characters can be F (funny), S (scary), ?, or . (no transition video specified). It is guaranteed that at most \lfloor \frac{n}{2} \rfloor transition videos are already decided, and all other characters are undecided (?).
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
        
    #State: Output State: After the loop executes all iterations, `i` will be `n + 1`, `n` remains an integer between 2 and 24, `j` will be `n + 1`, `xx` is a list containing `n` arrays (each representing an input string `x`), and for every index `k` from 1 to `n`, `a[k]` is incremented by the total number of 'F's across all input strings `x` up to index `k-1`. Similarly, `b[k]` is incremented by the total number of 'S's across all input strings `x` up to index `k-1`.
    #
    #In simpler terms, after the loop completes, `a[k]` will hold the cumulative count of 'F's from all inputs up to the k-th position, and `b[k]` will hold the cumulative count of 'S's from all inputs up to the k-th position. The variable `xx` will contain a list of all the input strings `x` provided during the loop iterations.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: After the loop executes all the iterations, `i` is `n + 1`, `n` is an integer between 2 and 24, `j` is not equal to `n + 1`, `sa` is a list containing all integers from 6 to `n`, and `sb` is a list containing all integers from 6 to `n`.
    #
    #In this final state, `i` has reached `n + 1` as the loop increments `i` from 1 to `n`. The value of `n` remains within its specified range of 2 to 24. The variable `j` is not equal to `n + 1`, indicating it has been modified during the loop's execution. The lists `sa` and `sb` both contain all integers starting from 6 up to `n`, reflecting the conditions under which elements were appended to these lists throughout the loop's iterations.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Postcondition: `i` is `n + 1`, `n` is an integer between 2 and 24, `j` is not equal to `n + 1`, `sa` is a list containing all integers from 6 to `n` with 1 appended and all integers from 2 to `n` (excluding those for which `a[i] == 0` and `b[i] == 0`), `sb` is a list containing all integers from 6 to `n`, and the length of `sa` is greater than or equal to the length of `sb`.
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
            
        #State: nx is a string of length n, composed entirely of 'F' characters.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `i` is `n + 1`, `n` is an integer between 2 and 24, `j` is not equal to `n + 1`, `sa` is a list containing all integers from 6 to `n`, and `sb` is a list containing all integers from 6 to `n` with all integers from 1 to `n` appended.
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
            
        #State: The final value of `nx` will be a string of length `n`, consisting entirely of 'S' characters.
    #State: `i` is `n + 1`, `n` is an integer between 2 and 24, `j` is not equal to `n + 1`, `sa` and `sb` are both lists containing all integers from 6 to `n`. If the length of `sa` is greater than or equal to the length of `sb`, `nx` is a string of length `n` composed entirely of 'F' characters. Otherwise, `nx` is a string of length `n` consisting entirely of 'S' characters.
#Overall this is what the function does:The function processes an input consisting of \( n \) lines, each containing \( n \) characters representing a partial transition video plan. Each character can be 'F' (funny), 'S' (scary), '?', or '.' (no transition video specified). The function counts the cumulative occurrences of 'F' and 'S' for each position and categorizes positions into two lists: `sa` for positions with more 'F's than 'S's, and `sb` for positions with more 'S's than 'F's. If the length of `sa` is greater than or equal to the length of `sb`, the function generates a string of 'F's; otherwise, it generates a string of 'S's. The function then prints the generated string.

