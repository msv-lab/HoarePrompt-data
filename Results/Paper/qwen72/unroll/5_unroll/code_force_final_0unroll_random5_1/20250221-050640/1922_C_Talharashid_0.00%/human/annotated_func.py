#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, each test case contains n (2 ≤ n ≤ 10^5) and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9) representing the coordinates of the cities in ascending order, m (1 ≤ m ≤ 10^5) representing the number of queries, and m pairs of integers (x_i, y_i) (1 ≤ x_i, y_i ≤ n; x_i ≠ y_i) representing the queries. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. For each city, the closest city is unique.
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
        
    #State: The loop has processed all test cases, and for each query, it has printed the minimum distance between the cities specified in the query. The variables `t`, `n`, `lst`, `m`, `start`, `end`, `inc`, `s`, `d1`, and `d2` are no longer in their initial states but have been used to compute the results for the queries. The final state of these variables is not explicitly defined but is the result of the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, each containing a list of city coordinates and a set of queries. For each query, it calculates and prints the minimum distance between the two specified cities by considering the distances in both forward and backward directions. The function does not return any value but prints the results directly. After processing all test cases, the variables used within the function are no longer in their initial states, but their final states are not explicitly defined.

