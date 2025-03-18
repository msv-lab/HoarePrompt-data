#State of the program right berfore the function call: The function should take an integer x as input where 2 ≤ x ≤ 1000, and it should be called multiple times with different values of x, each time finding an integer y such that 1 ≤ y < x and \gcd(x, y) + y is maximized.
def func():
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: `i` is equal to the user-provided number of iterations (an integer between 2 and 1000), `x` is the last input integer provided (2 ≤ x ≤ 1000), and `y` is equal to `x // 2`.
#Overall this is what the function does:The function reads an integer from the user, which represents the number of iterations to perform. For each iteration, it reads another integer `x` (where 2 ≤ x ≤ 1000) and calculates `y` as `x // 2`. It then prints `y` for each iteration. After the function concludes, the number of iterations `i` is equal to the user-provided number of iterations, `x` is the last input integer provided (2 ≤ x ≤ 1000), and `y` is equal to `x // 2` for the last iteration. The function does not return any value.

