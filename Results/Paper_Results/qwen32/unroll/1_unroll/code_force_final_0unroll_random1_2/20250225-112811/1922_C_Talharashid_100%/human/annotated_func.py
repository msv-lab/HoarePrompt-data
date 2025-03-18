#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 2 <= n <= 10^5, a is a list of n distinct integers in ascending order where 0 <= a_1 < a_2 < ... < a_n <= 10^9, m is an integer such that 1 <= m <= 10^5, and for each of the m queries, x_i and y_i are integers such that 1 <= x_i, y_i <= n and x_i != y_i. The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. Additionally, for each city, the closest city is uniquely determined.
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
        
    #State: The program outputs the result of each query directly, which is the difference in cumulative distances based on the direction of the query. The state of `t`, `n`, `l`, `m`, `x`, `y`, `d1`, and `d2` is reset for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of city positions and a series of queries. For each query, it calculates and outputs the cumulative distance difference between two specified cities based on their relative positions in the list.

