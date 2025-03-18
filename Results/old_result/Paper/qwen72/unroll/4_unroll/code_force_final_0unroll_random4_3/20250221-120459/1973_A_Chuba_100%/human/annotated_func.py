#State of the program right berfore the function call: The function should take three integers p_1, p_2, and p_3 as input, where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, and return the maximum number of draws that could have happened or -1 if the scores are not consistent with any valid set of games.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: Output State: The function will have printed the maximum number of draws for each set of inputs or -1 if the scores are not consistent with any valid set of games, and the loop will have completed all `t` iterations. The variables `p_1`, `p_2`, `p_3`, and `t` will remain unchanged.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `p_1`, `p_2`, and `p_3` (where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30) from the input. It then calculates and prints the maximum number of draws that could have happened based on these scores, or -1 if the scores are not consistent with any valid set of games. After processing all `t` test cases, the function concludes, and the variables `p_1`, `p_2`, `p_3`, and `t` remain unchanged.

