#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each element is greater than 0 and 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5 and the sum of q over all test cases does not exceed 3 * 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` and `q` are integers read from input where 1 <= n, q <= 3 * 10^5; `c` is a list of `n` integers where each element is greater than 0 and 1 <= c_i <= 10^9; For each query, `l_i` and `r_i` are integers such that 1 <= l_i <= r_i <= n; `a` is a list of `n + 1` integers where the first element is `0` and the next `n` elements are the integers read from the input; `b` is a list of `n + 1` integers where `b[i]` is the cumulative sum of `x` values from the start of the list `a` up to the `i`-th element, with `x` being 1 if `a[i] > 1` and 2 otherwise.
    a = list(accumulate(a))
    print(*a)
    #This is printed: 0, a[1], a[2], ..., a[n] (where a[i] is the cumulative sum of a[0] to a[i])
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: a sequence of q lines, each containing either 'YES' or 'NO' based on the condition for each query.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a list of integers and a set of queries. Each query specifies a range within the list. The function calculates the cumulative sum of the list and checks if the sum of the specified range meets a certain condition. It then prints 'YES' or 'NO' for each query based on this condition.

