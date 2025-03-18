#State of the program right berfore the function call: t is a positive integer, each test case contains two integers n and q where 1 <= n, q <= 3 * 10^5, an array c of length n where each element is a positive integer not exceeding 10^9, and q subarray queries defined by pairs of integers l_i and r_i where 1 <= l_i <= r_i <= n.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: `t` is a positive integer, `n` is an input integer, `q` is an input integer, `c` is an array of length `n` where each element is a positive integer not exceeding \(10^9\), `a` is an array of length `n+1` where `a[0]` is 0 and the rest of the elements are the integers inputted separated by spaces, `b` is an array of length `n+1` where `b[0]` is 0 and `b[i]` for `i` from 1 to `n+1` is the sum of `x` for each iteration of the loop, `i` is `n+1`, `x` is 1 if `a[n]` > 1 else 2.
    #
    #Explanation: After the loop completes all its iterations, the variable `i` will be equal to `n+1` because the loop runs from `1` to `n`. The value of `x` will be determined by checking if `a[n]` is greater than 1 or not. The array `b` will have its last element `b[n]` as the sum of all `x` values calculated during each iteration of the loop. All other variables (`t`, `n`, `q`, `c`, `a`) will retain their initial or unchanged states as they are not modified within the loop.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: Output State: The value of `q` is 0, and the loop has completed all its iterations. For each iteration, based on the conditions provided, either 'NO' or 'YES' was printed depending on whether `a[y] - a[x - 1]` is less than `b[y] - b[x - 1]` or if `x` equals `y`. After the loop completes, there will be no further inputs or outputs, and the program terminates.
    #
    #In more detail, after all iterations of the loop have finished, the variable `q` which initially counted the number of iterations, is now 0. The loop has processed all its inputs, and for each input pair `(x, y)`, it printed 'NO' if the condition `a[y] - a[x - 1] < b[y] - b[x - 1]` or `x == y` was met, otherwise it printed 'YES'. The arrays `a` and `b` have been updated according to the loop's logic, but their exact values are not specified in the problem statement beyond their initial conditions and the operations performed within the loop. The variables `x` and `y` used in the loop are no longer relevant as the loop has ended.
#Overall this is what the function does:The function processes a series of subarray queries on an array `a`. It first constructs an auxiliary array `b` where `b[i]` is the sum of certain values up to index `i`. Then, for each query defined by indices `x` and `y`, it checks if the sum of elements in the subarray from `x` to `y` in array `a` is less than the corresponding sum in array `b`. If the condition is met or if `x` equals `y`, it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value but prints the result for each query.

