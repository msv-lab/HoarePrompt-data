#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 10^5; a is a list of n integers in strictly increasing order such that 0 ≤ a[0] < a[1] < ... < a[n-1] ≤ 10^9; m is an integer such that 1 ≤ m ≤ 10^5; and each query consists of two distinct integers x and y such that 1 ≤ x, y ≤ n.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 10^4; n is an integer such that 2 ≤ n ≤ 10^5; a is a list of n integers in strictly increasing order such that 0 ≤ a[0] < a[1] < ... < a[n-1] ≤ 10^9; m is an integer such that 1 ≤ m ≤ 10^5; After processing all queries, d1 and d2 are dictionaries where d1[i] contains the value computed from the forward pass and d2[i] contains the value computed from the backward pass for each index i in the list a. The loop processes m queries, each consisting of two distinct integers x and y, and prints the difference between the corresponding values in d1 or d2 based on the query direction.
#Overall this is what the function does:The function processes a list `a` of `n` integers in strictly increasing order and handles `m` queries. For each query consisting of two distinct integers `x` and `y`, it computes and prints the difference between the values stored in dictionaries `d1` and `d2`. Dictionary `d1` contains values computed in a forward pass, while `d2` contains values from a backward pass. The function does not return any value but outputs the results of the queries.

