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
        
    #State: t is 0, and for each iteration i (where 0 ≤ i < t), `v[i]` is a list of integers entered by the user, and `result[i]` is calculated as `(v[i][0] + v[i][1] + v[i][2] - max(0, v[i][2] - v[i][0] - v[i][1])) // 2` if the sum of the first three elements of `v[i]` is even. If the sum is odd, `-1` is printed instead.
#Overall this is what the function does:The function reads a positive integer `t` and then processes `t` test cases. For each test case, it takes three integers `p_1`, `p_2`, and `p_3` as input. It calculates a result based on the sum of these three integers. If the sum is odd, it prints `-1`. If the sum is even, it calculates the result as `(p_1 + p_2 + p_3 - max(0, p_3 - p_1 - p_2)) // 2` and prints this value. After processing all test cases, the function ends.

