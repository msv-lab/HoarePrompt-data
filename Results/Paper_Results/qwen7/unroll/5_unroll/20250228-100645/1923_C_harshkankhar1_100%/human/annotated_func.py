#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; the array c is a list of n positive integers where 1 ≤ c_i ≤ 10^9; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n; the sum of n over all test cases does not exceed 3 × 10^5; the sum of q over all test cases does not exceed 3 × 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: `t` is a positive integer, `n` and `q` are positive integers such that 1 ≤ n, q ≤ 3 × 10^5, the array `c` is a list of n positive integers where 1 ≤ c_i ≤ 10^9, the list `a` is `[0]` followed by integers split from input, where each integer is between 1 and 10^9 inclusive, the list `b` is a list of length n+1 where each element b[i] (for i from 1 to n) is equal to the number of times an integer greater than 1 appears before index i in list `a`.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: The output state will consist of 'YES' or 'NO' printed for each query based on the condition `a[y] - a[x - 1] >= b[y] - b[x - 1]` and `x != y`. The values of `t`, `n`, `q`, `c`, `a`, and `b` will remain unchanged after the loop executes all the iterations.
#Overall this is what the function does:The function processes multiple test cases, each defined by positive integers n and q, an array c of n positive integers, and q queries. For each query, it compares the sum of elements in the array c from index l to r with the count of elements greater than 1 in the same range. If the sum is greater than or equal to the count and l is not equal to r, it prints 'YES'; otherwise, it prints 'NO'. The function does not modify the input arrays c, a, and b, and it does not return any value.

