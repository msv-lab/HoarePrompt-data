#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where each integer is between 1 and 10^9 inclusive; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `n + 1`; `x` will be 1 if `a[i]` (which is `a[n + 1]`) is greater than 1, else 2; `b[i]` (which is `b[n + 1]`) will be the sum of all `x` values from `b[0]` to `b[n]`.
    #
    #In simpler terms, after the loop completes all its iterations, `i` will be `n + 1`, `x` will depend on whether `a[n + 1]` is greater than 1, and `b[n + 1]` will be the cumulative sum of `x` values calculated during each iteration of the loop.
    a = list(accumulate(a))
    print(*a)
    #This is printed: [a[0], a[0] + a[1], ..., a[0] + a[1] + ... + a[n]]
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: `q` must be equal to the total number of iterations the loop will run, `x` is an input integer, `y` is an input integer, the output is either 'NO' or 'YES' depending on the condition a[y] - a[x - 1] < b[y] - b[x - 1] or x == y.
#Overall this is what the function does:The function processes a list `c` of `n` positive integers and handles `q` queries. For each query, it checks a range `[l_i, r_i]` within the list and returns 'YES' if the sum of elements in the range `[x, y]` is greater than or equal to the sum of `x` values in the same range, otherwise it returns 'NO'.

