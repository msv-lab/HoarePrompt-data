#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n, a, b ≤ 10,000,000.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `a` is an input integer within 1 to 10,000,000, `x` is `n // a`, and if `(n - x * a) % b == 0`, then `y` is `(n - x * a) // b`. If no such `x` results in `(n - x * a) % b == 0`, then the program does not output 'YES' and returns nothing.
    print('NO')
#Overall this is what the function does:The function accepts three integer inputs, `n`, `a`, and `b`, and checks if it is possible to express `n` as a combination of multiples of `a` and `b`. If such a combination exists, it outputs 'YES' followed by the counts of `a` and `b` used; otherwise, it outputs 'NO'. The function does not return any value explicitly, so it effectively returns `None`.

