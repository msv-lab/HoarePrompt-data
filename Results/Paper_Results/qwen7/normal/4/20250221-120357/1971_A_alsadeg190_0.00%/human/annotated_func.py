#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 100, `i` is `x`, `x` and `y` are input integers from each iteration of the loop. The final values of `x` and `y` will depend on the comparison in each iteration, but `t` remains unchanged.
#Overall this is what the function does:The function reads multiple pairs of integers from the user input, compares each pair, and prints the larger number followed by the smaller number. The variable `t` is not used within the function and remains unchanged. The function does not return any value.

