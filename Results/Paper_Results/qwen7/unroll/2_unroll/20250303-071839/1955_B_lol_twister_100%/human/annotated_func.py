#State of the program right berfore the function call: n is an integer such that 2 <= n <= 500, c and d are integers such that 1 <= c, d <= 10^6, and l is a list of integers such that 1 <= l_i <= 10^9 and the length of l is n^2.
def func_1(n, c, d, l):
    a = min(l)
    li = []
    for k in range(0, n):
        for h in range(0, n):
            li.append(a + k * c + d * h)
        
    #State: Output State: `a` is the minimum value in the list `l`, `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, and `l` is a list of integers where each element `l[i]` (for i in 0 to n^2-1) is given by `a + floor(i/n) * c + i % n * d`; `li` is a list of length n^2 containing the same elements as `l`.
    li.sort()
    l.sort()
    if (l == li) :
        return 'yes'
        #The program returns 'yes'
    #State: `a` is the minimum value in the list `l`, `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, and `l` is a list of integers where each element `l[i]` (for i in 0 to n^2-1) is given by `a + floor(i/n) * c + i % n * d`; `li` is a list of length n^2 containing the same elements as `l` sorted in ascending order, but `l` is not sorted in ascending order
    return 'no'
    #The program returns 'no'
#Overall this is what the function does:The function accepts four parameters: an integer \( n \) (where \( 2 \leq n \leq 500 \)), two integers \( c \) and \( d \) (where \( 1 \leq c, d \leq 10^6 \)), and a list of integers \( l \) (where the length of \( l \) is \( n^2 \) and \( 1 \leq l_i \leq 10^9 \)). It calculates a new list \( li \) based on the values of \( a \) (the minimum value in \( l \)), \( c \), \( d \), and \( n \). If the original list \( l \) is sorted in the same way as \( li \), the function returns 'yes'; otherwise, it returns 'no'.

