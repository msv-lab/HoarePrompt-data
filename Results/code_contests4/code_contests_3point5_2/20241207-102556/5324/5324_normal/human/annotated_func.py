#State of the program right berfore the function call: **Precondition**: **n is a positive integer. a_i is an integer representing the size of the tier in the i-th house, and it follows the constraints 1 ≤ a_i ≤ n. Each number from 1 to n occurs exactly twice in the list of a_i's.**
def func_1(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
        
    #State of the program after the loop has been executed: `x` and `y` are updated based on their previous values until `y` becomes 0, at that point `x` holds the greatest common divisor of the initial values of `x` and `y`, and `y` is 0
    return x
    #The program returns the greatest common divisor of the initial values of `x` and `y` when `y` becomes 0
#Overall this is what the function does:The function func_1 accepts two positive integers `x` and `y` and calculates the greatest common divisor of the initial values of `x` and `y`. It achieves this by continuously updating `x` and `y` until `y` becomes 0. The function then returns the greatest common divisor of the initial values of `x` and `y`.

#State of the program right berfore the function call: **Precondition**: **n is an integer such that 1 ≤ n ≤ 10^5. The list a contains 2n integers where each integer represents the size of a tier and is between 1 and n (inclusive). Each number from 1 to n occurs exactly twice in the list a.**
def func_2():
    n = int(input())
    a = sorted(zip(map(int, input().split()), range(1, 2 * n + 1)))
    dist = 0
    prev = 1
    for i in range(n):
        pos = a[2 * i][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `a` is a sorted list of tuples where each tuple contains the size of a tier and its corresponding index, each number from 1 to n occurs exactly twice, `dist` is the sum of the absolute differences between consecutive index values in the tuples in list `a`, `prev` is equal to the index value from the last tuple in list `a`, `n` is greater than or equal to the length of list `a`
    prev = 1
    for i in range(n):
        pos = a[2 * i + 1][1]
        
        dist += abs(pos - prev)
        
        prev = pos
        
    #State of the program after the  for loop has been executed: `a` is a sorted list of tuples, `dist` is the sum of the absolute differences between consecutive index values in the tuples in list `a`, `prev` is the index value from the last tuple in list `a`, `n` is greater than or equal to the length of list `a`
    print(dist)
#Overall this is what the function does:The function `func_2` reads an integer `n` from input and a list `a` consisting of 2n integers where each integer represents the size of a tier and is between 1 and n (inclusive), with each number from 1 to n occurring exactly twice in the list. The function then calculates the total distance `dist` by summing the absolute differences between consecutive indices of the sorted list `a`. Finally, it prints the total distance `dist`. The function does not accept any parameters and operates within the constraints specified.

