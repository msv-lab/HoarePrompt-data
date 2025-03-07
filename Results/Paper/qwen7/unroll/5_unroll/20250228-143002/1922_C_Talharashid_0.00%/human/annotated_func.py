#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is an integer such that 2 ≤ n ≤ 10^5, a is a list of n integers where 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9, m is an integer such that 1 ≤ m ≤ 10^5, and for each query, x_i and y_i are integers such that 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i.
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
        
    #State: The output state will consist of `t` lines, each containing an integer result from the given code snippet. For each iteration `i` (where `0 <= i < t`), the result is calculated based on the input list `lst` and the number of queries `m`. The result for each query is the minimum value of `s1` and `s2`, where `s1` is the sum of differences calculated from the left side of the list and `s2` is the sum of differences calculated from the right side of the list, for the specified subarray defined by `start` and `end`.
#Overall this is what the function does:The function processes multiple test cases, each involving a list of integers and a set of queries. For each test case, it calculates the sum of absolute differences between adjacent elements in the list from both left and right directions. It then responds to each query by providing the minimum value between the sums calculated from the left and right sides for the specified subarray. The function outputs the results for all queries in the form of integers, one per line.

