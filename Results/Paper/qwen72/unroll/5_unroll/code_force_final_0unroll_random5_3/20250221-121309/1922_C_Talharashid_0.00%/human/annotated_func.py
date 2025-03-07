#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of n (2 ≤ n ≤ 10^5) cities with coordinates a_1, a_2, ..., a_n (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9) in ascending order, and m (1 ≤ m ≤ 10^5) queries. Each query is a pair of integers x_i, y_i (1 ≤ x_i, y_i ≤ n; x_i ≠ y_i), representing the cities between which the minimum travel cost needs to be calculated. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. For each city, the closest city is unique.
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
        
    #State: The loop has processed all test cases, and for each query, it has printed the minimum travel cost between the cities x_i and y_i. The variables `t`, `n`, `lst`, `m`, `start`, `end`, `inc`, `s`, `d1`, and `d2` have been updated and used within the loop, but their final values are not retained for the next test case. The loop ends after processing all queries for all test cases, and the program is ready to terminate or accept new input.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the number of cities and their coordinates, then calculates the minimum travel cost for a series of queries. Each query specifies two cities, and the function prints the minimum travel cost between these cities. The function does not return any value; it only prints the results of the queries. After processing all test cases, the function terminates, and the state of the program is such that all input has been processed and the corresponding minimum travel costs have been printed for each query.

