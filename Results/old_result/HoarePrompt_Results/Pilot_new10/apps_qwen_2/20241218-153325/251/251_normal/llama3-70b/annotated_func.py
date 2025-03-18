#State of the program right berfore the function call: The input is a list of tuples, where each tuple contains two positive integers representing the radius and height of a cake, and the length of this list is a positive integer n such that 1 <= n <= 100 000.
def func():
    n = int(input())
    cakes = []
    for _ in range(n):
        r, h = map(int, input().split())
        
        cakes.append((math.pi * r * r * h, r, h))
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `cakes` is a list of `n` tuples, each tuple contains three elements where the first element is \(\pi \cdot r^2 \cdot h\), the second element is `r`, and the third element is `h`, where `r` and `h` are positive integers.
    cakes.sort(reverse=True)
    dp = [0.0] * n
    dp[0] = cakes[0][0]
    for i in range(1, n):
        dp[i] = cakes[i][0]
        
        for j in range(i):
            if cakes[i][1] < cakes[j][1] and cakes[i][2] < cakes[j][2]:
                dp[i] = max(dp[i], dp[j] + cakes[i][0])
        
    #State of the program after the  for loop has been executed: `i` is `n`, `n` is a positive integer, `dp` is a list of length `n` where `dp[i]` for each `i` from 0 to `n-1` is the maximum volume of a subset of cakes that can be selected such that no selected cake has both radius and height greater than or equal to another previously selected cake, `cakes` is a list of `n` tuples, each tuple contains the volume of the cake, the radius, and the height in descending order of volume.
    print(dp[-1])
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains two positive integers representing the radius and height of a cake. It calculates the maximum volume of a subset of cakes that can be selected such that no selected cake has both a radius and height greater than or equal to another previously selected cake. The function sorts the cakes by their volumes in descending order and then uses dynamic programming to determine the maximum volume. The final output is the maximum volume of the selected subset of cakes.

