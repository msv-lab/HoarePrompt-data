#State of the program right berfore the function call: The function should take three integers p_1, p_2, and p_3 as input such that 0 <= p_1 <= p_2 <= p_3 <= 30, representing the scores of the three players after all the games.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: The values of `p_1`, `p_2`, and `p_3` remain unchanged. The loop prints a series of results or `-1` for each iteration based on the input values `v` provided during each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `v[0]`, `v[1]`, and `v[2]` from the input, representing the scores of three players. If the sum of these scores is odd, it prints `-1`. Otherwise, it calculates a result based on the scores and prints this result. The function does not modify the input scores and performs these operations for each of the `t` test cases.

