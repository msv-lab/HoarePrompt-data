#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 500, c and d are integers such that 1 <= c, d <= 10^6, and l is a list of n^2 integers where each integer b_i satisfies 1 <= b_i <= 10^9. The sum of n^2 over all test cases does not exceed 25 * 10^4.
def func_1(n, c, d, l):
    a = min(l)
    li = []
    for k in range(0, n):
        for h in range(0, n):
            li.append(a + k * c + d * h)
        
    #State: `t` is an integer such that 1 <= t <= 10^4. For each test case, `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, and `l` is a list of n^2 integers where each integer `b_i` satisfies 1 <= `b_i` <= 10^9. The sum of n^2 over all test cases does not exceed 25 * 10^4. `a` is the minimum value in the list `l`. `li` is a list of n^2 integers where each integer is of the form a + k * c + d * h for k, h in the range [0, n-1].
    li.sort()
    l.sort()
    if (l == li) :
        return 'yes'
        #The program returns 'yes'
    #State: `t` is an integer such that 1 <= t <= 10^4; for each test case, `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, `l` is a list of n^2 integers sorted in ascending order where each integer `b_i` satisfies 1 <= `b_i` <= 10^9, `a` is the minimum value in the list `l`, `li` is a list of n^2 integers where each integer is of the form a + k * c + d * h for k, h in the range [0, n-1], and `li` is sorted in ascending order. The list `l` is not equal to the list `li`.
    return 'no'
    #The program returns 'no'
#Overall this is what the function does:The function `func_1` checks if the input list `l` of `n^2` integers can be rearranged into a sorted list where each element is of the form `a + k * c + d * h` for `k, h` in the range `[0, n-1]`, with `a` being the minimum value in `l`. It returns 'yes' if such a rearrangement is possible, otherwise it returns 'no'.

