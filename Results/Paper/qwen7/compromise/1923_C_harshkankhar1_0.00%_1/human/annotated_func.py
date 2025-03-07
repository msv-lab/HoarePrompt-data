#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; the array c is a list of n positive integers where 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are positive integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: `t` is a positive integer, `n` is an input integer, `q` is an input integer, `a` is a list starting with 0 followed by integers entered as input, `b` is a list of length `n + 1` where each element is calculated based on the previous element and the value of `a[i]` (if `a[i] > 1`, then `x = 1`, otherwise `x = 2`), starting from `b[0] = 0`.
    a = list(accumulate(a))
    print(*a)
    #This is printed: the cumulative sums of the original list `a`
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: Output State: `t` is a positive integer, `n` is an input integer, `q` is an input integer, `a` is a list where each element is the cumulative sum of the elements in the original list `a`, `b` is a list of length `n + 1` where each element is calculated based on the previous element and the value of `a[i]` (if `a[i] > 1`, then `x = 1`, otherwise `x = 2`), starting from `b[0] = 0`, the loop iterates `q` times, each time reading two integers `x` and `y` from input, and printing 'NO' if `a[y] - a[x - 1] < b[y] - b[x - 1]` or `x == y`, otherwise printing 'YES'. The values of `t`, `n`, `q`, `a`, and `b` remain unchanged after the loop executes all iterations.
#Overall this is what the function does:The function processes a series of test cases. Each test case includes an integer `n`, an integer `q`, an array `a` of `n` positive integers, and `q` queries. Each query consists of two integers `x` and `y`. For each query, the function checks whether the subarray of `a` from index `x-1` to `y-1` meets the condition `a[y] - a[x-1] >= b[y] - b[x-1]` and `x != y`. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the results for each query.

