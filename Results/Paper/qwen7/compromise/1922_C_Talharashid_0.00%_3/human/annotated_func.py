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
        
    #State: All variables outside the loop remain unchanged, `i` is 0, `start` is 0, `end` is 0, `inc` is -1, `mini` is the minimum distance found during the entire loop execution, `s` is 0, and `m` is greater than or equal to the number of iterations.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer n and a strictly increasing list of n non-negative integers. It also takes an integer m and m pairs of distinct integers x_i and y_i. The function calculates and prints the minimum value between two distances based on the processed data. Specifically, it computes distances for both forward and backward traversals through the list and finds the minimum distance between the given pairs (x_i, y_i) considering the calculated distances.

