#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each test case, x and y are integers such that 0 ≤ x, y ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        x, y = map(int, input().split())
        
        print(min(x, y), max(x, y))
        
    #State of the program after the  for loop has been executed: - \( t \) is a non-negative integer such that \( 1 \leq t \leq 100 \).
    #- \( x \) is an integer such that \( 0 \leq x \leq 9 \).
    #- \( y \) is an integer such that \( 0 \leq y \leq 9 \).
    #- If \( t > 0 \), the loop processes \( t \) pairs of integers and prints the minimum and maximum of each pair. After all iterations, \( x \) and \( y \) will hold the values of the last pair of integers entered by the user.
    #- If \( t = 0 \), the loop does not execute, and the values of \( x \) and \( y \) remain as they were in the initial state.
#Overall this is what the function does:The function reads an integer `t` which represents the number of test cases (where 1 ≤ t ≤ 100). For each test case, it reads two integers `x` and `y` (where 0 ≤ x, y ≤ 9) and prints the minimum and maximum of each pair. After processing all test cases, if `t` is greater than 0, `x` and `y` will hold the values of the last pair of integers entered by the user. If `t` is 0, the loop does not execute, and the values of `x` and `y` remain unchanged from their initial state.

