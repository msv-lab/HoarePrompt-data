#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, a is a list of n integers in strictly increasing order (0 ≤ a_1 < a_2 < ... < a_n ≤ 10^9), m is an integer such that 1 ≤ m ≤ 10^5, and x_i and y_i are integers such that 1 ≤ x_i, y_i ≤ n and x_i ≠ y_i.
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
        
    #State: Output State: The loop has completed all its iterations. For each of the `m` queries, the correct difference based on the values of `d1` and `d2` has been printed. The values of `n`, `l`, `d1`, and `d2` remain unchanged from their final state after the last iteration. The variable `m` remains as the last input value provided, and `j` is equal to `m-1`. The variables `x` and `y` are the last pair of integers inputted by the user during the loop's final iteration, and they have been used to compute the final output.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \( t \), an integer \( n \), a strictly increasing list \( a \) of \( n \) integers, an integer \( m \), and \( m \) pairs of integers \( (x_i, y_i) \). For each test case, it calculates and prints the difference based on two dictionaries \( d1 \) and \( d2 \), which are constructed from the list \( a \). Specifically, for each query \( (x_i, y_i) \), it computes and outputs the difference according to the values in \( d1 \) and \( d2 \). After processing all test cases, the function does not return any value but prints the results for each query.

