#State of the program right berfore the function call: t is a positive integer, each test case consists of n and q where 1 <= n, q <= 3 * 10^5, an array c of length n where each element is a positive integer not exceeding 10^9, and q queries each defined by a pair of integers l_i and r_i representing the borders of the subarray to check if it is good.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: n is an integer, q is an integer, t is a positive integer, a is a list starting with 0 followed by integers, b is a list where each element b[i] (for i from 1 to n) is the sum of b[0] and the value 1 if a[i] > 1 or 2 otherwise for all previous elements.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: a is a list of cumulative sums, b is a list where each element b[i] is the sum of b[0] and the value 1 if a[i] > 1 or 2 otherwise for all previous elements, n is an integer, q is an integer, t is a positive integer, the loop has executed q times with user inputs (x, y), and printed 'NO' if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y, otherwise printed 'YES'.
#Overall this is what the function does:The function processes a set of inputs including a positive integer `t`, followed by pairs of integers `n` and `q` where 1 <= n, q <= 3 * 10^5, an array `a` of length `n` where each element is a positive integer not exceeding 10^9, and `q` queries each defined by a pair of integers `l_i` and `r_i` representing the borders of the subarray. For each query, it checks if the subarray from index `l_i` to `r_i` is "good" and prints 'YES' if the subarray is good, otherwise prints 'NO'. The function does not return any value but modifies the standard output based on the queries.

