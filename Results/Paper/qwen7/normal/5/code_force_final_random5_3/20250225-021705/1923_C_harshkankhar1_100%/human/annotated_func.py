#State of the program right berfore the function call: t is a positive integer, each test case contains two integers n and q where 1 <= n, q <= 3 * 10^5, an array c of length n where each element is a positive integer not exceeding 10^9, and q queries defined by pairs of integers l_i and r_i where 1 <= l_i <= r_i <= n.
def func_1():
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: Output State: After the loop executes all its iterations, `a[i]` will be either greater than 1 or less than or equal to 1 for each `i` from 1 to `n`. The variable `x` will be 1 if `a[i]` is greater than 1, otherwise it will be 2. The list `b` will be updated such that for every `i` from 1 to `n`, `b[i]` will be the sum of `b[i-1]` and `x`. Specifically, `b[i]` will be the cumulative sum of `x` values from `i=1` to `i`. The variable `i` will be `n` after the loop completes, and `b[n+1]` will be `b[n] + x` where `x` is determined by `a[n]`.
    #
    #In simpler terms, after all iterations, `b[i]` will hold the total count of occurrences where `a[i]` was greater than 1 up to index `i`, and `b[n+1]` will be the final count including the last iteration.
    a = list(accumulate(a))
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: Output State: After all iterations of the loop have finished, `q` will be 0 (since it starts as a positive integer and decreases by 1 with each iteration until it reaches 0), `x` and `y` will be the last pair of integers input during the loop's final iteration. The program will print 'NO' if `a[y] - a[x - 1] < b[y] - b[x - 1]` or if `x == y`, otherwise it will print 'YES'. The variables `a`, `b`, and `i` will reflect their final states after all iterations, with `i` being `n` (the total number of elements in the list `a`), and `b[n+1]` being `b[n] + x` where `x` is determined by the final value of `a[n]`.
    #
    #In simpler terms, after running the loop through all its iterations, `q` will be zero, and the program will make its final decision ('NO' or 'YES') based on the last inputs `x` and `y`, using the updated lists `a` and `b`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an array `a` of positive integers and a set of queries. For each query, it compares the sum of elements in a specified subarray with a cumulative count related to those elements. If the sum of the subarray is less than the cumulative count or if the query indices are the same, it prints 'NO'; otherwise, it prints 'YES'. The function ultimately prints the result for each query and does not return any value.

