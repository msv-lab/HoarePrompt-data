#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, X is an integer such that 2 ≤ X ≤ 10^18.
def func():
    for i in range(int(input())):
        x = int(input())
        
        max = 100000000
        
        min = -100000000
        
        ans = ''
        
        t = 0
        
        while x != 1:
            if x % 2 == 0:
                ans = f'{max}' + ' ' + ans
                max -= 1
                x = x // 2
            else:
                ans = f'{min}' + ' ' + ans
                min += 1
                x -= 1
            t += 1
        
        print(t)
        
        print(*ans)
        
    #State: `min` is 999999, `ans` is a string containing all the `min` and `max` values from each iteration with appropriate spacing, `i` is `input_value - 1`, `max` is 1, `t` is the total number of iterations until `x` becomes 1.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes an integer \(X\) (with \(2 \leq X \leq 10^{18}\)) and an integer \(t\) (with \(1 \leq t \leq 1000\)). It calculates the number of iterations \(t\) required to reduce \(X\) to 1 by repeatedly dividing \(X\) by 2 when even or decrementing \(X\) by 1 when odd. Additionally, it constructs a string `ans` containing a sequence of maximum and minimum values encountered during the process. Finally, it prints the total number of iterations and the constructed string.

