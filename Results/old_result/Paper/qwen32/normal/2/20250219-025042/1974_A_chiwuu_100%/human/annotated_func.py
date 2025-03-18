#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, there are two integers x and y such that 0 ≤ x, y ≤ 99.
def func():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        
        a = int(a)
        
        b = int(b)
        
        t = b
        
        if t % 2 == 0:
            t = t // 2
        else:
            t = t // 2 + 1
        
        t1 = t * 15 - b * 4
        
        if t1 >= a:
            t = t
        else:
            t2 = a - t1
            if t2 % 15 == 0:
                t = t + t2 // 15
            else:
                t = t + t2 // 15 + 1
        
        print(t)
        
    #State: - After all `n` iterations, the final value of `t` will be printed for each test case.
    #
    #### Example Calculation:
    #
    #Let's assume the following inputs for a single test case:
    #- `t` (initial) = 5 (from the problem statement, `t` is the number of test cases, but here we consider one test case with `x=5` and `y=3`)
    #- `n` = 3 (number of iterations)
    #- Inputs for each iteration:
    #  - Iteration 1: `a = 10`, `b = 6`
    #  - Iteration 2: `a = 20`, `b = 8`
    #  - Iteration 3: `a = 30`, `b = 10`
    #
    ##### Iteration 1:
    #- `a = 10`, `b = 6`
    #- `t = b // 2 = 6 // 2 = 3` (since `b` is even)
    #- `t1 = t * 15 - b * 4 = 3 * 15 - 6 * 4 = 45 - 24 = 21`
    #- Since `t1 >= a` (21 >= 10), `t` remains 3.
    #
    ##### Iteration 2:
    #- `a = 20`, `b = 8`
    #- `t = b // 2 = 8 // 2 = 4` (since `b` is even)
    #- `t1 = t * 15 - b * 4 = 4 * 15 - 8 * 4 = 60 - 32 = 28`
    #- Since `t1 >= a` (28 >= 20), `t` remains 4.
    #
    ##### Iteration 3:
    #- `a = 30`, `b = 10`
    #- `t = b // 2 = 10 // 2 = 5` (since `b` is even)
    #- `t1 = t * 15 - b * 4 = 5 * 15 - 10 * 4 = 75 - 40 = 35`
    #- Since `t1 >= a` (35 >= 30), `t` remains 5.
    #
    #### Final Output State:
    #After all iterations, the final value of `t` is 5 for this test case.
    #
    #### Generalized Output State:
    #For any given test case with initial `t` (which is the number of test cases), and `n` iterations, the final value of `t` after all iterations will depend on the specific values of `a` and `b` provided in each iteration. However, the process described above will always yield the final value of `t` after all iterations.
    #
    #### Conclusion:
    #The final output state after all iterations of the loop is determined by the iterative updates of `t` based on the conditions provided in the loop body. The exact value of `t` will vary depending on the inputs, but the process remains consistent.
    #
    #Output State:
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads two integers `a` and `b`. It then calculates a value `t` based on `b` and adjusts `t` if necessary to ensure that `t * 15 - b * 4` is at least `a`. Finally, it prints the calculated value of `t` for each test case.

