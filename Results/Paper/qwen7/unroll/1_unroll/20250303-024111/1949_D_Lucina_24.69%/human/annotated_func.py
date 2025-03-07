#State of the program right berfore the function call: n is an integer where 2 ≤ n ≤ 24. The input consists of n lines, each containing n characters representing the partial transition video plan between scenarios. Characters can be F (funny), S (scary), ?, or . (no transition video needed). It is guaranteed that at most \lfloor \frac{n}{2} \rfloor transition videos are already decided, and all other characters are undecided (?).
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
        
    #State: Output State: `n` is an input integer where 2 ≤ n ≤ 24; `a` is a list of length n+1 where each element is the count of 'F' received from the corresponding input strings; `b` is a list of length n+1 where each element is the count of 'S' received from the corresponding input strings; `xx` is a list containing n+1 elements, each being a string input from the user.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: `n` is an input integer where 2 ≤ n ≤ 24; `a` is a list of length n+1 where each element is the count of 'F' received from the corresponding input strings; `b` is a list of length n+1 where each element is the count of 'S' received from the corresponding input strings; `xx` is a list containing n+1 elements, each being a string input from the user; `sa` is a list containing indices `i` where `a[i] > 0` and `b[i] == 0`; `sb` is a list containing indices `i` where `b[i] > 0` and `a[i] == 0`.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Output State: `n` is an input integer where 2 ≤ n ≤ 24; `a` is a list of length n+1 where each element is the count of 'F' received from the corresponding input strings; `b` is a list of length n+1 where each element is the count of 'S' received from the corresponding input strings; `xx` is a list containing n+1 elements, each being a string input from the user; `sa` is a list containing indices `i` where `a[i] == 0` and `b[i] == 0`; `sb` is a list of length n+1 where each element is a string input from the user. The length of `sa` is greater than or equal to the length of `sb`.
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
            
        #State: Output State: `n` is an input integer where 2 ≤ n ≤ 24; `a` is a list of length n+1 where each element is the count of 'F' received from the corresponding input strings; `b` is a list of length n+1 where each element is the count of 'S' received from the corresponding input strings; `xx` is a list containing n+1 elements, each being a string input from the user with each character either 'F', 'S', or '?'; `sa` is a list containing indices `i` where `a[i] == 0` and `b[i] == 0`; `sb` is a list of length n+1 where each element is a string input from the user. After the loop executes, each element in `xx` has been modified such that any '?' character has been replaced with either 'F' or 'S' based on specific conditions: if the current index `i` (or `j`) is within the first quarter of `sa`, then '?' is replaced with 'F', otherwise it is replaced with 'S'.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: `n` is an input integer where 2 ≤ n ≤ 24; `a` is a list of length n+1 where each element is the count of 'F' received from the corresponding input strings; `b` is a list of length n+1 where each element is the count of 'S' received from the corresponding input strings; `xx` is a list containing n+1 elements, each being a string input from the user; `sa` is a list containing indices `i` where `a[i] > 0` and `b[i] == 0`; `sb` is a list containing indices `i` where `b[i] > 0` and `a[i] == 0`; After the loop executes, `sb` contains indices `i` where `b[i] > 0` and `a[i] == 0`. The length of `sb` is greater than or equal to the length of `sa`.
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
            
        #State: Output State: `n` is an input integer where 2 ≤ n ≤ 24; `a` is a list of length n+1 where each element is the count of 'F' received from the corresponding input strings; `b` is a list of length n+1 where each element is the count of 'S' received from the corresponding input strings; `xx` is a list containing n+1 elements, each being a string input from the user; `sa` is a list containing indices `i` where `a[i] > 0` and `b[i] == 0`; `sb` is a list containing indices `i` where `b[i] > 0` and `a[i] == 0`, and after the loop executes, `sb` contains indices `i` where `b[i] > 0` and `a[i] == 0`. The length of `sb` is greater than or equal to the length of `sa`; Each element `nx` in the output is a string generated by replacing '?' in the corresponding `xx[i]` with either 'S' or 'F' based on the conditions in the loop, and printed during each iteration.
    #State: `n` is an input integer where 2 ≤ n ≤ 24; `a` is a list of length n+1 where each element is the count of 'F' received from the corresponding input strings; `b` is a list of length n+1 where each element is the count of 'S' received from the corresponding input strings; `xx` is a list containing n+1 elements, each being a string input from the user with each character either 'F', 'S', or '?'; `sa` is a list containing indices `i` where `a[i] == 0` and `b[i] == 0`; `sb` is a list of length n+1 where each element is a string input from the user. After the loop executes, each element in `xx` has been modified such that any '?' character has been replaced with either 'F' or 'S' based on specific conditions: if the current index `i` (or `j`) is within the first quarter of `sa`, then '?' is replaced with 'F', otherwise it is replaced with 'S'. If `len(sa) >= len(sb)`, the replacement follows the above conditions. Otherwise, `sb` contains indices `i` where `b[i] > 0` and `a[i] == 0`, and each element `nx` in the output is a string generated by replacing '?' in the corresponding `xx[i]` with either 'S' or 'F' based on the conditions in the loop, and printed during each iteration.
#Overall this is what the function does:The function processes an input consisting of n lines, each containing n characters representing the partial transition video plan between scenarios. It counts the occurrences of 'F' (funny) and 'S' (scary) in each line and stores these counts in lists `a` and `b`. Based on the counts, it identifies undecided characters ('?') and replaces them with either 'F' or 'S' according to specific rules. The function ensures that at most \(\lfloor \frac{n}{2} \rfloor\) transition videos are decided. Finally, it prints the modified lines.

