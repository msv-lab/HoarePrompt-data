#State of the program right berfore the function call: The function should accept three integers p_1, p_2, and p_3 as input, where 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30, representing the scores of the three players sorted in non-decreasing order.
def func():
    t = int(input())
    for _ in range(t):
        v = list(map(int, input().split()))
        
        if (v[0] + v[1] + v[2]) % 2 == 1:
            print('-1')
        else:
            result = (v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2
            print(result)
        
    #State: `p_1`, `p_2`, and `p_3` are integers where 0 ≤ `p_1` ≤ `p_2` ≤ `p_3` ≤ 30, `t` is 0, and `v` is a list of integers input by the user. If the sum of the first three elements of `v` is odd, no changes are made to `v`. If the sum is even, `result` is calculated as `(v[0] + v[1] + v[2] - max(0, v[2] - v[0] - v[1])) // 2` for each iteration.
#Overall this is what the function does:The function reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads three integers from the user, representing the scores of three players in non-decreasing order (0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30). If the sum of these scores is odd, it prints `-1`. If the sum is even, it calculates a result based on the scores and prints it. The function does not return any value. After the function concludes, `t` is 0, and the scores for each test case have been processed and printed.

