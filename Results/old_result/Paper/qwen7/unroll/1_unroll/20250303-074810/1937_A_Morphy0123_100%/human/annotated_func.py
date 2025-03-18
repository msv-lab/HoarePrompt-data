#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            power = 1
            n = log2(n)
            while power < n:
                power += 1
            if power == n:
                print(2 ** power)
            else:
                power -= 1
                print(2 ** power)
        
    #State: Output State: The value of `t` remains unchanged, and for each `i` from `0` to `n_cases-1`, the output consists of either `1`, `2 ** power` where `power` is an integer, or no output if the input `n` was not `1`. Each `n` is processed independently based on its value, and the results are printed during the execution of the loop.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of an integer `n`. It calculates and prints the smallest power of 2 that is greater than or equal to `n`, unless `n` is 1, in which case it simply prints 1. After processing all test cases, the function does not return any value but prints the results directly.

