#State of the program right berfore the function call: t is a positive integer, each test case consists of two integers n and q where 1 <= n, q <= 3 * 10^5, an array c of length n where each element is a positive integer not exceeding 10^9, and q subarray queries defined by pairs of integers l_i and r_i where 1 <= l_i <= r_i <= n.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: `b` is a list of length `n + 1` where each element `b[i]` (for `i` from 1 to `n`) is equal to `i` if `a[i] > 1`, otherwise `2 * i`. The first element `b[0]` remains `0`.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: Output State: The output state consists of a series of 'YES' and 'NO' printed for each iteration of the loop based on the condition `a[y] - a[x - 1] >= b[y] - b[x - 1]` with `x != y`. The variables `a` and `b` remain unchanged from their initial state after the loop has executed all its iterations.
#Overall this is what the function does:The function processes a set of inputs including an integer `n`, an integer `q`, an array `c` of length `n` containing positive integers, and `q` subarray queries defined by pairs of integers `l_i` and `r_i`. It calculates and stores cumulative sums in array `a` and a modified cumulative sum-like array `b`. For each subarray query, it determines whether the sum of elements in the subarray defined by `l_i` to `r_i` is greater than or equal to a specific value derived from `b`, and prints 'YES' or 'NO' accordingly. The function does not return any value but prints the results of the subarray queries.

