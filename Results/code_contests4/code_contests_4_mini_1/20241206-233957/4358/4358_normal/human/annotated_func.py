#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 300; p is a list of n distinct integers where each integer is between 1 and n; A is an n x n binary matrix where for all integers i, j (1 ≤ i < j ≤ n), Ai, j = Aj, i holds, and Ai, i = 0 for all integers i (1 ≤ i ≤ n).
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
        
    #State of the program after the loop has been executed: `n` is a string representation of a number greater than or equal to 0, `p` is a map object of distinct integers, `A` is an `n` x `n` binary matrix filled with the binary representations of the input strings, `__author__` is 'RASULBEK', `i` is equal to `n`, `j` is equal to the length of the last string `s`, `a` is a list containing `n` lists, where each inner list `b` contains integers where each element is 1 if the corresponding character in the respective input string `s` is '1' and 0 if it is '0'.
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
        
    #State of the program after the loop has been executed: `n` is a string representation of a number greater than or equal to 0, `i` is equal to `n`, `j` is equal to `n`, `p` remains unchanged, and `a` remains unchanged.
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
        
    #State of the program after the loop has been executed: `n` is a string representation of a number greater than or equal to 0, `i` is equal to `n`, `j` is equal to `n`, and `p` and `a` remain unchanged.
    i = 0
    s = ''
    while i < n:
        s += str(p[i]) + ' '
        
        i += 1
        
    #State of the program after the loop has been executed: `i` is equal to the integer value of `n`, `n` is a string representation of a number greater than or equal to 0, `j` is equal to `n`, `p` is unchanged, `a` is unchanged, and `s` is updated to include the string representations of all elements in `p` from index 0 to `i-1`, separated by spaces.
    print(s)
#Overall this is what the function does:The function accepts an integer `n`, a list `p` of `n` distinct integers, and an \( n \times n \) binary matrix. It processes these inputs to swap elements in `p` based on conditions defined by the binary matrix `A`. The result is a space-separated string of the integers in `p` after the potential swaps are performed. Note that the function does not handle invalid inputs or cases where `n` is not properly defined, which may lead to incorrect behavior.

