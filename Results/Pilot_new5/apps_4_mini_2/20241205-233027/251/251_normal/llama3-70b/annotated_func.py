#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100,000, and each cake is described by two integers r_i and h_i (1 ≤ r_i, h_i ≤ 10,000) representing the radius and height of the i-th cake.
def func():
    n = int(input())
    cakes = []
    for _ in range(n):
        r, h = map(int, input().split())
        
        cakes.append((math.pi * r * r * h, r, h))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 100,000; `cakes` is a list containing `n` entries, each represented as (volume, radius, height) where volume = (math.pi * `r_i` * `r_i` * `h_i`) for each input pair (`r_i`, `h_i`).
    cakes.sort(reverse=True)
    dp = [0.0] * n
    dp[0] = cakes[0][0]
    for i in range(1, n):
        dp[i] = cakes[i][0]
        
        for j in range(i):
            if cakes[i][1] < cakes[j][1] and cakes[i][2] < cakes[j][2]:
                dp[i] = max(dp[i], dp[j] + cakes[i][0])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 100,000; `dp[i]` is the maximum sum of the volumes of cakes that can be stacked, where each cake `i` meets the conditions of being smaller in both radius and height compared to previously considered cakes; `dp[0]` is equal to `cakes[0][0]`, and `dp[1]` through `dp[n-1]` are computed based on the conditions applied to all previous cakes in the `cakes` list.
    print(dp[-1])
#Overall this is what the function does:The function accepts a positive integer `n` representing the number of cakes, followed by `n` pairs of integers representing the radius and height of each cake. It calculates the volume of each cake, sorts the cakes in descending order by volume, and then computes the maximum sum of volumes of cakes that can be stacked based on the condition that a cake can only be stacked on top of another if it is smaller in both radius and height. Finally, it prints the maximum sum of volumes of the stackable cakes.

