#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each of the t test cases, there are two space-separated integers x and y such that 0 ≤ x, y ≤ 9.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 100, `x` is the first integer from the last pair of input, `y` is the second integer from the last pair of input, and `i` is equal to the original value of `x`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, where 1 ≤ t ≤ 100. For each test case, it reads two space-separated integers `x` and `y` such that 0 ≤ x, y ≤ 9. It then prints the two integers in ascending order.

