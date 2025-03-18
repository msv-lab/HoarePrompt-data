#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; n and k are integers such that 1 ≤ n ≤ 3⋅10^5 and 0 ≤ k ≤ n; for each test case, r_i and c_i are integers such that 1 ≤ r_i, c_i ≤ n and the moves you made are valid according to the problem description.
def func():
    t = int(input())
    while t:
        t -= 1
        
        n, k = list(map(int, input().split(' ')))
        
        num = 0
        
        for i in range(k):
            c, r = list(map(int, input().split(' ')))
            if c == r:
                num += 1
            else:
                num += 2
        
        m = n - num
        
        if m == 0:
            print(0)
        elif m == 1:
            print(1)
        else:
            dp = [(0) for i in range(m + 1)]
            dp[1] = 1
            dp[2] = 3
            for i in range(3, m + 1):
                dp[i] = (dp[i - 1] + (i - 1) * dp[i - 2] * 2) % (10 ** 9 + 7)
            print(dp[m])
        
    #State: Output State: The output state will depend on the inputs provided within each iteration of the loop. Specifically, it will be determined by the values of `n`, `k`, and the subsequent inputs for `c` and `r`. The final output will be one of the following based on the value of `m = n - num`:
    #
    #- If `m == 0`, it will print `0`.
    #- If `m == 1`, it will print `1`.
    #- Otherwise, it will compute a dynamic programming solution to find the number of ways to achieve `m` using a specific formula and print the result modulo \(10^9 + 7\).
    #
    #The exact output cannot be determined without knowing the specific inputs for each iteration, but the process described above will be followed for each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (number of test cases), an integer n (size of the grid), an integer k (number of moves), and k pairs of integers (r, c) representing row and column moves. For each test case, it calculates the number of ways to achieve a specific configuration on a grid of size n x n, based on the given moves. If the number of ways is zero, it prints 0; if one, it prints 1; otherwise, it computes the result using dynamic programming and prints it modulo \(10^9 + 7\).

