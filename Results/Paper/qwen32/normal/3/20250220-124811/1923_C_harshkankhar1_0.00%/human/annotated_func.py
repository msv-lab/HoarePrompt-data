#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 1 <= n, q <= 3 * 10^5. c is a list of n integers where each element is greater than 0 and 1 <= c_i <= 10^9. For each query, l_i and r_i are integers such that 1 <= l_i <= r_i <= n. The sum of n over all test cases does not exceed 3 * 10^5 and the sum of q over all test cases does not exceed 3 * 10^5.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: `b` is a list where `b[0]` is 0 and `b[i]` for `1 <= i <= n` is the cumulative sum of `x` values determined by the condition `a[i] > 1`.
    a = list(accumulate(a))
    print(*a)
    #This is printed: a (where a is a list of cumulative sums of its original elements)
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: `b` is a list where `b[0]` is 0 and `b[i]` for `1 <= i <= n` is the cumulative sum of `x` values determined by the condition `a[i] > 1`; `a` is a list of cumulative sums of its original elements; `q` is 0; the loop has finished executing all `q` iterations; `x` and `y` are the integers read from the input in the last iteration; the program has printed 'NO' if `a[y] - a[x - 1] < b[y] - b[x - 1]` or `x == y`, otherwise it has printed 'YES'.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a list of integers and a series of queries. Each query specifies a range within the list. The function calculates and prints the cumulative sum of the list elements up to each index. Then, for each query, it checks if the sum of the elements in the specified range is at least as large as the count of elements greater than 1 in that range, excluding the case where the range consists of a single element, and prints 'YES' or 'NO' accordingly.

