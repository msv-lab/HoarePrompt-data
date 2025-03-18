#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: Output State: The loop will continue to execute as long as the user provides more inputs. After all iterations, `i` will be equal to the total number of times the loop has executed, which is the value entered on the first line minus one. For each iteration, `x` will be an integer between 2 and 1000 (inclusive), and `y` will be `x // 2`. The final value of `i` will be the total number of inputs provided, and `y` will be the result of dividing the last provided `x` by 2.
#Overall this is what the function does:The function processes a series of test cases where the number of test cases \( t \) is provided first, followed by \( t \) integers \( x \) (each between 2 and 1000 inclusive). For each \( x \), it calculates \( y \) as \( x \) divided by 2 using integer division and prints \( y \). After processing all test cases, the function does not return any value but outputs the results of the calculations.

