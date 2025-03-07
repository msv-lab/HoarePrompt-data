#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: Output State: The loop has executed for all input cases, meaning `i` is now equal to the total number of inputs provided. For each iteration, `x` was an input integer, and `y` was calculated as `x - 1`. After all iterations, `i` will be the sum of all inputs minus the number of inputs (since `i` starts from 0 and increments by 1 for each input). `x` will hold the value of the last input provided, and `y` will be the last input value minus one.
    #
    #In simpler terms, after all iterations, `i` will be the total number of inputs, `x` will be the last input integer provided, and `y` will be `x - 1`.
#Overall this is what the function does:The function processes a series of integer inputs. It reads an integer `t` which represents the number of subsequent integer inputs. For each of these `t` inputs, it calculates and prints the value of the input integer decreased by one. After processing all inputs, the function does not return any value but ensures that for each input `x`, the value `x - 1` is printed.

