#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each element c_i satisfies 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5 and the sum of q over all test cases does not exceed 3 * 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `t` remains the same integer; `n` and `q` remain the same integers; `c` remains the same list of integers; `a` remains the same list of integers; `b` is a list where `b[i]` is the cumulative sum of 1s and 2s based on the condition `a[i] > 1` for each `i` from 1 to `n`.
    a = list(accumulate(a))
    print(*a)
    #This is printed: a[0], a[1], a[2], ..., a[n-1] (where each a[i] is the cumulative sum of the elements up to the i-th index in the list c)
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: `t` remains the same integer; `n` and `q` remain the same integers; `c` remains the same list of integers; `a` is still a list of integers where each element is the cumulative sum of the elements up to that index in the original list; `b` is still a list where `b[i]` is the cumulative sum of 1s and 2s based on the condition `a[i] > 1` for each `i` from 1 to `n`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a list of integers and a series of queries. For each query, it determines if the sum of the integers in a specified sub-list meets a certain condition compared to a derived cumulative sum list. It prints 'YES' if the condition is met (except when the sub-list has only one element), otherwise it prints 'NO'.

