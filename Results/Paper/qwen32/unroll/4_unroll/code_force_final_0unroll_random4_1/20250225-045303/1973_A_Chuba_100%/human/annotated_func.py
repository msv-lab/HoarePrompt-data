#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order. The first line of the input contains an integer t (1 ≤ t ≤ 500) denoting the number of test cases.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: The output state consists of `t` lines, each containing either `-1` if the sum of the scores for that test case is odd, or the calculated result if the sum is even.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three sorted scores. For each test case, it checks if the sum of the scores is odd. If it is, the function outputs `-1`. If the sum is even, it calculates and outputs a specific result based on the scores.

