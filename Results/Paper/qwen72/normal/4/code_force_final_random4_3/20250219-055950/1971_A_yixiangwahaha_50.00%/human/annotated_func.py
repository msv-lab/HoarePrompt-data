#State of the program right berfore the function call: The function should be called within a loop that iterates t times, where t is a non-negative integer such that 1 <= t <= 100. For each iteration, x and y are integers provided as input, with 0 <= x, y <= 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: After the loop executes all 10 iterations, `i` is 9, the loop will have iterated 10 times, `xylist` is a list of strings obtained by splitting the last input string on spaces, `x` is a list that now includes 10 integer values, each value being the first element of the `xylist` from each iteration, and `y` is a list that now includes 10 integer values, each value being the second element of the `xylist` from each iteration.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: `i` is 9, `xylist` is a list of strings obtained by splitting the last input string on spaces, `x` is a list of 10 integers, `y` is a list of 10 integers. For each iteration, if `x[i]` is less than `y[i]`, the condition `x[i] < y[i]` is true, and the output is `x[i]` followed by `y[i]`. Otherwise, the condition `x[i] < y[i]` is false, and the output is `y[i]` followed by `x[i]`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which is not used within the function. It then reads 10 pairs of integers (each pair on a new line) and stores them in two lists, `x` and `y`. After collecting the inputs, the function iterates through these lists and prints each pair of integers in a sorted order, ensuring that the smaller integer is printed first followed by the larger integer. The final state of the program after the function concludes is that `x` and `y` each contain 10 integers, and the function has printed 10 lines of sorted integer pairs.

