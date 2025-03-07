#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: Output State: `t` is an input integer within the range 1 to 100; `x` is a list containing 10 integers; `y` is a list containing 10 integers.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: Output State: The loop will compare each pair of elements from lists `x` and `y`, and print the smaller value followed by the larger value for each comparison. Since the initial values of `x` and `y` are not specified, the exact printed output cannot be determined without those values. However, the output will consist of 10 lines, each showing two numbers separated by a space, where the first number is the smaller of the two compared numbers from `x` and `y` at the same index, and the second number is the larger one.
#Overall this is what the function does:The function reads an integer `t` and two lists of integers `x` and `y` from the user. It then compares the corresponding elements of `x` and `y` for 10 pairs and prints each comparison result, showing the smaller value followed by the larger value for each pair. The function does not return any value.

