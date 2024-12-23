#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 100000, cakes is a list of tuples where each tuple contains two positive integers representing the radius and height of the i-th cake such that 1 <= r_i, h_i <= 10000.
def func_1(n, cakes):
    volumes = [(math.pi * r * r * h) for r, h in cakes]
    dp = [0] * n
    for i in range(n):
        dp[i] = volumes[i]
        
        for j in range(i):
            if volumes[j] < volumes[i]:
                dp[i] = max(dp[i], dp[j] + volumes[i])
        
    #State of the program after the  for loop has been executed: `i` is `n`, `j` is `0`, `dp` is a list of length `n` where each element `dp[i]` is the maximum value of `volumes[i]` plus the maximum sum of subproblems from indices `0` to `i-2`, `n` remains the same, and `volumes` is a list of volumes calculated as \(\pi \times r_i \times r_i \times h_i\) for each cake \((r_i, h_i)\) in `cakes`.
    return max(dp)
    #The program returns the maximum value in the list dp, which represents the maximum value of volumes[i] plus the maximum sum of subproblems from indices 0 to i-2 for each i from 0 to n-1
#Overall this is what the function does:The function `func_1` accepts two parameters: `n` (a positive integer such that 1 ≤ n ≤ 100000) and `cakes` (a list of tuples where each tuple contains two positive integers representing the radius and height of the i-th cake such that 1 ≤ r_i, h_i ≤ 10000). It calculates the volume of each cake using the formula \( \pi \times r_i \times r_i \times h_i \) and stores these volumes in a list called `volumes`. Then, it uses dynamic programming to compute the maximum value of `volumes[i]` plus the maximum sum of subproblems from indices 0 to i-2 for each i from 0 to n-1. This is stored in a list called `dp`. Finally, it returns the maximum value in the `dp` list, which represents the optimal way to select cakes to maximize the sum of their volumes considering the subproblem constraints.

#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100 000, and cakes is a list of tuples where each tuple contains two positive integers representing the radius and height of the i-th cake respectively, with 1 <= radius_i, height_i <= 10 000.
def func_2():
    data = input().split()
    n = int(data[0])
    cakes = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]
    result = func_1(n, cakes)
    print(f'{result:.6f}')
#Overall this is what the function does:The function `func_2` reads input from the standard input, processes it to extract the number of cakes and their respective radii and heights, and then calls another function `func_1` with these values. It finally prints the result returned by `func_1`, formatted to six decimal places. The input consists of the integer `n` followed by `2n` integers representing the radii and heights of the cakes. If `n` is outside the range 1 to 100,000, the function will still read and process the input, but this case is not handled within the function itself. Additionally, if the radii or heights of the cakes are outside the range 1 to 10,000, no specific handling is provided for such cases.

