#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n ≤ 10,000,000, 1 ≤ a ≤ 10,000,000, and 1 ≤ b ≤ 10,000,000.
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
        
    #State of the program after the  for loop has been executed: `a` is an integer such that 1 ≤ `a` ≤ 10,000,000; `b` is an input integer; `n` is a valid integer; `x` is `n // a`, and no valid `y` is calculated if `(n - x * a) % b != 0`. If at least one valid condition was met during the loop, then `y` is a non-negative integer derived from the condition that was satisfied; otherwise, `y` is undefined.
    print('NO')
#Overall this is what the function does:The function accepts three integers, `n`, `a`, and `b`, read from user input. It checks if `n` can be expressed as a non-negative integer combination of `a` and `b` (i.e., `n = x * a + y * b` for non-negative integers `x` and `y`). If a valid combination exists, it prints 'YES' along with values of `x` and `y`. If no valid combination is found after testing all possible values of `x`, it prints 'NO'. The function does not return any values.

