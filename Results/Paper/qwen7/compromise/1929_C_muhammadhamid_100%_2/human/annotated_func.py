#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, k is an integer such that 2 <= k <= 30, x is an integer such that 1 <= x <= 100, and a is an integer such that 1 <= a <= 10^9.
def func():
    for _ in range(int(input())):
        k, x, a = map(int, input().split())
        
        s = 1
        
        for i in range(x):
            s += s // (k - 1) + 1
        
        print('Yes' if a >= s else 'No')
        
    #State: Output State: After the loop executes all its iterations, the variable `k` retains its final value as determined by the loop's conditions, `x` also retains its final value as determined by the loop's conditions, and `a` remains unchanged as it is not affected by the loop. The variable `i` is set to `x + 1` because the loop runs from `i = 0` to `i = x - 1`, making `i` equal to `x` after all iterations. The variable `s` is updated through the loop to include the sum of `s // (k - 1) + 1` for each iteration from `i = 0` to `i = x - 1`. Given the operations `s += s // (k - 1) + 1` starting from `s = 1`, `s` will be the sum of 1 plus the result of adding `s // (k - 1) + 1` for each iteration, which ultimately results in `s` being `x + 1`.
    #
    #To summarize, the output state after the loop executes all its iterations is:
    #- `k`: The integer value entered by the user.
    #- `x`: The integer value entered by the user.
    #- `a`: The integer value entered by the user, unchanged.
    #- `i`: Equal to `x`.
    #- `s`: The sum of 1 plus the result of adding `s // (k - 1) + 1` for each iteration from `i = 0` to `i = x - 1`, resulting in `s = x + 1`.
#Overall this is what the function does:The function processes multiple inputs, each consisting of three integers \( k \), \( x \), and \( a \). For each input, it calculates a value \( s \) starting from 1 and updating it through a loop where \( s \) is incremented by \( s // (k - 1) + 1 \) for \( x \) iterations. After the loop, it prints 'Yes' if \( a \) is greater than or equal to \( s \), otherwise it prints 'No'. The function does not return any value but prints the result for each input.

