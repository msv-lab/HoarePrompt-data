#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: Output State: The values of `t` and `x` remain unchanged, and the output consists of pairs of integers printed based on the condition in the loop. For each iteration `i` in the range of `x`, if the first integer `x` is greater than the second integer `y`, it prints `x` followed by `y`; otherwise, it prints `y` followed by `x`.
#Overall this is what the function does:The function reads multiple pairs of integers from the user input, compares each pair, and prints them in descending order if the first integer is greater than the second; otherwise, it prints them in ascending order. The function does not accept any parameters and does not return any value.

