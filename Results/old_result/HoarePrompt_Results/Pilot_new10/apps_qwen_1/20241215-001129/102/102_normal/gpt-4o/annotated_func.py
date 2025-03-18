#State of the program right berfore the function call: n, a, and b are integers such that 1 <= n, a, b <= 10 000 000, and n is the amount of money Vasya has, a is the cost of one bottle of Ber-Cola, and b is the cost of one Bars bar.
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
        
    #State of the program after the  for loop has been executed: Output State:
    print('NO')
#Overall this is what the function does:The function `func_1` reads three integers `n`, `a`, and `b` from input, where `n` represents the amount of money Vasya has, `a` is the cost of one bottle of Ber-Cola, and `b` is the cost of one Bars bar. It then attempts to find non-negative integers `x` and `y` such that `x * a + y * b = n`. If such integers exist, it prints 'YES' followed by the values of `x` and `y`, and returns immediately. If no such integers exist, it prints 'NO' and returns nothing.

