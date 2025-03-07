#State of the program right berfore the function call: The function should be called within a loop that processes t test cases, where t is an integer such that 1 <= t <= 100. For each test case, x and y are integers provided as space-separated values, with 0 <= x, y <= 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: `t` remains the same as the initial input integer, `x` is a list of 10 integers, `y` is a list of 10 integers.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: `t` remains the same as the initial input integer, `x` is a list of 10 integers, `y` is a list of 10 integers. The loop prints pairs of integers from `x` and `y` for each index `i` from 0 to 9. If `x[i]` is less than `y[i]`, it prints `x[i]` followed by `y[i]`. Otherwise, it prints `y[i]` followed by `x[i]`. The values of `x` and `y` are not modified by the loop.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, indicating the number of test cases, and then reads 10 pairs of integers (x, y) for each test case. It stores these integers in two lists, `x` and `y`. After reading the inputs, the function prints the pairs of integers from `x` and `y` for each index `i` from 0 to 9, ensuring that the smaller integer is printed first followed by the larger integer. The function does not return any value, and the lists `x` and `y` are not modified after the printing. The initial input integer `t` remains unchanged throughout the function's execution.

