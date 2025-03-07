#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: Output State: `t` is an integer between 1 and 100 inclusive; `x` is a list with 10 elements, each element is an integer; `y` is a list with 10 elements, each element is an integer.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: Output State: The output state will consist of 10 lines, each line containing two integers separated by a space. For each iteration `i` from 0 to 9, if the value of `x[i]` is less than the value of `y[i]`, the line will display `x[i]` followed by `y[i]`. Otherwise, it will display `y[i]` followed by `x[i]`.
#Overall this is what the function does:The function reads 10 pairs of integers from the input, where each pair consists of two integers \(x\) and \(y\). It then prints 10 lines, each containing two integers separated by a space. For each pair, if \(x\) is less than \(y\), it prints \(x\) followed by \(y\); otherwise, it prints \(y\) followed by \(x\). The function does not return any value.

