#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, a is a list of n distinct integers in strictly ascending order where 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9, m is an integer such that 1 ≤ m ≤ 10^5, and for each query, x and y are integers such that 1 ≤ x, y ≤ n and x ≠ y. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. Additionally, for each city, the closest city is uniquely determined.
def func():
    for i in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        d1 = defaultdict(int)
        
        d2 = defaultdict(int)
        
        d1[2] = 1
        
        for i in range(1, n - 1):
            if l[i + 1] - l[i] < l[i] - l[i - 1]:
                d1[i + 2] = 1 + d1[i + 1]
            else:
                d1[i + 2] = l[i + 1] - l[i] + d1[i + 1]
        
        d2[n - 1] = 1
        
        for i in range(n - 2, 0, -1):
            if l[i] - l[i - 1] < l[i + 1] - l[i]:
                d2[i] = 1 + d2[i + 1]
            else:
                d2[i] = l[i] - l[i - 1] + d2[i + 1]
        
        m = int(input())
        
        for j in range(m):
            x, y = map(int, input().split())
            if y > x:
                print(d1[y] - d1[x])
            else:
                print(d2[y] - d2[x])
        
    #State: The loop has completed all `t` iterations, where `t` is the total number of test cases. For each test case, the loop has processed `m` queries, and for each query, it has printed the correct distance between the cities `x` and `y` based on the precomputed dictionaries `d1` and `d2`. The variables `i`, `n`, `l`, `d1`, `d2`, `m`, `j`, `x`, and `y` do not retain their values from one test case to another; they are reinitialized for each new test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of city positions and a series of queries. For each query, it calculates and prints the cumulative distance from one city to another based on precomputed shortest paths in both forward and backward directions.

