#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, x is an integer such that 2 ≤ x ≤ 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: Output State: After the loop executes all its iterations, `i` will be equal to the total number of inputs provided minus one, `x` will be the last input integer provided where 2 ≤ x ≤ 1000, and `y` will be `x - 1`.
    #
    #This means that if there were `n` total inputs, `i` would be `n-1`, and `y` would be the value of the last input minus one.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (1 ≤ t ≤ 1000) and an integer `x` (2 ≤ x ≤ 1000). For each test case, it reads the values of `t` and `x`, calculates `y` as `x - 1`, and prints `y`. After processing all test cases, the function does not return any value but leaves the program in a state where the last printed value is `x - 1` for the last test case provided.

