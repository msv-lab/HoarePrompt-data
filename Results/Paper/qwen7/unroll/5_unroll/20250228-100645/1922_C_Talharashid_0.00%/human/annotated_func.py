#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and a is a list of n integers in strictly increasing order (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9). m is an integer such that 1 ≤ m ≤ 10^5, and for each query, x_i and y_i are integers such that 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4. For each input value of t, there are two dictionaries d1 and d2 which store intermediate results of the calculations. There is a list lst which contains integers based on user input. Variable s is used to accumulate values during the calculation process. After processing all inputs, there are m queries where start and end indices are provided, and for each query, the minimum value between the absolute differences calculated from d1 and d2 is printed.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads a list of integers `lst` and calculates two dictionaries `d1` and `d2` that store intermediate results. It then handles `m` queries, each providing two indices `start` and `end`. For each query, it computes the minimum value between the absolute differences obtained from `d1` and `d2` and prints the result.

