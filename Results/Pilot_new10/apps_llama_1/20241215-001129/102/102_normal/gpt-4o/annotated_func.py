#State of the program right berfore the function call: the program reads three integers n, a, and b from the input, where n, a, and b are positive integers and 1 ≤ n, a, b ≤ 10,000,000.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `a` is a positive integer in the range 1 to 10,000,000, `b` is an integer in the range 1 to 10,000,000, and either the loop has found integer values `x` and `y` such that `n = a*x + b*y` and printed them before returning, or it has completed all iterations without finding such values, with `x` being `n // a` in the latter case.
    print('NO')
#Overall this is what the function does:The function reads three integers n, a, and b from the input, attempts to find integer values x and y such that n = a*x + b*y, and prints "YES" along with the values of x and y if such a combination exists; otherwise, it prints "NO". The function handles all positive integers n, a, and b but may behave unexpectedly with zero or negative inputs and does not enforce the specified upper limit of 10,000,000 for n, a, and b. After executing, the function returns None.

