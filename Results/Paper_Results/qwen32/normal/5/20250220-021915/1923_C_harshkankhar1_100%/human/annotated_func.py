#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5. The array c is a list of n integers where each element is greater than 0 and less than or equal to 10^9. For each query i, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5 and the sum of q over all test cases does not exceed 3 · 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 1 ≤ n ≤ 3 · 10^5; `q` is an integer such that 1 ≤ q ≤ 3 · 10^5; The array `c` is a list of `n` integers where each element is greater than 0 and less than or equal to 10^9; For each query `i`, `l_i` and `r_i` are integers such that 1 ≤ `l_i` ≤ `r_i` ≤ `n`; The sum of `n` over all test cases does not exceed 3 · 10^5 and the sum of `q` over all test cases does not exceed 3 · 10^5; `a` is a list where the first element is `0` and the subsequent elements are integers read from the input; `b` is a list of `n + 1` integers where `b[i]` is the cumulative sum of `x` from `b[1]` to `b[i]` for all `i` from 1 to `n`, where `x` is 1 if `a[i] > 1` else 2.`
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: The loop has executed `q` times, and for each query, a value 'YES' or 'NO' has been printed based on the condition `a[y] - a[x - 1] < b[y] - b[x - 1] or x == y`. The values of `t`, `n`, `q`, `c`, `a`, and `b` remain unchanged from their initial state.
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of an integer `n`, an integer `q`, a list `c` of `n` integers, and `q` queries. Each query is defined by two integers `l_i` and `r_i`. For each query, the function determines whether the sum of elements in the subarray of `c` from index `l_i` to `r_i` (inclusive) is less than the cumulative sum of values `x` (where `x` is 1 if the element is greater than 1, otherwise 2) for the same subarray. It prints 'YES' if the condition is met and 'NO' otherwise.

