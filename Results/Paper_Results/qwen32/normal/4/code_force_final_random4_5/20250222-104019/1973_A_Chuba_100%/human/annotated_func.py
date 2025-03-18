#State of the program right berfore the function call: Each test case contains three integers p_1, p_2, and p_3 (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) representing the scores of the three players, sorted in non-decreasing order. The number of test cases t satisfies 1 ≤ t ≤ 500.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: The loop will print the result for each of the `t` test cases, which is either `-1` if the sum of the scores is odd, or `(v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2` if the sum is even.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three sorted integers representing the scores of three players. For each test case, it checks if the sum of the scores is odd. If it is, the function outputs `-1`. If the sum is even, it calculates and outputs a specific result based on the scores.

