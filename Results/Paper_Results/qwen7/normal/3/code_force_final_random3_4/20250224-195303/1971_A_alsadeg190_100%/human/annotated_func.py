#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `i` is 2, `x` is the first integer from the input converted to an integer, `y` is the second integer from the input converted to an integer.
    #
    #After the loop executes all its iterations, the value of `i` will be equal to `x - 1` because the loop runs from `0` to `x-1`. However, based on the provided information, we only know the state after 3 iterations, so we can only conclude that `i` is 2. The values of `x` and `y` will be the values entered in the last iteration of the loop, as the loop continuously updates these values with the new inputs. The variable `t` remains unchanged as it was set initially and is not affected by the loop.
#Overall this is what the function does:The function processes an integer `t` where `1 ≤ t ≤ 100`, representing the number of test cases. For each test case, it reads two integers `x` and `y` where `0 ≤ x, y ≤ 9`. It then prints either `(x, y)` or `(y, x)` based on whether `x` is less than `y`. After processing all test cases, the function does not return any specific value but outputs pairs of integers based on the comparison condition.

