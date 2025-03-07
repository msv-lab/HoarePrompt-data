#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and a is a list of n non-negative integers in strictly increasing order (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9). m is an integer such that 1 ≤ m ≤ 10^5, and for each query, x_i and y_i are distinct integers such that 1 ≤ x_i, y_i ≤ n.
def func():
    t = int(input())
    for i in range(t):
        d1 = defaultdict(int)
        
        d2 = defaultdict(int)
        
        n = int(input())
        
        lst = list(map(int, input().split()))
        
        start = 0
        
        end = len(lst) - 1
        
        inc = 1
        
        s = 0
        
        while start != end:
            mini = 11111111
            if start + 1 < len(lst):
                mini = min(abs(lst[start] - lst[start + 1]), mini)
            if start - 1 > -1:
                mini = min(abs(lst[start] - lst[start - 1]), mini)
            if mini == abs(lst[start] - lst[start + inc]):
                s += 1
            else:
                s += abs(lst[start] - lst[start + inc])
            start += inc
            d1[start] = s
        
        start = len(lst) - 1
        
        end = 0
        
        inc = -1
        
        s = 0
        
        while start != end:
            mini = 11111111
            if start + 1 < len(lst):
                mini = min(abs(lst[start] - lst[start + 1]), mini)
            if start - 1 > -1:
                mini = min(abs(lst[start] - lst[start - 1]), mini)
            if mini == abs(lst[start] - lst[start + inc]):
                s += 1
            else:
                s += abs(lst[start] - lst[start + inc])
            start += inc
            d2[start] = s
        
        m = int(input())
        
        for i in range(m):
            start, end = map(int, input().split())
            start -= 1
            end -= 1
            s = 0
            if start < end:
                s1 = abs(d1[end] - d1[start])
                s2 = abs(d2[start] - d2[end])
            else:
                s1 = abs(d2[end] - d2[start])
                s2 = abs(d1[start] - d1[end])
            print(min(s1, s2))
        
    #State: Output State: After the loop executes all its iterations, the variable `i` will be equal to `m-1`. The variables `start` and `end` will be adjusted based on the number of iterations `m`. Specifically, `start` will be the initial value of `start` minus `2 * m`, and `end` will be the last `end` value entered by the user minus 1. The variable `s` will be 0 because it is reset to 0 at the beginning of each iteration. The variable `s2` will hold the minimum absolute difference calculated from the values in `d1` and `d2` arrays, depending on whether `start` is less than `end`.
    #
    #In summary, the final state of the variables after the loop completes all iterations will be:
    #- `i`: `m-1`
    #- `start`: Initial `start` value minus `2 * m`
    #- `end`: Last `end` value minus 1
    #- `s`: 0
    #- `s2`: Minimum absolute difference from `d1` and `d2` arrays based on the condition `start < end`
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer n, a strictly increasing list of n non-negative integers, and an integer m representing the number of queries. It then handles each query by calculating the minimum absolute difference between the values at indices x_i and y_i in the list. The function outputs these minimum differences for all queries.

