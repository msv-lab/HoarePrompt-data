#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, there are two space-separated integers x and y such that 0 ≤ x, y ≤ 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: `t` is a string representing the input value; `x` is a list containing the integer value of the first substring of `t` ten times; `y` is a list containing the integer value of the second substring of `t` ten times; `xylist` is a list of substrings obtained by splitting the last input string by spaces; `i` is 10.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: `t` is a string representing the input value; `x` is a list containing the integer value of the first substring of `t` ten times; `y` is a list containing the integer value of the second substring of `t` ten times; `xylist` is a list of substrings obtained by splitting the last input string by spaces; `i` is 10.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, then for each of the next `t` lines, it reads two space-separated integers `x` and `y`. For each pair, it prints the smaller of the two integers followed by the larger one.

