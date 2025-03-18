#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 50, and for each test case, n is an integer such that 2 ≤ n ≤ 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 2):
            print(i, i)
        
    #State: Output State: `i` will be `n + 2`, and `n` must be greater than 4.
    #
    #Natural Language Description: After the loop has executed all its iterations, the value of `i` will be `n + 2`. This is because the loop starts from 3 and increments `i` up to `n + 1`, making the final value of `i` equal to `n + 2`. Additionally, for the loop to run at least once, `n` must be greater than 4. Since the loop runs based on the input `n`, `n` must maintain this condition to complete all iterations.
#Overall this is what the function does:The function accepts no parameters and processes two inputs, `t` and `n`. For each test case defined by `t`, it prints specific pairs of integers. Initially, it prints `(1, 1)` and `(1, 2)`. Then, it iterates from 3 to `n + 1`, printing each integer twice. After completing all iterations, the final value of the loop variable `i` will be `n + 2`, with the constraint that `n` must be greater than 4 for the loop to execute fully. The function does not return any value.

