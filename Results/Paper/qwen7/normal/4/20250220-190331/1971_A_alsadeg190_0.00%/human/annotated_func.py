#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `i` is a value between 0 and x (inclusive), `x` is an integer from the input split on the last iteration of the loop, and `y` is an integer from the input split on the last iteration of the loop. Regardless of the condition in the loop, `x` and `y` retain their values from the last input provided.
    #
    #In simpler terms, after the loop completes all its iterations, `x` will be the `x` value from the last input provided, and `y` will be the `y` value from the last input provided. The variable `i` will be equal to `x`, which is the total number of iterations the loop executed. The variable `t` remains unchanged from its initial state.
#Overall this is what the function does:The function processes a series of pairs of integers (x, y) up to a specified number of times (t). For each pair, it ensures that the first number in the pair is greater than or equal to the second number. If the first number is less than the second, it swaps them. After processing all pairs, it outputs the final values of x and y from the last input pair provided. The function does not return any value but prints the final x and y values.

