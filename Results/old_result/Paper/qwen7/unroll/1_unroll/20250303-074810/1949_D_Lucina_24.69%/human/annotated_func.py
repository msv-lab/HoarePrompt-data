#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 24. The input consists of n lines, where the j-th character of the i-th line corresponds to the transition video between the i-th and the j-th scenarios. Each line contains n characters, which can be F (funny), S (scary), ?, or . (no transition video specified). It is guaranteed that the i-th character of the j-th line and the j-th character of the i-th line are the same for all i and j. At most \lfloor \frac{n}{2} \rfloor transition videos are already decided, meaning at most 2\lfloor \frac{n}{2} \rfloor characters in the input are F or S.
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
        
    #State: Output State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length n+1 where each element is the count of 'F' received from the input for each index, `b` is a list of length n+1 where each element is the count of 'S' received from the input for each index, `xx` is a list containing n elements, each being the input string received during each iteration of the loop.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: Output State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length n+1 where each element is the count of 'F' received from the input for each index, `b` is a list of length n+1 where each element is the count of 'S' received from the input for each index, `xx` is a list containing n elements, each being the input string received during each iteration of the loop, `sa` is a list containing indices `i` where `a[i] > 0` and `b[i] == 0`, `sb` is a list containing indices `i` where `b[i] > 0` and `a[i] == 0`.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: Output State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length n+1 where each element is the count of 'F' received from the input for each index, `b` is a list of length n+1 where each element is the count of 'S' received from the input for each index, `xx` is a list containing n elements, each being the input string received during each iteration of the loop, `sa` is a list containing indices i where a[i] > 0 and b[i] == 0, `sb` is a list containing indices i where b[i] > 0 and a[i] == 0, and `sa` is updated to include all indices i where a[i] == 0 and b[i] == 0.
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
            
        #State: Output State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length n+1 where each element is the count of 'F' received from the input for each index, `b` is a list of length n+1 where each element is the count of 'S' received from the input for each index, `xx` is a list containing n elements, each being the input string received during each iteration of the loop, `sa` is a list containing indices i where a[i] > 0 and b[i] == 0, `sb` is a list containing indices i where b[i] > 0 and a[i] == 0, and `sa` is updated to include all indices i where a[i] == 0 and b[i] == 0, `nx` is a string generated during each iteration of the inner loop based on the conditions provided.
        #
        #In simpler terms, after the loop executes all its iterations, the `nx` variable will contain a string generated for each `i` from 1 to `n`. This string is constructed by checking the corresponding character in `xx[i]`, and if it's not '?', it uses that character. If it is '?', it checks additional conditions involving `sa` and `sb` lists to decide whether to append 'F' or 'S'. The `sa`, `sb`, `a`, and `b` lists remain unchanged as they are not modified within the loop.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: Output State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length n+1 where each element is the count of 'F' received from the input for each index, `b` is a list of length n+1 where each element is the count of 'S' received from the input for each index, `xx` is a list containing n elements, each being the input string received during each iteration of the loop, `sa` is a list containing indices `i` where `a[i] > 0` and `b[i] == 0`, `sb` is a list containing indices `i` where `b[i] > 0` and `a[i] == 0`, and after executing the loop, `sb` contains indices `i` where `b[i] > 0` and `a[i] == 0` with the additional condition that `a[i] == 0` and `b[i] == 0` for those indices added in the loop.
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
            
        #State: Output State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length n+1 where each element is the count of 'F' received from the input for each index, `b` is a list of length n+1 where each element is the count of 'S' received from the input for each index, `xx` is a list containing n elements, each being the input string received during each iteration of the loop, `sa` is a list containing indices `i` where `a[i] > 0` and `b[i] == 0`, `sb` is a list containing indices `i` where `b[i] > 0` and `a[i] == 0` with the additional condition that `a[i] == 0` and `b[i] == 0` for those indices added in the loop, and after executing the loop, `sb` contains indices `i` where `b[i] > 0` and `a[i] == 0` with the additional condition that `a[i] == 0` and `b[i] == 0` for those indices added in the loop.
    #State: `n` is an integer such that 2 ≤ n ≤ 24, `a` is a list of length n+1 where each element is the count of 'F' received from the input for each index, `b` is a list of length n+1 where each element is the count of 'S' received from the input for each index, `xx` is a list containing n elements, each being the input string received during each iteration of the loop, `sa` is a list containing indices `i` where `a[i] > 0` and `b[i] == 0`, `sb` is a list containing indices `i` where `b[i] > 0` and `a[i] == 0`. After the loop executes, if `len(sa) >= len(sb)`, `sa` is updated to include all indices `i` where `a[i] == 0` and `b[i] == 0`, and `nx` is a string generated based on the conditions provided. Otherwise, `sb` is updated to include additional indices `i` where `a[i] == 0` and `b[i] == 0`, and `nx` is a string generated based on the conditions provided.
#Overall this is what the function does:The function processes a symmetric 2D grid of size n x n, where each cell contains a character indicating the type of transition video between scenarios (F for funny, S for scary, ? for undecided, or . for no video). It counts the occurrences of 'F' and 'S' for each row and stores these counts in lists `a` and `b`. Based on the counts, it categorizes rows into two groups: `sa` for rows with more 'F' than 'S', and `sb` for rows with more 'S' than 'F'. If the number of rows in `sa` is greater than or equal to the number of rows in `sb`, it fills in the undecided cells ('?') with 'F' under certain conditions; otherwise, it fills them with 'S'. The function then prints the modified grid.

