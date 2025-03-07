#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 24. The input consists of n lines, where the j-th character of the i-th line corresponds to the transition video between the i-th and the j-th scenarios. Each line contains n characters, which can be F (funny), S (scary), ?, or . (no transition video yet). At most \lfloor \frac{n}{2} \rfloor transition videos are already decided, represented by F or S, and the rest are undecided, represented by ?. The input guarantees that the i-th character of the j-th line and the j-th character of the i-th line are the same for all i and j.
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
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `2 * n + 1`, `j` will be `n + 1`, `n` will still be an integer such that \(2 \leq n \leq 24\), `xx` will be a list containing `n` strings, each being the input string `x`, `a` will be a list with counts of 'F' characters starting from index 1 up to `n`, and `b` will be a list with counts of 'S' characters starting from index 1 up to `n`.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: The final state of the loop will be as follows: `i` will be equal to `n + 1`, `sa` will contain all indices `i` (from 2 to `n`) where `a[i] > 0` and `b[i] == 0`, and `sb` will contain all indices `i` (from 2 to `n`) where `b[i] > 0` and `a[i] == 0`. The variable `n` remains unchanged and must be between 2 and 24.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Output State: `i` is `n + 1`, `n` must be between 2 and 24, `sa` contains all indices `i` (from 1 to `n`) where `a[i] == 0` and `b[i] == 0`, and `sb` will contain all indices `i` (from 2 to `n`) where `b[i] > 0` and `a[i] == 0`.
        #
        #This means that after the loop has executed all its iterations, the variable `i` will be set to `n + 1`, as the loop increments `i` from 1 to `n + 1`. During each iteration, if `a[i]` is 0 and `b[i]` is 0, the index `i` is appended to the list `sa`. The list `sb` remains unchanged, containing all indices `i` (from 2 to `n`) where `b[i] > 0` and `a[i] == 0`.
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
            
        #State: After the loop executes all iterations, `i` will be set to `n + 1`, `j` will also be `n + 1`, and `nx` will be a string constructed based on the values in `xx` and the conditions specified in the loop.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: `i` is `n + 1`, `n` is between 2 and 24, `sa` will contain all indices \( i \) (from 2 to \( n \)) where \( a[i] > 0 \) and \( b[i] == 0 \), and `sb` will contain all indices \( i \) (from 2 to \( n \)) where \( b[i] > 0 \) and \( a[i] == 0 \). If \( a[i] == 0 \) and \( b[i] == 0 \), then `sb` now includes index \( i \).
        #
        #Explanation: After the loop has executed all its iterations, the value of `i` will be `n + 1` because the loop increments `i` from 1 to `n + 1`. During each iteration, the loop checks if `a[i] == 0` and `b[i] == 0`. If both conditions are met, the index `i` is appended to `sb`. Since the loop runs from `i = 1` to `i = n + 1`, it will check all indices from 1 to `n + 1`. However, the loop only appends indices from 2 to `n` to `sb` based on the given conditions. Therefore, after the loop completes, `sb` will contain all indices \( i \) (from 2 to \( n \)) where \( b[i] > 0 \) and \( a[i] == 0 \), provided these conditions were met during the loop's execution. The value of `n` remains unchanged as per the problem statement.
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
            
        #State: i is n + 1, n is between 2 and 24, nx is a string of length n-1 consisting of 'S', 'F', or '?', and sb contains all indices i (from 2 to n) where b[i] > 0 and a[i] == 0.
    #State: `i` is set to `n + 1`, `n` is between 2 and 24, `nx` is a string of length `n-1` consisting of 'S', 'F', or '?', `sa` contains all indices `i` (from 2 to `n`) where `a[i] > 0` and `b[i] == 0`, and `sb` contains all indices `i` (from 2 to `n`) where `b[i] > 0` and `a[i] == 0`.
#Overall this is what the function does:The function processes a 2D list representing transition videos between scenarios. It counts the number of 'F' (funny) and 'S' (scary) videos for each scenario. Based on these counts and certain conditions, it constructs and prints a new list of transition videos. If the count of 'F' videos is greater than or equal to the count of 'S' videos, it prioritizes 'F' videos; otherwise, it prioritizes 'S' videos. The function ensures that the final output respects the initial constraints and prints the new list of transition videos.

