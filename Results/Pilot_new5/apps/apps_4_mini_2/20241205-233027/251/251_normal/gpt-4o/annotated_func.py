#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 100,000), and cakes is a list of tuples where each tuple contains two integers (r_i, h_i) representing the radius and height of the i-th cake, with each r_i and h_i satisfying (1 ≤ r_i, h_i ≤ 10,000).
def func_1(n, cakes):
    volumes = [(math.pi * r * r * h) for r, h in cakes]
    dp = [0] * n
    for i in range(n):
        dp[i] = volumes[i]
        
        for j in range(i):
            if volumes[j] < volumes[i]:
                dp[i] = max(dp[i], dp[j] + volumes[i])
        
    #State of the program after the  for loop has been executed: `n` is a positive integer (1 ≤ n ≤ 100,000); `dp` is a list where each `dp[i]` is the maximum volume sum of cakes whose volumes are less than `volumes[i]` for `i` in range `n`, where `dp[i]` equals the volume of the cake at index `i` if no other volumes are less than it.
    return max(dp)
    #The program returns the maximum value from the list `dp`, which represents the maximum volume sum of cakes whose volumes are less than each corresponding volume in the `volumes` list.
#Overall this is what the function does:The function accepts a positive integer `n` and a list of tuples `cakes`, where each tuple contains the radius and height of a cake. It calculates the volume of each cake and then finds the maximum volume sum of cakes that can be stacked such that each cake below has a smaller volume than the one above it. The function returns the maximum volume sum achievable under these conditions.

#State of the program right berfore the function call: n is a positive integer representing the number of cakes, and cakes is a list of tuples where each tuple contains two integers (r_i and h_i) representing the radius and height of the i-th cake, respectively, with 1 ≤ r_i, h_i ≤ 10,000.
def func_2():
    data = input().split()
    n = int(data[0])
    cakes = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]
    result = func_1(n, cakes)
    print(f'{result:.6f}')
#Overall this is what the function does:The function accepts a positive integer `n` representing the number of cakes and a list of tuples `cakes`, where each tuple contains two integers representing the radius and height of each cake. It calls another function with these parameters and prints the result formatted to six decimal places, but does not handle potential input errors or validate input format.

