#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4; for each test case, n is an integer where 2 ≤ n ≤ 10^5, a is a list of n integers where 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9, m is an integer where 1 ≤ m ≤ 10^5, and for each of the m queries, x_i and y_i are integers where 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i. Additionally, the sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5.
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
        
    #State: The loop has completed all iterations, and the variables `t`, `n`, `a`, and `m` remain unchanged. The dictionaries `d1` and `d2` are populated with the cumulative minimum differences for each index when traversing the list `lst` from the start to the end and from the end to the start, respectively. For each of the `m` queries, the minimum of the two possible cumulative differences (one from `d1` and one from `d2`) is printed.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of a list of strictly increasing integers and a set of queries. For each query, it calculates and prints the minimum cumulative difference between the specified indices, considering both forward and backward traversals of the list. The function reads the number of test cases, the list of integers, and the queries from standard input. After processing all queries for all test cases, the function terminates with the input variables `t`, `n`, `a`, and `m` unchanged, and the dictionaries `d1` and `d2` populated with the cumulative differences for each index.

