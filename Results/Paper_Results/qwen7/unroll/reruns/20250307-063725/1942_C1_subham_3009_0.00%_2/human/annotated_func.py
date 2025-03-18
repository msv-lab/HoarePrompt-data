#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, x, and y are integers such that 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0. The vertices Bessie has chosen are represented by x distinct integers from 1 to n. The sum of x over all test cases does not exceed 2⋅10^5.
def func():
    if (__name__ == '__main__') :
        t = int(input())
        while t > 0:
            t -= 1
            
            [n, x, y] = map(int, input().split())
            
            arr = input().split()
            
            arr = [int(arr[i]) for i in range(x)]
            
            print(x - 2)
            
        #State: Output State: The output state will be a series of integers, each being "x - 2", where "x" is the value of the variable "x" provided in each iteration of the loop.
        #
        #Explanation: In each iteration of the while loop, the value of `t` is decremented by 1. The values of `n`, `x`, and `y` are read from user input, but these values do not affect the final output. The array `arr` is also populated with some integers based on the value of `x`, but again, these details do not influence the final output. The only operation that produces output is `print(x - 2)`, which prints `x - 2` for each iteration. Since the loop continues until `t` becomes 0, the number of times this print statement is executed is equal to the initial value of `t`. Therefore, the output will consist of `t` lines, each containing an integer that is `x - 2` from the corresponding iteration.
    #State: The output consists of `t` lines, each containing the value `x - 2` from the corresponding iteration.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `t` (1 ≤ t ≤ 10^4). For each test case, it reads additional integers `n`, `x`, and `y` (with 4 ≤ n ≤ 10^9, 2 ≤ x ≤ min(n, 2⋅10^5), and y = 0), and a list of `x` distinct integers representing vertices. The function then prints `x - 2` for each test case, resulting in `t` lines of output, each containing the value `x - 2`.

