#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, a is a list of n integers where 0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9, m is an integer such that 1 ≤ m ≤ 10^5, and each query consists of two distinct integers x_i and y_i such that 1 ≤ x_i, y_i ≤ n.
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
        
    #State: Output State: The output state consists of the results of `m` queries for each test case. For each query, if `y > x`, the output is the value of `d1[y] - d1[x]`. If `y <= x`, the output is the value of `d2[y] - d2[x]`. The dictionaries `d1` and `d2` are computed based on the differences between consecutive elements in the list `l`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer n, a list of n integers a, an integer m, and m queries consisting of pairs of integers (x, y). It then computes two dictionaries, d1 and d2, based on the differences between consecutive elements in the list a. Finally, it outputs the results of the queries, printing the value of d1[y] - d1[x] if y > x, and d2[y] - d2[x] otherwise.

