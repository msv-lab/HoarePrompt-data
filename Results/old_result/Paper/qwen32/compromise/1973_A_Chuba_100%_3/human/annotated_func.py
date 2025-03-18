#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order. The number of test cases, t, satisfies 1 ≤ t ≤ 500.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: The output state consists of t lines, each corresponding to the result of a test case. For each test case, if the sum of the scores (p_1 + p_2 + p_3) is odd, the output is '-1'. Otherwise, the output is the calculated result given by the formula (p_1 + p_2 + p_3 - max(0, p_3 - p_0 - p_1)) // 2. The variables p_1, p_2, p_3, and t remain unchanged after the loop executes all iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three sorted scores. For each test case, it checks if the sum of the scores is odd. If it is, the function outputs '-1'. Otherwise, it calculates and outputs a specific result based on the formula provided. The input scores and the number of test cases remain unchanged after processing.

