#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each test case contains n (2 ≤ n ≤ 10^5) and a list a of n integers (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9) in ascending order, m (1 ≤ m ≤ 10^5) queries, and each query consists of two integers x_i and y_i (1 ≤ x_i, y_i ≤ n; x_i ≠ y_i). The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. For each city, the closest city is unique.
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
        
    #State: The loop has processed all test cases, and for each query, it has printed the minimum distance between the cities represented by the indices x_i and y_i. The variables t, n, lst, m, d1, d2, start, end, inc, and s have been updated and used during the execution of the loop, but their final values are not relevant to the output state. The initial state of the input variables (t, n, lst, m, x_i, y_i) remains unchanged as they are read from input for each test case.
#Overall this is what the function does:The function processes multiple test cases. Each test case involves reading an integer `n` and a list `a` of `n` integers in ascending order, representing the positions of cities. It then reads an integer `m` and a list of `m` queries, where each query is a pair of integers `(x_i, y_i)` representing two different cities. For each query, the function calculates and prints the minimum distance between the two cities, considering the distances in both directions (forward and backward) along the list of cities. The function does not return any value; it only prints the results of the queries. The initial state of the input variables (t, n, lst, m, x_i, y_i) remains unchanged as they are read from input for each test case.

