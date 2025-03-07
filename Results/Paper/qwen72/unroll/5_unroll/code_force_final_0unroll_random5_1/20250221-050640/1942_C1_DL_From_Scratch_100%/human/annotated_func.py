#State of the program right berfore the function call: The function should be called with a specific problem context, including the number of test cases t, the number of sides of the polygon n, the number of vertices Bessie has chosen x, the maximum number of other vertices you can choose y (where y = 0), and a list of x distinct integers representing the vertices Bessie has chosen. The values must satisfy 1 ≤ t ≤ 10^4, 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2 · 10^5), and y = 0. The sum of x over all test cases should not exceed 2 · 10^5.
def func():
    T = int(input())
    for _ in range(T):
        n, x, y = map(int, input().split())
        
        list0 = list(map(int, input().split()))
        
        list0 = sorted(list0)
        
        count = 0
        
        for i in range(x - 1):
            num = list0[i + 1] - list0[i] - 1
            if num == 1:
                count += 1
        
        num = list0[0] + n - list0[-1] - 1
        
        if num == 1:
            count += 1
        
        print(count + x - 2)
        
    #State: For each test case, the loop will output the number of gaps of size 1 between the chosen vertices, plus the number of chosen vertices minus 2. The variables `T`, `n`, `x`, `y`, and `list0` will be updated for each test case, but their values will be determined by the input for each iteration. The final values of these variables will be the ones from the last test case.
#Overall this is what the function does:The function reads multiple test cases from the input, where each test case includes the number of sides of a polygon `n`, the number of vertices Bessie has chosen `x`, and a list of `x` distinct integers representing the chosen vertices. For each test case, it calculates and prints the number of gaps of size 1 between the chosen vertices, plus the number of chosen vertices minus 2. The function does not return any value; it only outputs the result for each test case. After the function concludes, the variables `T`, `n`, `x`, `y`, and `list0` will hold the values from the last test case processed.

