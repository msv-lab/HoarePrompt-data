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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `a` is an input integer between 1 and 10,000,000, `b` is an input integer where 1 ≤ `b` ≤ 10,000,000, `x` is the maximum integer from 0 to `n // a`, and (n - x * a) is never divisible by `b`. If `n` is less than `a`, then `x` is 0.
    print('NO')
#Overall this is what the function does:The function reads three integer inputs: n, a, and b. It checks if there exists non-negative integers x and y such that n = x * a + y * b, with x being derived from the maximum possible non-negative multiples of a that do not exceed n. If such integers exist, it prints 'YES' followed by the values of x and y; otherwise, it prints 'NO'. The function does not return any value explicitly, hence it returns None automatically if no conditions are met. Notably, the function's logic does not complete any return statement for the case where n < a and no valid (x, y) pair found, determining its conclusion solely through printed outputs, omitting that under those circumstances `y` would conceptually become n // b (though this value isn't utilized). Additionally, it lacks handling for cases where either a or b is zero, which could lead to undefined behavior in practical scenarios.

