#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input consists of n lines, each containing n characters. The j-th character of the i-th line is one of 'F', 'S', '?', or '.', where 'F' indicates a funny transition video, 'S' indicates a scary transition video, '?' indicates an undecided transition video, and '.' indicates that i=j. The i-th character of the j-th line is the same as the j-th character of the i-th line for all i and j. There are at most floor(n/2) characters in the input that are 'F' or 'S'.
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
        
    #State: `n` is 3, `a` is [1, 3, 4, 4], `b` is [1, 2, 3, 3], `xx` is ['', 'FSF', 'SSF', 'SFF']
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: n is 3, a is [1, 3, 4, 4], b is [1, 2, 3, 3], xx is ['', 'FSF', 'SSF', 'SFF'], sa is [], sb is [].
    if (len(sa) >= len(sb)) :
        t = len(sa)
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: the initial state of `sa`
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
            
        #State: A list of `n` strings, where each string is of length `n` and constructed by appending characters from `xx[i]` according to the conditions: if `xx[i][j - 1]` is not '?', append it; if `xx[i][j - 1]` is '?', append 'F' if `i` or `j` (or both) are in `sa[:n // 4 - 1]`; otherwise, append 'S'.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: n is 3, a is [1, 3, 4, 4], b is [1, 2, 3, 3], xx is ['', 'FSF', 'SSF', 'SFF'], sa is [], sb is [].
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
            
        #State: n is 3, a is [1, 3, 4, 4], b is [1, 2, 3, 3], xx is ['', 'FSF', 'SSF', 'SFF'], sa is [], sb is [].
    #State: `n` is 3, `a` is [1, 3, 4, 4], `b` is [1, 2, 3, 3], `xx` is ['', 'FSF', 'SSF', 'SFF']. If `len(sa) >= len(sb)`, `sa` contains a list of `n` strings, where each string is of length `n` and constructed by appending characters from `xx[i]` according to the conditions: if `xx[i][j - 1]` is not '?', append it; if `xx[i][j - 1]` is '?', append 'F' if `i` or `j` (or both) are in `sa[:n // 4 - 1]`; otherwise, append 'S'. Otherwise, `sa` and `sb` remain unchanged as empty lists.
#Overall this is what the function does:The function reads an integer `n` and an `n x n` grid of characters where each character is either 'F', 'S', '?', or '.', representing different types of transition videos or no transition. It processes the grid to replace '?' characters with either 'F' or 'S' based on the counts of 'F' and 'S' in each row and column, ensuring that the final grid has at most floor(n/2) 'F' or 'S' characters. The function then prints the modified grid.

