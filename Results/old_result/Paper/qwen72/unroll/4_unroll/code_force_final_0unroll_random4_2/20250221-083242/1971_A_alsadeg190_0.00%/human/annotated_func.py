#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. For each test case, it receives two integers x and y, where 0 <= x, y <= 9. The number of test cases t is a positive integer such that 1 <= t <= 100.
def func():
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The values of `x` and `y` will be updated to the last input values received during the loop execution. The number of test cases `t` remains unchanged.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of two integers `x` and `y` (0 <= x, y <= 9). For each test case, it prints the two integers in ascending order. The number of test cases is determined by the initial input `x`, which must be a positive integer (1 <= x <= 100). After processing all test cases, the values of `x` and `y` will be the last input values received during the loop execution, and the function does not return any value.

