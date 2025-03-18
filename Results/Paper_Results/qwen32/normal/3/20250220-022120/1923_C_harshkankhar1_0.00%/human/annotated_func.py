#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n and q are integers such that 1 ≤ n, q ≤ 3 · 10^5. c is a list of n integers where each element is greater than 0 and less than or equal to 10^9. For each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n. The sum of n over all test cases does not exceed 3 · 10^5 and the sum of q over all test cases does not exceed 3 · 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is at least 1, `q` is an integer such that 1 ≤ q ≤ 3 · 10^5, `c` is a list of `n` integers where each element is greater than 0 and less than or equal to 10^9, `a` is a list where `a[0]` is 0 and `a[1]` to `a[n]` are the integers read from the input, `b` is a list of `n + 1` integers where `b[i]` is `b[i - 1] + x` for each `i` from 1 to `n` and `x` is 1 if `a[i] > 1` else 2.
    a = list(accumulate(a))
    print(*a)
    #This is printed: 0 c[0] c[0] + c[1] c[0] + c[1] + c[2] ... c[0] + c[1] + ... + c[n-1]
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n` is at least 1, `q` is 0, `c` is a list of `n` integers where each element is greater than 0 and less than or equal to 10^9, `a` is a list where `a[0]` is 0 and `a[i]` for `i` from 1 to `n` is the cumulative sum of the integers read from the input, `b` is a list of `n + 1` integers where `b[i]` is `b[i - 1] + x` for each `i` from 1 to `n` and `x` is 1 if `a[i] > 1` else 2, and all `q` queries have been processed, resulting in 'YES' or 'NO' printed for each query.
#Overall this is what the function does:The function `func_1` processes multiple test cases. For each test case, it reads an integer `n` and a list `c` of `n` integers. It then processes `q` queries, each consisting of two integers `l_i` and `r_i`. For each query, it determines if the sum of the elements in `c` from index `l_i` to `r_i` (inclusive) is at least as large as the count of elements in that range that are greater than 1, and prints 'YES' if true, otherwise 'NO'.

