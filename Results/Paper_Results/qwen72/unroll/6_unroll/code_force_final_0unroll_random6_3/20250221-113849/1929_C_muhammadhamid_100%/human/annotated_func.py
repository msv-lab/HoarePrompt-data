#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, k, x, and a are integers where 2 <= k <= 30, 1 <= x <= 100, and 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: The value of `t` is unchanged, and for each test case, `k`, `x`, and `a` are unchanged. The variable `s` is updated to the final value calculated by the loop, and the output for each test case is 'Yes' if `a` is greater than or equal to the final value of `s`, otherwise 'No'.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads three integers `k`, `x`, and `a` from the input. It then calculates a value `s` starting from 1 and updates it in a loop that runs `x` times. The loop increments `s` by `s // (k - 1) + 1` in each iteration. After the loop, the function prints 'Yes' if `a` is greater than or equal to the final value of `s`, otherwise it prints 'No'. The function does not return any value. After the function concludes, the input variables `t`, `k`, `x`, and `a` remain unchanged, and the output for each test case is either 'Yes' or 'No' based on the comparison.

