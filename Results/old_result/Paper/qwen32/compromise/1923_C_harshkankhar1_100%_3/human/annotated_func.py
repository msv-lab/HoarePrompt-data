#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each element is greater than 0 and 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5 and the sum of q over all test cases does not exceed 3 * 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `b` is a list of n+1 integers where `b[0]` is 0 and `b[i]` for 1 <= i <= n is the cumulative sum of 1s and 2s based on the condition `a[j] > 1` for 1 <= j <= i.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: `b` is a list of `n+1` integers where `b[0]` is 0 and `b[i]` for `1 <= i <= n` is the cumulative sum of 1s and 2s based on the condition `a[j] > 1` for `1 <= j <= i`; `a` is a list where each element `a[i]` is the cumulative sum of the elements from `a[0]` to `a[i]`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines whether the sum of the elements in a specified sublist is greater than the count of elements in that sublist that are greater than 1. It outputs "YES" if the sum is greater and "NO" otherwise.

