#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 500, c and d are integers such that 1 ≤ c, d ≤ 10^6, and l is a list of n^2 integers where each integer is in the range [1, 10^9].
def func_1(n, c, d, l):
    a = min(l)
    li = []
    for k in range(0, n):
        for h in range(0, n):
            li.append(a + k * c + d * h)
        
    #State: Output State: `n` is an integer such that 2 ≤ n ≤ 500, `c` and `d` are integers such that 1 ≤ c, d ≤ 10^6, `l` is a list of n^2 integers where each integer is in the range [1, 10^9], `a` is the minimum value from the list `l`, `li` is a list of n^2 integers where each integer is calculated as `a + k * c + d * h` for each combination of `k` and `h` in the range of 0 to n-1.
    li.sort()
    l.sort()
    if (l == li) :
        return 'yes'
        #The program returns 'yes'
    #State: Postcondition: `n` is an integer such that 2 ≤ n ≤ 500, `c` and `d` are integers such that 1 ≤ c, d ≤ 10^6, `l` is a list of n^2 integers where each integer is in the range [1, 10^9], `a` is the minimum value from the list `l`, `li` is a list of n^2 integers where each integer is calculated as `a + k * c + d * h` for each combination of `k` and `h` in the range of 0 to n-1, `li` is not sorted, `l` is sorted.
    return 'no'
    #The program returns 'no'
#Overall this is what the function does:The function accepts an integer \( n \) (where \( 2 \leq n \leq 500 \)), two integers \( c \) and \( d \) (where \( 1 \leq c, d \leq 10^6 \)), and a list \( l \) of \( n^2 \) integers (each integer in the range [1, \( 10^9 \)]). It calculates a new list \( li \) where each element is formed by adding the minimum value of \( l \) to a linear combination of indices \( k \) and \( h \) scaled by \( c \) and \( d \). Both \( l \) and \( li \) are then sorted. If the sorted lists \( l \) and \( li \) are identical, the function returns 'yes'; otherwise, it returns 'no'.

