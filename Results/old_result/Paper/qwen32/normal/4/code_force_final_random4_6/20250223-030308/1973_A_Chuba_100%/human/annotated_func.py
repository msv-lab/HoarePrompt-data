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
        
    #State: a series of `t` printed values, each being either `-1` or the calculated `result` based on the input values for each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integer scores in non-decreasing order. For each test case, it prints either `-1` if the sum of the scores is odd, or a calculated value representing half the sum of the scores minus the maximum of zero or the difference between the highest score and the sum of the other two scores.

