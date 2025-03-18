#State of the program right berfore the function call: n is an integer where 2 ≤ n ≤ 24, and the input consists of n lines, each containing n characters representing the partial transition video plan. The characters can be F (funny), S (scary), ?, or . (no transition video). At most \lfloor \frac{n}{2} \rfloor transition videos are already decided (i.e., at most 2\lfloor \frac{n}{2} \rfloor characters are F or S).
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
        
    #State: Output State: `xx` is a list containing `n+1` strings, each being the input received at each iteration of the loop. The lists `a` and `b` are updated such that for each index `i` from `1` to `n+1`, `a[i]` represents the total number of times the character `'F'` appeared at position `i-1` across all inputs, and `b[i]` represents the total number of times the character `'S'` appeared at position `i-1` across all inputs.
    #
    #This means that after all iterations of the loop, `xx` will contain a list of all the inputs provided during the loop's execution, and the lists `a` and `b` will reflect the cumulative counts of `'F'` and `'S'` characters at each position across all inputs.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: After the loop executes all iterations, `i` will be `n+1`, `n` is a positive integer, `a` is a list of integers where each `a[i]` (for `1 ≤ i ≤ n+1`) represents the total number of times the character `'F'` appeared at position `i-1` across all inputs, and `b` is a list of integers where each `b[i]` (for `1 ≤ i ≤ n+1`) represents the total number of times the character `'S'` appeared at position `i-1` across all inputs. `sa` is a list containing all indices `i` (from `1` to `n+1`) for which `a[i] > 0` and `b[i] == 0`. The list `sb` is a list containing the single integer `1`.
    #
    #In simpler terms, after the loop completes all its iterations, `sa` will include all positions where `'F'` appeared without any preceding `'S'`, and `sb` will still just contain the number `1`.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Postcondition: `i` is `n+1`, `n` is a positive integer, `a` is a list of integers with length `n+1` where each `a[i]` (for `1 ≤ i ≤ n+1`) represents the total number of times the character `'F'` appeared at position `i-1` across all inputs, `b` is a list of integers with length `n+1` where each `b[i]` (for `1 ≤ i ≤ n+1`) represents the total number of times the character `'S'` appeared at position `i-1` across all inputs, `sa` is a list containing all indices `i` (from `1` to `n+1`) for which `a[i] > 0` and `b[i] == 0`, and `sb` is a list containing the single integer `1`. The length of `sa` is greater than or equal to the length of `sb`.
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
            
        #State: The final value of `nx` will be a string constructed based on the conditions within the loop for all iterations from 1 to `n`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: `i` is `n+1`, `n` is a positive integer, `a` is a list of integers where each `a[i]` (for `1 ≤ i ≤ n+1`) represents the total number of times the character `'F'` appeared at position `i-1` across all inputs, and `b` is a list of integers where each `b[i]` (for `1 ≤ i ≤ n+1`) represents the total number of times the character `'S'` appeared at position `i-1` across all inputs, `sa` will include all positions where `'F'` appeared without any preceding `'S'`, and `sb` contains the number `1` appended with the value of `i` if `a[i] == 0` and `b[i] == 0`. After all iterations of the loop, `sb` will contain the numbers `1` through `n+1` because the condition `a[i] == 0 and b[i] == 0` was met for each `i` from `1` to `n+1`.
        #
        #This means that for every `i` from `1` to `n+1`, the loop added `i` to `sb` when both `a[i]` and `b[i]` were `0`. Therefore, `sb` will be `[1, 2, 3, ..., n+1]`.
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
            
        #State: sb is [1, 2, 3, ..., n+1].
    #State: `sa` includes all positions where the character 'F' appeared without any preceding 'S', and `sb` contains the integers from 1 to `n+1`. If the length of `sa` is greater than or equal to the length of `sb`, then `nx` will be a string constructed based on the conditions within the loop for all iterations from 1 to `n`. Otherwise, `sb` will contain the integers from 1 to `n+1`.
#Overall this is what the function does:The function processes an input consisting of n lines, each containing n characters representing a partial transition video plan. These characters can be 'F' (funny), 'S' (scary), '?', or '.' (no transition video). The function updates two lists, `a` and `b`, to count the occurrences of 'F' and 'S' at each position across all inputs. It then determines two lists, `sa` and `sb`, based on these counts. Depending on the lengths of `sa` and `sb`, the function constructs and prints a new string for each line, replacing '?' with either 'F' or 'S' based on specific conditions. If `sa` is longer than or equal to `sb`, it prioritizes 'F'; otherwise, it prioritizes 'S'. Finally, the function outputs these constructed strings.

