#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. The array c is a list of n integers where each element c_i is an integer such that 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5, and the sum of q over all test cases does not exceed 3 * 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `t` is an integer such that 1 <= t <= 10^4; for each test case, `n` and `q` are integers read from the input where 1 <= `n`, `q` <= 3 * 10^5; the array `c` is a list of `n` integers where each element `c_i` is an integer such that 1 <= `c_i` <= 10^9; for each query, `l_i` and `r_i` are integers such that 1 <= `l_i` <= `r_i` <= `n`; the sum of `n` over all test cases does not exceed 3 * 10^5, and the sum of `q` over all test cases does not exceed 3 * 10^5; `a` is a list where `a[0]` is 0 and `a[1:]` contains the integers from `c`; `b` is a list of `n + 1` integers where `b[i]` is the cumulative sum of 1 and 2 based on the condition `a[j] > 1` for `j` from 1 to `i`.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: The output state consists of `t` test cases, each with `n` integers in array `c`, `q` queries defined by pairs `(l_i, r_i)`, and the lists `a` and `b` computed as described. After executing the loop, the output will be a series of 'YES' or 'NO' responses for each query, based on the condition `a[y] - a[x - 1] < b[y] - b[x - 1]` or `x == y`. The values of `t`, `n`, `q`, `c`, `a`, and `b` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines whether the sum of the elements in the specified range of the list is at least as large as the number of elements in that range that are greater than 1. It outputs 'YES' if the condition is met and 'NO' otherwise.

