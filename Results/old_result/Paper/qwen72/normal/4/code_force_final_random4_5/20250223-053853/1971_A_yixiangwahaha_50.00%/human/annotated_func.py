#State of the program right berfore the function call: The function is designed to handle multiple test cases, where each test case consists of two integers x and y. The number of test cases t is a positive integer such that 1 <= t <= 100, and for each test case, x and y are integers in the range 0 <= x, y <= 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: `t` is an input string representing the number of test cases, `x` is a list containing 10 integers, and `y` is a list containing 10 integers, where each integer in `x` and `y` is between 0 and 9 (inclusive).
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: The values of `t`, `x`, and `y` remain unchanged. The loop prints pairs of integers from the lists `x` and `y` for each index `i` from 0 to 9. If `x[i]` is less than `y[i]`, it prints `x[i]` followed by `y[i]`. Otherwise, it prints `y[i]` followed by `x[i]`.
#Overall this is what the function does:The function `func` processes 10 test cases, each consisting of two integers `x` and `y` within the range 0 to 9. It reads the number of test cases `t` but does not use it in the function. For each test case, it prints the two integers in ascending order. The function does not return any value, and the lists `x` and `y` remain unchanged after the function concludes.

