#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are non-negative integers such that 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: After all iterations of the loop have finished, `t` will be 0, and there will be no further inputs or computations on `v`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of three non-negative integers \(p_1\), \(p_2\), and \(p_3\) where \(0 \leq p_1 \leq p_2 \leq p_3 \leq 30\). For each test case, it checks if the sum of these integers is odd. If the sum is even, it calculates a specific value based on these integers and prints it; otherwise, it prints -1. After processing all test cases, the function ends with no further operations on the input data.

