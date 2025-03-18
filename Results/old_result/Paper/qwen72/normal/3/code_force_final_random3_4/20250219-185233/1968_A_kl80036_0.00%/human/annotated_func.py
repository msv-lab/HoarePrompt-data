#State of the program right berfore the function call: The function `func` is expected to be called with an integer `x` where 2 ≤ x ≤ 1000. The function should also handle multiple test cases, where the number of test cases `t` is an integer such that 1 ≤ t ≤ 1000. For each test case, the function should find an integer `y` (1 ≤ y < x) that maximizes the value of gcd(x, y) + y.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `i` is `t-1`, `x` is an input integer greater than 0, `y` is the integer result of `x` divided by 2.
#Overall this is what the function does:The function `func` is designed to handle multiple test cases. It reads an integer `t` from the input, representing the number of test cases, where 1 ≤ t ≤ 1000. For each test case, it reads another integer `x` (2 ≤ x ≤ 1000) and calculates `y` as `x // 2`. The function then prints `y` for each test case. After processing all test cases, the function concludes without returning any value. The final state of the program includes `t` being an integer between 1 and 1000, `i` being `t-1`, and `x` being the last input integer greater than 0, with `y` being the integer result of `x` divided by 2.

