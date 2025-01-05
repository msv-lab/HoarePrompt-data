#State of the program right berfore the function call: **Precondition**: 
- n is an integer such that 1 <= n <= 300.
- p is a list of n distinct integers between 1 and n.
- A is a 2D list of characters with dimensions n x n, where each character is either '0' or '1'.
- For all integers i,j where 1 <= i < j <= n, A[i][j] = A[j][i].
- For all integers i where 1 <= i <= n, A[i][i] = '0'.
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
        
    #State of the program after the loop has been executed: `i` is the sum of the first `n` positive integers, `a` is a list of lists containing the converted values from strings, `n` remains the same
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
        
    #State of the program after the loop has been executed: `i` is equal to `n-1`, `n` is the sum of the first `n` positive integers, `a` is a list of lists containing the converted values from strings, `j` is equal to `n`, `p` is sorted in non-decreasing order based on the values in `p`, the list `a` may have been updated based on the conditions in the loop, `tmp` is a temporary variable used for swapping values.
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
        
    #State of the program after the loop has been executed: `i` is equal to `n`, `n` is the sum of the first `n` positive integers, `a` is a list of lists containing converted values from strings, `j` is equal to `n`, `p` is sorted in non-decreasing order based on the values in `p`, the list `a` may have been updated based on the conditions in the loop, `tmp` is a temporary variable used for swapping values
    i = 0
    s = ''
    while i < n:
        s += str(p[i]) + ' '
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is equal to `n`, `s` contains the concatenated string of all elements in `p` up to index `n-1` separated by a space
    print(s)
#Overall this is what the function does:The function `func` reads input data according to predefined constraints and processes it to sort the values in list `p` in non-decreasing order. It then prints the sorted values as a concatenated string separated by spaces. The function does not accept any parameters and solely operates on the provided input data.

