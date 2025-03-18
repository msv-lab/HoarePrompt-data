#State of the program right berfore the function call: n is an integer such that 2 <= n <= 24. The input is a list of n strings, each of length n, containing characters 'F', 'S', '?', or '.'. The character at the i-th row and j-th column is the same as the character at the j-th row and i-th column for all i and j, and at most 2 * floor(n / 2) characters in the input are 'F' or 'S'.
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
        
    #State: After the loop executes all iterations, `n` remains the same as the initial input. The list `xx` contains `n + 1` elements, where the first element is an empty string and the next `n` elements are the input strings provided during the loop execution. The lists `a` and `b` are updated such that for each input string `x` at iteration `i`, if the character at index `k` in `x` is 'F', both `a[i]` and `a[k+1]` are incremented by 1. If the character at index `k` in `x` is 'S', both `b[i]` and `b[k+1]` are incremented by 1. All other indices in `a` and `b` remain unchanged.
    sa = []
    sb = []
    for i in range(1, n + 1):
        if a[i] > 0 and b[i] == 0:
            sa.append(i)
        
        if b[i] > 0 and a[i] == 0:
            sb.append(i)
        
    #State: After the loop executes all iterations, `n` remains the same as the initial input, `xx` contains `n + 1` elements where the first element is an empty string and the next `n` elements are the input strings provided during the loop execution. `sa` is a list containing all indices `i` (from 1 to `n`) where `a[i] > 0` and `b[i] == 0`. `sb` is a list containing all indices `i` (from 1 to `n`) where `b[i] > 0` and `a[i] == 0`.
    if (len(sa) >= len(sb)) :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sa.append(i)
            
        #State: `n` remains the same as the initial input, `xx` remains unchanged, `sa` contains all indices `i` (from 1 to `n`) where `a[i] == 0` and `b[i] == 0`, and `sb` remains unchanged.
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
            
        #State: The loop has completed all iterations, `n` remains unchanged, `xx` remains unchanged, `sa` contains all indices `i` (from 1 to `n`) where `a[i] == 0` and `b[i] == 0`, `sb` remains unchanged, `i` is `n + 1`, and `nx` is a string of length `n` for each `i` from 1 to `n`, where each character is determined by the conditions in the loop: if `xx[i][j - 1]` is not '?', the character is the one at position `j - 1` in `xx[i]`; if `xx[i][j - 1]` is '?' and `i` or `j` is in the first quarter of `sa` (i.e., `sa[:n // 4]`), the character is 'F'; otherwise, the character is 'S'.
    else :
        for i in range(1, n + 1):
            if a[i] == 0 and b[i] == 0:
                sb.append(i)
            
        #State: `n` remains the same as the initial input, `i` is `n + 1`, and `sb` is a list that contains all indices `i` (from 1 to `n`) where both `a[i]` and `b[i]` are 0. The lists `sa` and `xx` remain unchanged.
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
            
        #State: `n` remains the same, `i` is `n + 1`, and `nx` is a string of length `n` for each iteration of `i` from 1 to `n`, where each character in `nx` is determined as follows: If `xx[i][j - 1]` is not equal to '?', the character is `xx[i][j - 1]`. If `xx[i][j - 1]` is equal to '?' and either `i` or `j` is in the first `n // 4` elements of the list `sb`, the character is 'S'. Otherwise, the character is 'F'.
    #State: After the loop executes all iterations, `n` remains the same as the initial input, `xx` contains `n + 1` elements where the first element is an empty string and the next `n` elements are the input strings provided during the loop execution. `i` is `n + 1`. If `len(sa) >= len(sb)`, `sa` contains all indices `i` (from 1 to `n`) where `a[i] == 0` and `b[i] == 0`, `sb` remains unchanged, and `nx` is a string of length `n` for each `i` from 1 to `n`, where each character is determined by the conditions in the loop: if `xx[i][j - 1]` is not '?', the character is the one at position `j - 1` in `xx[i]`; if `xx[i][j - 1]` is '?' and `i` or `j` is in the first quarter of `sa` (i.e., `sa[:n // 4]`), the character is 'F'; otherwise, the character is 'S'. If `len(sa) < len(sb)`, `nx` is a string of length `n` for each iteration of `i` from 1 to `n`, where each character in `nx` is determined as follows: if `xx[i][j - 1]` is not equal to '?', the character is `xx[i][j - 1]`; if `xx[i][j - 1]` is equal to '?' and either `i` or `j` is in the first `n // 4` elements of the list `sb`, the character is 'S'; otherwise, the character is 'F'.
#Overall this is what the function does:The function reads an integer `n` and a list of `n` strings, each of length `n`, from the user. It processes this symmetric matrix, counting the occurrences of 'F' and 'S' in each row and column. The function then identifies indices where only 'F' or 'S' are present and appends indices with no 'F' or 'S' to the appropriate list. Based on the size of these lists, it updates the matrix by replacing '?' characters: if the list of 'F' indices is larger or equal, it replaces '?' with 'F' for the first quarter of these indices and with 'S' otherwise; if the list of 'S' indices is larger, it replaces '?' with 'S' for the first quarter of these indices and with 'F' otherwise. The function prints the updated matrix. The final state of the program is that `n` remains unchanged, the original input matrix `xx` is unchanged, and the updated matrix is printed.

