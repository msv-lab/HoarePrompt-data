#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 500, c and d are integers such that 1 ≤ c, d ≤ 10^6, and l is a list of n^2 integers where each integer b_i satisfies 1 ≤ b_i ≤ 10^9. The sum of n^2 over all test cases does not exceed 25 * 10^4.
def func_1(n, c, d, l):
    a = min(l)
    li = []
    for k in range(0, n):
        for h in range(0, n):
            li.append(a + k * c + d * h)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 2 ≤ n ≤ 500, `c` and `d` are integers such that 1 ≤ c, d ≤ 10^6, `l` is a list of `n^2` integers where each integer `b_i` satisfies 1 ≤ b_i ≤ 10^9, `a` is the minimum value in the list `l`, `li` is a list containing `n^2` elements where the `i-th` element is `a + k * c + d * h` for `k` ranging from 0 to `n-1` and `h` ranging from 0 to `n-1`.
    li.sort()
    l.sort()
    if (l == li) :
        return 'yes'
        #The program returns 'yes'
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is an integer such that 2 ≤ n ≤ 500, `c` and `d` are integers such that 1 ≤ c, d ≤ 10^6, `l` is a sorted list of `n^2` integers where each integer `b_i` satisfies 1 ≤ b_i ≤ 10^9, `a` is the minimum value in the list `l`, `li` is a sorted list containing `n^2` elements where the `i-th` element is `a + k * c + d * h` for `k` ranging from 0 to `n-1` and `h` ranging from 0 to `n-1`. The list `l` is not equal to the list `li`.
    return 'no'
    #The program returns 'no'
#Overall this is what the function does:The function `func_1` takes four parameters: `n` (the size of a matrix), `c` and `d` (two integers), and `l` (a list of `n^2` integers representing the elements of the matrix). It returns 'yes' if the list `l` can be rearranged to match a specific sequence generated based on the minimum value in `l` and the integers `c` and `d`; otherwise, it returns 'no'.

