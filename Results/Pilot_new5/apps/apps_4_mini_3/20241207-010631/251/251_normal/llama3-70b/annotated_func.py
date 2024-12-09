#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100,000), and for each cake i (1 ≤ i ≤ n), r_i and h_i are integers such that (1 ≤ r_i, h_i ≤ 10,000).
def func():
    n = int(input())
    cakes = []
    for _ in range(n):
        r, h = map(int, input().split())
        
        cakes.append((math.pi * r * r * h, r, h))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100,000), `cakes` is a list containing `n` tuples, each tuple being of the form `(volume, r, h)` where `volume` is calculated as `math.pi * r * r * h` for each `r` and `h` input received during the loop iterations.
    cakes.sort(reverse=True)
    dp = [0.0] * n
    dp[0] = cakes[0][0]
    for i in range(1, n):
        dp[i] = cakes[i][0]
        
        for j in range(i):
            if cakes[i][1] < cakes[j][1] and cakes[i][2] < cakes[j][2]:
                dp[i] = max(dp[i], dp[j] + cakes[i][0])
        
    #State of the program after the  for loop has been executed: `dp` contains the maximum sum of cake values for each cake based on the dimension conditions, with `dp[0]` equal to `cakes[0][0]`, and `n` is the number of cakes in the list.
    print(dp[-1])
#Overall this is what the function does:The function processes a collection of cakes defined by their radius and height, computes the volume for each cake, and determines the maximum sum of volumes that can be obtained by stacking cakes such that each cake in the stack must have both a smaller radius and height than the cake below it. The function does not accept any parameters and outputs the maximum sum of the cake volumes based on the stacking conditions.

