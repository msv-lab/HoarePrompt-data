#State of the program right berfore the function call: t is a positive integer; for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5; c is a list of n positive integers where each element is between 1 and 10^9 inclusive; for each query, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: `i` is equal to `n`, `x` is 1 if `a[n]` is greater than 1 else `x` is 2, `b[n]` is the sum of `b[0]` and the sequence of `x` values added up from `i=1` to `i=n`.
    #
    #In simpler terms, after the loop has executed all its iterations, the variable `i` will be equal to the input integer `n`. The variable `x` will be 1 if the last element of the list `a` (i.e., `a[n]`) is greater than 1, otherwise it will be 2. The list `b` will have its final value at index `n` as the cumulative sum of `x` starting from `b[0]` and adding `x` for each iteration from `i=1` to `i=n`.
    a = list(accumulate(a))
    print(*a)
    #This is printed: 1 3 6 10
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: q is a positive integer decremented by the number of times the loop has executed, x and y are input integers for each iteration, and the program prints 'NO' if a[y] - a[x - 1] is less than b[y] - b[x - 1] or if x equals y, otherwise it prints 'YES'.
#Overall this is what the function does:The function processes a list of integers `a` and handles a series of queries. It first calculates a cumulative sum list `b` based on the values in `a`. Then, for each query, it compares the sum of a specified sublist in `a` with a corresponding value derived from `b`, and prints 'YES' if the sum in `a` is greater than or equal to the value from `b`, or 'NO' otherwise.

