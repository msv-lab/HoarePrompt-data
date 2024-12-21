#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n ≤ 10,000,000 and 1 ≤ a ≤ 10,000,000 and 1 ≤ b ≤ 10,000,000.
def func():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        y = (n - x * a) // b
        
        if x * a + y * b == n:
            print('YES')
            print(x, y)
            exit()
        
    #State of the program after the  for loop has been executed: `n` is within the range 1 ≤ `n` ≤ 10,000,000; `a` is greater than 0; if there exist non-negative integers `x` and `y` such that `x * a + y * b == n`, then the program prints 'YES', followed by values of `x` and `y`, and exits; otherwise, after all iterations, `x` will be the maximum integer value such that `x * a ≤ n` and `y` will be the largest integer satisfying `y = (n - x * a) // b`, but the program will not print anything or terminate early.
    print('NO')
#Overall this is what the function does:The function reads three integers n, a, and b from input, where 1 ≤ n, a, b ≤ 10,000,000. It checks whether there exist non-negative integers x and y such that the equation x * a + y * b equals n. If such integers are found during the iteration over possible values of x, it prints 'YES' followed by the values of x and y, then it terminates the program. If no valid pairs (x, y) are found after all possible iterations, it prints 'NO'. The function performs no parameter checks or input validation and does not handle edge cases where inputs may lead to invalid values or types. It strictly relies on inputs to fit within the given constraints.

