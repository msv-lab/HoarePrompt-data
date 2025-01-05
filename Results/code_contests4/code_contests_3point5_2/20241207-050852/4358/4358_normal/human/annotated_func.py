#State of the program right berfore the function call: **Precondition**: **n is an integer such that 1 <= n <= 300. The permutation p is a list of n distinct integers between 1 and n. The matrix A is a 2D list of characters with dimensions n x n where each character is either '0' or '1'. It is guaranteed that for all integers i, j where 1 ≤ i < j ≤ n, Ai, j = Aj, i holds and for all integers i where 1 ≤ i ≤ n, Ai, i = 0 holds.**
def func():
    __author__ = 'RASULBEK'
    n = input()
    p = map(int, raw_input().split())
    i = 0
    a = []
    while i < n:
        j = 0
        
        b = []
        
        s = raw_input()
        
        while j < len(s):
            if s[j] == '1':
                b.append(1)
            else:
                b.append(0)
            j += 1
        
        a.append(b)
        
        i += 1
        
    #State of the program after the loop has been executed: `n` is an integer such that 1 <= n <= 300, `p` is a list of n distinct integers between 1 and n, `A` is a 2D list of characters with dimensions n x n where each character is either '0' or '1', `i` is equal to `n`, `a` is a list of lists where each inner list corresponds to the input strings, `j` is equal to the length of the last input string, `b` is a list containing 1 or 0 based on the condition for each character in the last input string, `s` is the last entered string.
    i = 0
    while i < n:
        j = i + 1
        
        while j < n:
            if p[i] > p[j]:
                if a[i][j] == 1 and a[j][i] == 1:
                    tmp = p[i]
                    p[i] = p[j]
                    p[j] = tmp
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: Output State: `n` is an integer between 1 and 300, `p` is a list of n distinct integers between 1 and n sorted in non-decreasing order, `A` is a 2D list of characters with dimensions n x n, `i` is equal to `n`, `a` is a list of lists where each inner list corresponds to the input strings, `j` is equal to `n`, `b` is a list containing 1 or 0 based on the condition for each character in the last input string, `s` is the last entered string. The values in list `p` have been rearranged according to the conditions in the loop for all possible comparisons of elements in `p`.
    i = 0
    while i < n:
        j = i + 1
        
        while j < n:
            if p[i] > p[j]:
                if a[i][j] == 1 and a[j][i] == 1:
                    tmp = p[i]
                    p[i] = p[j]
                    p[j] = tmp
            j += 1
        
        i += 1
        
    #State of the program after the loop has been executed: `n` is an integer between 1 and 300, `p` is a list of n distinct integers between 1 and n sorted in non-decreasing order, `A` is a 2D list of characters with dimensions n x n, `i` is equal to `n`, `a` is a list of lists where each inner list corresponds to the input strings, `j` is equal to `n`, `b` is a list containing 1 or 0 based on the condition for each character in the last input string, `s` is the last entered string. The values in list `p` have been rearranged according to the conditions in the loop for all possible comparisons of elements in `p`.
    i = 0
    s = ''
    while i < n:
        s += str(p[i]) + ' '
        
        i += 1
        
    #State of the program after the loop has been executed: `n` is an integer between 1 and 300, `p` is a list of n distinct integers between 1 and n sorted in non-decreasing order, `A` is a 2D list of characters with dimensions n x n, `i` is equal to `n`, `a` is a list of lists where each inner list corresponds to the input strings, `j` is equal to `n`, `b` is a list containing 1 or 0 based on the condition for each character in the last input string, `s` is a string with all values of `p` concatenated with spaces in between
    print(s)
#Overall this is what the function does:The function `func` reads an integer `n`, a list of integers `p`, and a 2D list `A`. It then sorts the list `p` in non-decreasing order based on certain conditions. Finally, it concatenates the sorted `p` values into a string separated by spaces and prints the result. The function operates on global variables and does not explicitly return any value.

