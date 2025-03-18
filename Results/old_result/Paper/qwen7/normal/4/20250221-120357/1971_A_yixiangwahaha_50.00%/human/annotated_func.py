#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: Output State: `t` is an integer within the range 1 to 100, `x` is a list containing the integer values of `xylist[0]` repeated 10 times, `y` is a list containing the integer values of `xylist[1]` each incremented by 9, `i` is 10, `n` is 10, `xylist` is a list of strings split from the input, and `y` is appended with the integer value of `xylist[1]` nine more times.
    #
    #This means that after the loop has executed all 10 iterations, the list `x` will contain the integer value of `xylist[0]` ten times, and the list `y` will contain the integer value of `xylist[1]` ten times, each incremented by its respective index position minus one (since it starts from 1).
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: `t` is an integer within the range 1 to 100, `x` is a list containing the integer values of `xylist[0]` repeated 10 times, `y` is a list containing the integer values of `xylist[1]` each incremented by 9, `i` is 10, `n` is 10, `xylist` is a list of strings split from the input, and `y` is appended with the integer value of `xylist[1]` nine more times.
#Overall this is what the function does:The function reads an integer `t` and two lists of 10 integers each (`x` and `y`) from the input. It then compares corresponding elements of `x` and `y`, printing the smaller element followed by the larger element for each pair. After processing all pairs, the function does not return any value.

