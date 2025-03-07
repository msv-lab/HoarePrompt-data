#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5; c is a list of n integers where each integer c_i satisfies 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 · 10^5; the sum of q over all test cases does not exceed 3 · 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; for each test case, `n` and `q` are integers such that 1 ≤ `n`, `q` ≤ 3 · 10^5; `c` is a list of `n` integers where each integer `c_i` satisfies 1 ≤ `c_i` ≤ 10^9; for each query, `l_i` and `r_i` are integers such that 1 ≤ `l_i` ≤ `r_i` ≤ `n`; the sum of `n` over all test cases does not exceed 3 · 10^5; the sum of `q` over all test cases does not exceed 3 · 10^5; `a` is a list where `a[0]` is `0` and `a[1:]` contains the integers read from the input; `b` is a list of `n + 1` elements where `b[0]` is `0` and `b[i]` for `i` from `1` to `n` is the cumulative sum of `x` values calculated as `x = 1 if a[i] > 1 else 2`.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; for each test case, `n` and `q` are integers such that 1 ≤ `n`, `q` ≤ 3 · 10^5; `c` is a list of `n` integers where each integer `c_i` satisfies 1 ≤ `c_i` ≤ 10^9; `a` is a list where `a[0]` is `0` and `a[i]` for `i` from `1` to `n` is the cumulative sum of the original `c` list elements up to index `i`; `b` is a list of `n + 1` elements where `b[0]` is `0` and `b[i]` for `i` from `1` to `n` is the cumulative sum of `x` values calculated as `x = 1 if a[i] > 1 else 2`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines whether the sum of the elements in a specified range of the list is at least as large as the number of elements in that range that are greater than 1. It outputs "YES" if the condition is met and "NO" otherwise.

