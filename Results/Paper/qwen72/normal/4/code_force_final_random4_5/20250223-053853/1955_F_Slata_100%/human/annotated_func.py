#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, and each of the four integers p_i in the test cases is an integer such that 0 <= p_i <= 200.
def func():
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3))
        
    #State: The loop will execute `t` times, and for each iteration, it will read four integers `a`, `b`, `c`, and `d` from the input, then print the result of the expression `a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 2 == 3)`. The value of `t` will remain unchanged, and the values of `a`, `b`, `c`, and `d` will be read from the input for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, which represents the number of test cases. For each of the `t` test cases, it reads four integers `a`, `b`, `c`, and `d` from the input. It then calculates the sum of the integer division of each of these four integers by 2, and adds 1 to the sum if exactly three of the first three integers (`a`, `b`, `c`) are odd. The result of this calculation is printed for each test case. The function does not return any value. After the function concludes, the value of `t` remains unchanged, and the values of `a`, `b`, `c`, and `d` are no longer relevant as they are read and processed for each test case.

