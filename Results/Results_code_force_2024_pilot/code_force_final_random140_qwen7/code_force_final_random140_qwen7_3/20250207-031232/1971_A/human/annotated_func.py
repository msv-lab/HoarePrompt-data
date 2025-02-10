#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(max(a, b), min(a, b))
        
    #State: Output State: `t` must be greater than 0, `a` is an integer from the input, `b` is an integer from the input, and this process is repeated for each iteration up to the value of `t`. After all iterations, the final values of `a` and `b` will be the maximum and minimum values from all the pairs of integers input during the loop executions, respectively.
#Overall this is what the function does:The function reads a series of integer pairs from the user, prints the maximum and minimum values of each pair, and repeats this process for a number of times specified by the user (t). After all iterations, the final printed values are the maximum and minimum values from all the pairs of integers input during the loop executions.

