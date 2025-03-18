#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100000); for each cake, r_i and h_i are integers representing the radius and height of the i-th cake, respectively, with 1 ≤ r_i, h_i ≤ 10000.
def func():
    n = int(input())
    cakes = []
    for _ in range(n):
        r, h = map(int, input().split())
        
        cakes.append((math.pi * r * r * h, r, h))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100000), `cakes` is a list containing `n` tuples where each tuple is of the form `(volume, r_i, h_i)` with `volume` calculated as `math.pi * r_i * r_i * h_i` for each cake corresponding to the input values of `r_i` and `h_i`, and `_` takes values from 0 to n-1 during iterations.
    cakes.sort(reverse=True)
    dp = [0.0] * n
    dp[0] = cakes[0][0]
    for i in range(1, n):
        dp[i] = cakes[i][0]
        
        for j in range(i):
            if cakes[i][1] < cakes[j][1] and cakes[i][2] < cakes[j][2]:
                dp[i] = max(dp[i], dp[j] + cakes[i][0])
        
    #State of the program after the  for loop has been executed: `dp` is a list containing the maximum possible values calculated based on the conditions of the loop for each corresponding cake index, where `dp[i]` represents the maximum value obtainable using the cakes that satisfy the given conditions, `cakes` is a list of `n` tuples sorted in descending order by volume, and if no valid preceding cakes are found for a particular `i`, `dp[i]` retains its initial value `cakes[i][0]`. If `n` is 1, then `dp` will simply contain the value of `cakes[0][0]`.
    print(dp[-1])
#Overall this is what the function does:The function reads a positive integer `n`, then accepts `n` pairs of integers representing the radius and height of cakes. It calculates the volume for each cake and stores the volumes along with their dimensions in a list. The function then determines the maximum possible volume obtainable by stacking cakes, where a cake can only be placed on top of another if both its radius and height are smaller than those of the cake below it. Finally, it prints the maximum achievable volume using these rules. No values are returned from the function.

