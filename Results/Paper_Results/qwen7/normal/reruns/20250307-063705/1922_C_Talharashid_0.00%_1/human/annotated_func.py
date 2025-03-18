#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 10^5; a is a list of n integers in strictly increasing order such that 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9; m is an integer such that 1 ≤ m ≤ 10^5; each query consists of two distinct integers x_i and y_i such that 1 ≤ x_i, y_i ≤ n.
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
        
    #State: After the loop executes all the iterations, `t` will be 0, `m` will be 0, `start` will be `start - t * 2`, `end` will be `end - t * 1`, `s` will be 0, `s1` will be the absolute difference between either `d1[end]` and `d1[start]` or `d2[end]` and `d2[start]` depending on whether `start - t * 2 < end` or `start - t * 2 >= end`, and `s2` will be the absolute difference between either `d2[start]` and `d2[end]` or `d1[start]` and `d1[end]` depending on whether `start - t * 2 < end` or `start - t * 2 >= end`.
#Overall this is what the function does:The function processes a series of queries on a given list of integers. It first calculates the number of adjacent pairs with a specific difference for the entire list and for its reverse. Then, for each query, it determines the minimum count of such pairs between two specified indices. The function outputs the result for each query.

