#State of the program right berfore the function call: ** The input variables are as follows:
def func_1(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: The variables `x` and `y` are updated where `x` is assigned the greatest common divisor of the original `y` and the remainder of the original `x` divided by the original `y`, and `y` is assigned 0. The loop will not execute again as `y` is equal to 0.
    return x
    #The program returns the greatest common divisor of the original 'y' and the remainder of the original 'x' divided by the original 'y'.
#Overall this is what the function does:The function `func_1` calculates the greatest common divisor of two input parameters `x` and `y` using the Euclidean algorithm. It iteratively updates `x` and `y` until `y` becomes 0, where `x` then holds the greatest common divisor. The function returns this greatest common divisor. This function does not handle edge cases where one or both of the input parameters are negative.

#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5. The list of 2n integers contains values from 1 to n exactly two times each.**
def func_2():
    n = int(input())
    a = sorted(zip(map(int, input().split()), range(1, 2 * n + 1)))
    dist = 0
    prev = 1
    for i in range(n):
        pos = a[2 * i][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `n` is an integer, `a` contains 2n integers sorted in ascending order, `dist` is the sum of absolute differences between consecutive positions in `a`, `prev` is the position of the last element processed in the loop
    prev = 1
    for i in range(n):
        pos = a[2 * i + 1][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `n` is still an integer, `a` contains at least `2n+1` integers sorted in ascending order, `dist` is updated based on the final `a` values, `prev` is the last value of `pos` assigned in the loop, `pos` is assigned the second element of the sublist at index `2 * n + 1`, `dist` includes all the absolute differences between consecutive positions in the final `a` list
    print(dist)
#Overall this is what the function does:The function does not accept any parameters. It reads an integer `n` and a list of 2n integers where each value from 1 to n appears exactly twice. The function calculates the sum of absolute differences between consecutive positions of the elements in the list and prints the final sum as output.

