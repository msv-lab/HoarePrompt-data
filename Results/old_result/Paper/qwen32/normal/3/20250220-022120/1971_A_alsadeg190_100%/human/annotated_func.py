#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases, followed by t lines, each containing two space-separated integers x and y (0 ≤ x, y ≤ 9).
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The final values of `x` and `y` are the last pair read, and `i` is equal to the initial value of `x`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, followed by `t` lines, each containing two space-separated integers `x` and `y`. For each test case, it prints the two integers in ascending order.

