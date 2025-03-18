#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 1000) representing the number of test cases. Each of the following t lines contains a single integer x (2 ≤ x ≤ 1000).
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: - After all `t` iterations, `i` will have taken on all values from 0 to `t-1`.
    #   - Each `x` will be an input integer for each iteration.
    #   - Each `y` will be `x - 1` for each iteration, and each `y` will have been printed.
    #
    #### Conclusion:
    #After the loop has executed all `t` iterations, there is no specific final state for `i`, `x`, and `y` because `i` will have completed its range from 0 to `t-1`, and `x` and `y` will have been re-assigned in each iteration based on the input values.
    #
    #However, the output state of the program can be described as the collection of all printed `y` values, one for each test case.
    #
    #### Output State:
    #Output State:
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each of the next `t` lines, it reads an integer `x` and prints `x - 1`.

