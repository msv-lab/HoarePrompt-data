#State of the program right berfore the function call: The function `func` is expected to be called within a loop that processes `t` test cases, where `t` is a non-negative integer such that 1 <= t <= 100. For each test case, the function receives two integers `x` and `y` as input, where 0 <= x, y <= 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: `t` is an input string representing a non-negative integer such that 1 <= t <= 100, `x` is a list containing the integer value of the first element of `xylist` ten times, `y` is a list containing the integer value of the second element of `xylist` ten times, `i` is 9.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: `t` is an input string representing a non-negative integer such that 1 <= t <= 100, `x` is a list containing the integer value of the first element of `xylist` ten times, `y` is a list containing the integer value of the second element of `xylist` ten times, and `i` is 9. The loop has completed all 10 iterations, and for each index `i` from 0 to 9, if `x[i]` is less than `y[i]`, the values of `x[i]` and `y[i]` were printed in the order `x[i]` followed by `y[i]`. Otherwise, the values of `y[i]` and `x[i]` were printed in the order `y[i]` followed by `x[i]`.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases (1 <= t <= 100). It then reads 10 pairs of integers (0 <= x, y <= 9) from the input, storing them in two lists `x` and `y`. For each of the 10 pairs, the function prints the two integers in ascending order. The function does not return any value. After the function concludes, the lists `x` and `y` contain the 10 pairs of integers, and the input `t` remains unchanged.

