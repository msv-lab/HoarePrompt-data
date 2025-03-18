#State of the program right berfore the function call: The function should be called within a loop that iterates t times, where t is a non-negative integer such that 1 <= t <= 100. For each iteration, x and y are non-negative integers such that 0 <= x, y <= 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: `t` is a string input, `x` is a list containing 10 integers, `y` is a list containing 10 integers.
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: The values of `t`, `x`, and `y` remain unchanged. The loop prints pairs of integers from the lists `x` and `y` for each index `i` from 0 to 9. If `x[i]` is less than `y[i]`, it prints `x[i]` followed by `y[i]`. Otherwise, it prints `y[i]` followed by `x[i]`.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `t` from the input, which is expected to be a non-negative integer between 1 and 100. The function then reads 10 pairs of non-negative integers (each between 0 and 9) and stores them in two lists, `x` and `y`. After collecting the inputs, the function iterates through these lists and prints each pair of integers in ascending order. The function does not return any value. After the function concludes, the lists `x` and `y` contain 10 integers each, and the input `t` remains unchanged.

