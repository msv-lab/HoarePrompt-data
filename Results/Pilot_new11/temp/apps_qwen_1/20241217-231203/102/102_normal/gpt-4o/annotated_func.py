#State of the program right berfore the function call: n, a, and b are integers such that 1 <= n, a, b <= 10 000 000, and n, a, and b represent the amount of money Vasya has, the cost of one bottle of Ber-Cola, and the cost of one Bars bar respectively.
def func_1():
    n = int(input())
    a = int(input())
    b = int(input())
    for x in range(n // a + 1):
        if (n - x * a) % b == 0:
            y = (n - x * a) // b
            print('YES')
            print(x, y)
            return
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than or equal to `a`, and `a` and `b` are integers. If the loop executes, there exists an integer `x` in the range `0` to `n // a` such that `(n - x * a) % b == 0`, and the loop prints 'YES' with the values `x` and `y = (n - x * a) // b`. If the loop does not execute, the values of `n`, `a`, and `b` remain as they were initially and there is no such `x` that satisfies the condition.
    print('NO')
#Overall this is what the function does:The function accepts no parameters and does not return any value. It prompts the user to input three integers \( n \), \( a \), and \( b \), where \( n \) represents the amount of money Vasya has, \( a \) is the cost of one bottle of Ber-Cola, and \( b \) is the cost of one Bars bar. The function then checks if there exist non-negative integers \( x \) and \( y \) such that \( n - x \cdot a = y \cdot b \). If such integers exist, the function prints 'YES' followed by the values of \( x \) and \( y \). If no such integers exist, the function prints 'NO'.

