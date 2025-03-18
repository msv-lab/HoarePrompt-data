#State of the program right berfore the function call: t is a positive integer, and for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5. The array c is a list of n positive integers where 1 ≤ c_i ≤ 10^9. For each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: `t` is a positive integer, `n` is an input integer, `q` is an input integer, `a` is a list starting with 0 followed by integers from the input split by spaces, `b` is a list of length `n + 1` where each element is calculated based on the formula `b[i] = b[i - 1] + x`, with `x = 1` if `a[i] > 1` else `2`.
    #
    #In simpler terms, after the loop executes all iterations, `b` will contain values where each element (except the first one which is 0) is the sum of the previous element in `b` and either 1 or 2, depending on whether the corresponding element in `a` is greater than 1 or not.
    a = list(accumulate(a))
    print(*a)
    #This is printed: [a[0], a[1], a[2], ..., a[n-1]]
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: Output State: t is a positive integer, n is an input integer, q is the number of iterations the loop has executed, a is a list where each element is the accumulated sum of the elements from the original input list up to that index, b is a list of length n + 1 where each element (except the first one which is 0) is the sum of the previous element in b and either 1 or 2 depending on whether the corresponding element in a is greater than 1 or not, the loop has printed 'NO' for pairs (x, y) where a[y] - a[x - 1] is less than b[y] - b[x - 1] or x equals y, and printed 'YES' otherwise for each iteration.
#Overall this is what the function does:The function processes a set of test cases, each consisting of an array `a` of length `n`, and `q` queries. For each query, it determines whether the sum of elements in the subarray from index `x` to `y` (inclusive) in `a` is greater than or equal to the sum of elements in the subarray from index `x` to `y` in a derived array `b`. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function does not return any value but prints the results of the queries.

