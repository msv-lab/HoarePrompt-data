#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 24. The input consists of n lines, where the j-th character of the i-th line corresponds to the transition video between the i-th and the j-th scenarios. Each line contains n characters, and the characters can be F (funny), S (scary), ?, or . (no transition video). It is guaranteed that the i-th character of the j-th line and the j-th character of the i-th line are the same for all i and j. At most \lfloor \frac{n}{2} \rfloor transition videos are already decided, meaning at most 2 \lfloor \frac{n}{2} \rfloor characters in the input are F or S.
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
        
    #State: Output State: `n` is an integer such that 2 ≤ n ≤ 24; `a` is a list of length n+1 where each element represents the total count of 'F' characters in the strings `x` from each iteration of the loop; `b` is a list of length n+1 where each element represents the total count of 'S' characters in the strings `x` from each iteration of the loop; `xx` is a list containing all the strings `x` entered during the iterations of the loop; `i` is set to `n+1`; `j` is equal to `n`.
    #
    #In this final state, after all iterations of the loop have completed, the variable `n` remains within its initial bounds (2 to 24). The lists `a` and `b` contain the cumulative counts of 'F' and 'S' characters respectively from all the input strings `x` provided during the loop's iterations. The list `xx` contains all the strings `x` that were input into the loop. The variable `i` is set to `n+1`, indicating that no further iterations are needed. The variable `j` is equal to `n`, which is the last index considered in the inner loop, ensuring that all possible 'F' and 'S' counts have been updated.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: After the loop executes all the iterations, `i` will be `n+1`, `n` will be an integer such that 2 ≤ n ≤ 24, `a` and `b` will be lists of length `n+1`, `xx` will be a list containing all the strings `x` entered during the iterations of the loop, `j` will be equal to `n`, `sa` will be a list containing all integers from 1 to the highest index where `a[i] > 0` and `b[i] == 0`, and `sb` will be a list containing all integers from 1 to the highest index where `b[i] > 0` and `a[i] == 0`.
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: The final state of `sa` will contain all indices `i` from 1 to `n` where `a[i] == 0` and `b[i] == 0`.
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
            
        #State: The final value of `nx` is a string of length `n` constructed by iterating through each index `i` from 1 to `n`. For each index `i`, `nx` concatenates characters from `xx[i][j-1]` for all `j` from 1 to `n`. If `xx[i][j-1]` is '?', `nx` appends 'F' if either `i` or `j` is in the first quarter of the list `sa`, otherwise it appends 'S'. If `xx[i][j-1]` is not '?', `nx` simply appends the character from `xx[i][j-1]`.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: `i` is `n+1`, `sb` is a list containing all integers from 1 to `n` (inclusive), `a` is a list of integers where `a[i]` is 0 for all `i` from 1 to `n+1`, `b` is a list of integers where `b[i]` is 0 for all `i` from 1 to `n+1`, `n` is the original value it started with (greater than or equal to 3), `xx` is an empty list, `j` is `n`, `sa` is an empty list, and `sb` contains all integers from 1 to `n`.
        #
        #In simpler terms, after the loop has executed all its iterations, `i` will be `n+1`, meaning the loop has completed its full cycle. The list `sb` will contain every integer from 1 to `n`, indicating that all indices where `a[i]` and `b[i]` were both zero have been appended to `sb`. Both `a` and `b` will be lists of zeros from index 1 to `n+1`. The other variables `n`, `xx`, `j`, `sa`, and their conditions remain as described in the initial state.
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
            
        #State: After the loop has executed all its iterations, `i` is `n+1`, `sb` contains all integers from 1 to `n`, `a` and `b` are lists of zeros from index 1 to `n+1`, `n` is the original value it started with (greater than or equal to 3), `xx` is an empty list, `j` is `n`, and `sa` is an empty list.
    #State: After the if-else block executes, `nx` is a string of length `n` constructed as follows: for each index `i` from 1 to `n`, `nx` concatenates characters from `xx[i][j-1]` for all `j` from 1 to `n`. If `xx[i][j-1]` is '?', `nx` appends 'F' if either `i` or `j` is in the first quarter of the list `sa`, otherwise it appends 'S'. If `xx[i][j-1]` is not '?', `nx` simply appends the character from `xx[i][j-1]`. Additionally, `i` is `n+1`, `sb` contains all integers from 1 to `n`, `a` and `b` are lists of zeros from index 1 to `n+1`, `n` is the original value it started with (greater than or equal to 3), `xx` is an empty list, `j` is `n`, and `sa` is an empty list.
#Overall this is what the function does:The function processes a 2D grid of size n x n, where each cell contains either 'F' (funny), 'S' (scary), '?', or '.'. It counts the number of 'F' and 'S' characters in each row and stores these counts in lists `a` and `b`. Based on these counts, it decides the type of transition video ('F' or 'S') for the undecided cells ('?'). If more rows have 'F' counts greater than zero compared to 'S' counts, it sets all undecided cells to 'F'; otherwise, it sets them to 'S'. Finally, it prints the completed grid.

