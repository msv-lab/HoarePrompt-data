#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    t = input()
    x = []
    y = []
    for i in range(10):
        xylist = input().split(' ')
        
        x.append(int(xylist[0]))
        
        y.append(int(xylist[1]))
        
    #State: `xylist` is a list of strings split from the input; `x` is a list containing 10 integers, each being the integer version of the first element of each `xylist`; `y` is a list containing 10 integers, each being the integer version of the second element of each `xylist`; `i` is 9 (since the loop runs from 0 to 9, inclusive).
    for i in range(10):
        if x[i] < y[i]:
            print(x[i], ' ', y[i])
        else:
            print(y[i], ' ', x[i])
        
    #State: Output State: The loop has executed all 10 iterations. The variable `i` is now 10. For each iteration, the code compared the values of `x[i]` and `y[i]` and printed either `x[i]` followed by `y[i]` or `y[i]` followed by `x[i]` based on which value was smaller. After all iterations, the lists `x` and `y` remain unchanged because the loop only prints values and does not modify `x` or `y`. The `xylist` also remains unchanged as it is not modified within the loop.
#Overall this is what the function does:The function reads 10 pairs of integers from the user input, compares each pair, and prints the smaller number followed by the larger number. The original lists `x` and `y` remain unchanged after the function executes.

