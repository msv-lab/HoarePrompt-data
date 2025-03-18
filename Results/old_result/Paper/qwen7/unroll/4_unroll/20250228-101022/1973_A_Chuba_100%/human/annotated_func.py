#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are non-negative integers satisfying 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: Output State: The output state will consist of a series of lines, each containing either '-1' or a non-negative integer. The specific values depend on the inputs provided for each iteration of the loop. Each line corresponds to the result of one iteration, where if the sum of the three integers provided does not yield an odd number when divided by 2, it prints '-1', otherwise, it prints the calculated result.
#Overall this is what the function does:The function reads a positive integer `t` indicating the number of test cases. For each test case, it reads three non-negative integers `p_1`, `p_2`, and `p_3`. It then checks if the sum of these three integers is even. If the sum is odd, it prints `-1`. Otherwise, it calculates a result based on the sum and the difference between the largest and smallest integers, and prints this result. The function outputs a series of lines, each containing either `-1` or a non-negative integer, corresponding to the outcome of each test case.

