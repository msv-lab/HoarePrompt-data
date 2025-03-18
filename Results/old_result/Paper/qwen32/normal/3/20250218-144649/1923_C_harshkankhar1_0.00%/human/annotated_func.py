#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5. c is a list of n integers where each element c_i satisfies 1 ≤ c_i ≤ 10^9. For each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5, and the sum of q over all test cases does not exceed 3 · 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4; `n` is an integer such that 1 ≤ n ≤ 3 · 10^5; `q` is an integer such that 1 ≤ q ≤ 3 · 10^5; `c` is a list of `n` integers where each element `c_i` satisfies 1 ≤ `c_i` ≤ 10^9; `a` is a list where `a[0]` is 0 and `a[1]` to `a[n]` are the integers read from the input; For each query, `l_i` and `r_i` are integers such that 1 ≤ `l_i` ≤ `r_i` ≤ `n`; `b` is a list of `n + 1` integers where `b[0]` is 0 and `b[i]` for `i` from 1 to `n` is `b[i - 1] + x`, with `x` being 1 if `a[i] > 1` else 2; `i` is `n + 1`; all iterations of the loop have finished.
    a = list(accumulate(a))
    print(*a)
    #This is printed: 0 0 0 ... 0 (where there are n+1 zeros)
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: The loop has executed `q` times. For each of the `q` iterations, the program reads two integers `x` and `y` from the input, and prints 'NO' if `a[y] - a[x - 1] < b[y] - b[x - 1]` or `x == y`, otherwise it prints 'YES'. The values of `t`, `n`, `q`, `c`, `a`, `b`, and `i` remain unchanged from their initial state except that `i` is `n + 1` as specified.
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it reads an integer `n` and a list `c` of `n` integers, and an integer `q` representing the number of queries. Each query is defined by two integers `l_i` and `r_i`, specifying a range in the list `c`. The function determines and prints 'YES' or 'NO' for each query based on the comparison of the sum of elements and a derived value within the specified range of `c`.

