#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each test case contains n as an integer such that 2 ≤ n ≤ 10^5, a list a of n integers such that 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9, m as an integer such that 1 ≤ m ≤ 10^5, and m queries each containing two integers x_i and y_i such that 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. For each city, the closest city is determined uniquely.
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
        
    #State: After all iterations of the loop, the variables `t`, `n`, `m`, and the list `a` remain unchanged. The dictionaries `d1` and `d2` are populated with the cumulative minimum distances for each index in the list `a` when traversing from the start to the end and from the end to the start, respectively. For each query, the minimum distance between the two specified cities is printed.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the number of cities `n` and a list of city positions `a`, then calculates two dictionaries `d1` and `d2` that store the cumulative minimum distances for each index in `a` when traversing from the start to the end and from the end to the start, respectively. It then reads the number of queries `m` and a list of queries, each specifying two cities. For each query, it computes and prints the minimum distance between the two specified cities using the precomputed distances in `d1` and `d2`. The function does not return any values but prints the results of the queries. The input variables `t`, `n`, `m`, and the list `a` remain unchanged after the function execution.

