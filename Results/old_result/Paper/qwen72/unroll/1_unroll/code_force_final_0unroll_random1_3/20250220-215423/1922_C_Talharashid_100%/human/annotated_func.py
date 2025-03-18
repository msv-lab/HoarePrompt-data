#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each test case contains n (2 ≤ n ≤ 10^5) and a list of n integers a_1, a_2, ..., a_n (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9) in ascending order, m (1 ≤ m ≤ 10^5) queries, and each query consists of two integers x_i and y_i (1 ≤ x_i, y_i ≤ n; x_i ≠ y_i). The sum of n over all test cases does not exceed 10^5, and the sum of m over all test cases does not exceed 10^5. For every city, the closest city is determined uniquely.
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
        
    #State: The output state is the same as the initial state, except that the loop has been executed for each test case, and the results of the queries have been printed. The variables `d1` and `d2` will have been populated with the calculated distances for each city, but these are not part of the initial state and are not required to be described in the output state. The values of `t`, `n`, `l`, and `m` will have been processed, and the input for the next test case will be ready to be read.
#Overall this is what the function does:The function processes multiple test cases, each containing a list of city positions in ascending order and a series of queries. For each query, it calculates and prints the difference in the cumulative distances to the closest city for the specified cities. The function does not return any values; it only prints the results of the queries. After processing all test cases, the function concludes, and the program state is reset to read the next set of inputs.

