#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. Each of the following t lines contains two space-separated integers x and y (0 ≤ x, y ≤ 9).
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: `t` is an input string representing the number of test cases, `x` is a list containing ten integer values of `xylist[0]` from ten different inputs, `y` is a list containing ten integer values of `xylist[1]` from ten different inputs, `i` is 10.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: `t` is an input string representing the number of test cases, `x` is a list containing ten integer values of `xylist[0]` from ten different inputs, `y` is a list containing ten integer values of `xylist[1]` from ten different inputs, and `i` is 10. The loop has printed the smaller of `x[i]` and `y[i]` followed by the larger for each `i` from 0 to 9.
#Overall this is what the function does:The function reads ten pairs of integers, each pair consisting of two space-separated integers `x` and `y` (0 ≤ x, y ≤ 9). For each pair, it prints the smaller integer followed by the larger integer.

