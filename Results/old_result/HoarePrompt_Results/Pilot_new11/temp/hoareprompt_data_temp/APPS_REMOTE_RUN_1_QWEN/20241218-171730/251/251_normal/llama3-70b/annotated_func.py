#State of the program right berfore the function call: The input is a list of tuples, where each tuple contains two positive integers representing the radius and height of a simple cake. The length of the list is n (1 ≤ n ≤ 100 000), and for each tuple (r_i, h_i), 1 ≤ r_i, h_i ≤ 10 000.
def func():
    n = int(input())
    cakes = []
    for _ in range(n):
        r, h = map(int, input().split())
        
        cakes.append((math.pi * r * r * h, r, h))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `cakes` is a list of tuples where each tuple contains three elements: the volume of a cake (`math.pi * r * r * h`), the radius `r`, and the height `h` of the cake, where both `r` and `h` are integers obtained from user input.
    cakes.sort(reverse=True)
    dp = [0.0] * n
    dp[0] = cakes[0][0]
    for i in range(1, n):
        dp[i] = cakes[i][0]
        
        for j in range(i):
            if cakes[i][1] < cakes[j][1] and cakes[i][2] < cakes[j][2]:
                dp[i] = max(dp[i], dp[j] + cakes[i][0])
        
    #State of the program after the  for loop has been executed: `dp` is an array of length `n` where `dp[i]` (for `i` from `0` to `n-1`) contains the maximum volume that can be achieved by selecting a subset of cakes such that no cake in the subset has both dimensions less than those of any other cake in the subset, up to the `i-th` cake, `n` is a non-negative integer, and `cakes` is a list of cakes with each element containing three values representing the dimensions and volume of a cake.
    print(dp[-1])
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains two positive integers representing the radius and height of a simple cake. It calculates the volume of each cake using the formula \( \pi r^2 h \), sorts the cakes in descending order based on their volume, and then uses dynamic programming to find the maximum volume that can be achieved by selecting a subset of cakes such that no cake in the subset has both dimensions (radius and height) less than those of any other cake in the subset. The function prints the maximum volume that can be achieved.

