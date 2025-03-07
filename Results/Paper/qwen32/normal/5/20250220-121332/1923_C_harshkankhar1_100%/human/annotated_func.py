#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each element is greater than 0 (1 <= c_i <= 10^9). For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5, and the sum of q over all test cases does not exceed 3 * 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer such that 1 <= n <= 3 * 10^5; `q` is an integer such that 1 <= q <= 3 * 10^5; `c` is a list of `n` integers where each element is greater than 0 (1 <= c_i <= 10^9); `a` is a list of `n + 1` integers where the first element is 0 and the remaining `n` elements are the integers read from the input; `b` is a list of `n + 1` integers, where each `b[i]` is the cumulative sum of `x` values from `b[1]` to `b[i]` with `x` being 1 if `a[i] > 1` else 2; `i` is `n`; `x` is 1 if `a[n] > 1` else 2.`
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` is an integer such that 1 <= n <= 3 * 10^5; `q` is an integer such that 1 <= q <= 3 * 10^5; `c` is a list of `n` integers where each element is greater than 0 (1 <= c_i <= 10^9); `a` is a list of `n + 1` integers where `a[i]` is the cumulative sum of the first `i` elements of the original `a`; `b` is a list of `n + 1` integers, where each `b[i]` is the cumulative sum of `x` values from `b[1]` to `b[i]` with `x` being 1 if `a[i] > 1` else 2; `i` is `n`; `x` and `y` are the last pair of integers read from the input; the program has printed 'YES' or 'NO' for each of the `q` queries.
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it reads an integer `n` and a list `c` of `n` integers, and an integer `q` representing the number of queries. Each query consists of two integers `l_i` and `r_i` defining a range within the list `c`. The function then determines for each query whether the sum of elements in the range `[l_i, r_i]` is greater than or equal to the number of elements in that range that are greater than 1, printing 'YES' if true and 'NO' otherwise.

