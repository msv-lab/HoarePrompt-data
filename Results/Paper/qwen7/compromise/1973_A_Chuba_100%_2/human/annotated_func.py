#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are integers satisfying 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: Output State: The output state will consist of a series of integers printed based on the input provided for each iteration of the loop. For each input triplet (v[0], v[1], v[2]), if the sum of the triplet is odd, "-1" will be printed; otherwise, the result calculated as \((v[0] + v[1] + v[2] - \max(0, v[2] - v[0] - v[1])) // 2\) will be printed. This process will repeat for `t` iterations, where `t` is the initial value of the input integer.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \(p_1\), \(p_2\), and \(p_3\). For each test case, it checks if the sum of the three integers is odd. If the sum is odd, it prints \(-1\). If the sum is even, it calculates a specific value based on the integers and prints it. The function reads the number of test cases from the input, processes each test case according to the described logic, and outputs the results for each test case.

