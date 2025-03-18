#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. The array c is a list of n integers where each integer c_i satisfies 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5, and the sum of q over all test cases does not exceed 3 * 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is at least 1, `q` is an integer such that 1 <= q <= 3 * 10^5, the array `c` is a list of `n` integers where each integer `c_i` satisfies 1 <= `c_i` <= 10^9, for each query, `l_i` and `r_i` are integers such that 1 <= `l_i` <= `r_i` <= `n`, the sum of `n` over all test cases does not exceed 3 * 10^5, and the sum of `q` over all test cases does not exceed 3 * 10^5, `a` is a list where `a[0]` is 0 and `a[1:]` contains the integers read from the input, `b` is a list of `n + 1` integers where `b[i]` is the cumulative sum of `x` from `a[1]` to `a[i]` for all `i` from 1 to `n`, `x` is 1 if `a[i] > 1` else 2, and the loop has completed all iterations.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: `t` is an integer such that 1 <= t <= 10^4, `n` is at least 1, `q` is an integer such that 0 <= q <= 3 * 10^5, `c` is a list of `n` integers where each integer `c_i` satisfies 1 <= `c_i` <= 10^9, `a` is a list where `a[i]` is the cumulative sum of the integers from `a[0]` to `a[i]` for all `i` from 0 to `n`, `b` is a list of `n + 1` integers where `b[i]` is the cumulative sum of `x` from `a[1]` to `a[i]` for all `i` from 1 to `n`, and all `q` queries have been processed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and an array `a` of `n` integers. It then processes `q` queries, each defined by two integers `x` and `y`. For each query, it prints 'YES' if the sum of the elements in the subarray from index `x` to `y` (inclusive) is greater than or equal to the number of elements in that subarray that are greater than 1, otherwise it prints 'NO'.

