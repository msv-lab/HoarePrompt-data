#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: Output State: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9. After the loop executes all the iterations, the value of `a` may change based on the final value of `s` calculated in each iteration, but the values of `t`, `k`, and `x` remain unchanged. The variable `s` is reset to 1 at the start of each iteration of the loop, and its final value determines whether 'Yes' or 'No' is printed for that iteration.
#Overall this is what the function does:The function processes up to 1000 inputs, each consisting of integers k, x, and a. For each input, it calculates a value s starting from 1 and iteratively updates it based on the formula s += s // (k - 1) + 1 for x times. It then prints 'Yes' if a is greater than or equal to the final value of s, otherwise it prints 'No'. The function does not return any value but prints 'Yes' or 'No' for each input. The values of t, k, x, and a are checked to ensure they meet specific constraints before processing.

