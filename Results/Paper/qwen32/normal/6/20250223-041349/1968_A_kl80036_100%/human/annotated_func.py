#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the following t lines, there is an integer x such that 2 <= x <= 1000.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: `i` is equal to `t`, and all `x` values have been processed, with their corresponding `y` values (`x - 1`) printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, then for each of the following `t` lines, it reads an integer `x` and prints `x - 1`.

