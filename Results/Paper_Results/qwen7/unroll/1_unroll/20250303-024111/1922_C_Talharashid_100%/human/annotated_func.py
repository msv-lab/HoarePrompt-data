#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and a is a list of n non-negative integers in strictly increasing order (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9). m is an integer such that 1 ≤ m ≤ 10^5, and for each query, x_i and y_i are distinct integers such that 1 ≤ x_i, y_i ≤ n.
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
        
    #State: Output State: The output state consists of the values of `d1` and `d2` dictionaries computed for each test case, followed by the results of `m` queries for each test case. For each query, the output is the difference between the values of `d1` or `d2` at indices `y` and `x`, depending on whether `y` is greater than `x`.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \), a strictly increasing list of \( n \) non-negative integers \( a \), and an integer \( m \). It then computes two dictionaries, \( d1 \) and \( d2 \), based on the differences between consecutive elements in the list \( a \). Finally, for each of the \( m \) queries, it outputs the difference between the values of \( d1 \) or \( d2 \) at specified indices \( x \) and \( y \), depending on which index is larger.

