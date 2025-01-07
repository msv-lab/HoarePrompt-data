#State of the program right berfore the function call: n is a positive integer representing the number of cakes, and cakes is a list of tuples where each tuple contains two positive integers representing the radius and height of a cake.
def func_1(n, cakes):
    volumes = [(math.pi * r * r * h) for r, h in cakes]
    dp = [0] * n
    for i in range(n):
        dp[i] = volumes[i]
        
        for j in range(i):
            if volumes[j] < volumes[i]:
                dp[i] = max(dp[i], dp[j] + volumes[i])
        
    #State of the program after the  for loop has been executed: `dp` is a list where each element `dp[i]` contains the maximum sum of volumes formed by considering the volumes of cakes up to index `i`, `n` is a positive integer, `volumes` is a list of volumes, and if the loop does not execute, then `dp` is a list initialized to `[volumes[0], 0, 0, ..., 0]` if `n` is at least 1.
    return max(dp)
    #The program returns the maximum sum of volumes formed by considering the volumes of cakes up to index `i`, which is represented by the maximum value in the list `dp`.
#Overall this is what the function does:The function accepts a positive integer `n` and a list of tuples `cakes` where each tuple contains the radius and height of a cake. It calculates the volume of each cake and returns the maximum sum of volumes that can be formed by stacking cakes with strictly increasing volumes. If no cakes are provided or if `n` is 0, the function will return 0, since the maximum volume sum would be zero in that case.

#State of the program right berfore the function call: n is a positive integer representing the number of cakes (1 ≤ n ≤ 100,000), and cakes is a list of tuples where each tuple contains two integers representing the radius and height of each cake (1 ≤ r_i, h_i ≤ 10,000).
def func_2():
    data = input().split()
    n = int(data[0])
    cakes = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]
    result = func_1(n, cakes)
    print(f'{result:.6f}')
#Overall this is what the function does:The function accepts a positive integer `n`, representing the number of cakes, and a list of tuples `cakes`, each containing the radius and height of a cake. It calculates some result via `func_1` using `n` and `cakes`, then prints this result formatted to six decimal places. However, it does not handle any potential input errors such as invalid data types or values outside the specified ranges.

