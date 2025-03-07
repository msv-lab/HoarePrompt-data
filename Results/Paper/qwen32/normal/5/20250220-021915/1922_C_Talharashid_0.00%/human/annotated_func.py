#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and a is a list of n integers where 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9. m is an integer such that 1 ≤ m ≤ 10^5, and for each query, x_i and y_i are integers such that 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. For every city in each test case, the closest city is uniquely determined.
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
        
    #State: `t` is an input integer such that \(1 \leq t \leq 10^4\); `i` is `t - 1` (indicating that the loop has completed all `t` iterations); `d1` and `d2` are default dictionaries that store cumulative sums `s` for each city when traversed from the start to the end and from the end to the start, respectively, for the last test case; `n` is the number of cities in the last test case; `lst` is the list of city positions for the last test case; `start` and `end` are the last indices used for the queries in the last test case; `inc` is -1 for the last traversal; `m` is the number of queries in the last test case; `s` is 0 for the last query.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it receives a list of city positions and a series of queries. Each query specifies two cities, and the function calculates and prints the minimum distance required to reach the closest city to the midpoint of the two specified cities.

