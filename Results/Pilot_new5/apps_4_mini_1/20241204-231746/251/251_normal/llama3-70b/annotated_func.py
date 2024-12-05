#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and for each cake, r_i and h_i are positive integers such that 1 ≤ r_i, h_i ≤ 10,000.
def func():
    n = int(input())
    cakes = []
    for _ in range(n):
        r, h = map(int, input().split())
        
        cakes.append((math.pi * r * r * h, r, h))
        
    #State of the program after the  for loop has been executed: `n` is an input integer such that 1 ≤ `n` ≤ 100,000; `cakes` contains `n` tuples of the form `((math.pi * r * r * h), r, h)` for each input pair of `(r, h)`, where `r` is an input integer and `h` is an input integer.
    cakes.sort(reverse=True)
    dp = [0.0] * n
    dp[0] = cakes[0][0]
    for i in range(1, n):
        dp[i] = cakes[i][0]
        
        for j in range(i):
            if cakes[i][1] < cakes[j][1] and cakes[i][2] < cakes[j][2]:
                dp[i] = max(dp[i], dp[j] + cakes[i][0])
        
    #State of the program after the  for loop has been executed: `dp` is an array where `dp[i]` contains the maximum sum of cakes that can be obtained considering the constraints for all `i` from 0 to `n-1`, `cakes` is a list of cake attributes, `n` is the input integer such that 1 ≤ `n` ≤ 100,000. If no valid pairs exist for a particular `i`, then `dp[i]` retains the value of `cakes[i][0]` (the volume of the cake). If `n` is 1, then `dp[0]` is equal to `cakes[0][0]`, and the loop does not execute.
    print(dp[-1])
#Overall this is what the function does:The function accepts no parameters and reads an integer `n` followed by `n` pairs of integers representing the radius `r` and height `h` of cakes. It calculates and stores the volumes of the cakes, sorts them by volume in descending order, and then determines the maximum sum of volumes of cakes that can be stacked on top of each other based on the constraint that a cake can only be placed on another if both its radius and height are smaller. Finally, it prints the maximum achievable sum of volumes from the last computed value in the dynamic programming table.

