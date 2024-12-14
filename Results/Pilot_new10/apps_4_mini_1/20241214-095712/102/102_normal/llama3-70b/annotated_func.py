#State of the program right berfore the function call: n, a, and b are integers such that 1 ≤ n, a, b ≤ 10,000,000.
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
        
    #State of the program after the  for loop has been executed: `a` is an integer within 1 to 10,000,000; `b` is an input integer; `n` is an integer within 1 to 10,000,000; `x` is a non-negative integer such that `x <= n // a`; `y` is a non-negative integer such that `y = (n - x * a) // b for the final x value checked, or `y` is `n // b` if the loop does not execute.`
    print('NO')
#Overall this is what the function does:The function accepts three integers, `n`, `a`, and `b`, from user input, representing a total number that must be constructed using non-negative integer coefficients of `a` and `b`. It iterates over possible coefficients for `a` (denoted as `x`), and for each `x`, it computes the corresponding coefficient for `b` (denoted as `y`). If there exist non-negative integers `x` and `y` such that their respective contributions (`x * a + y * b`) equal `n`, the function prints 'YES' followed by the values of `x` and `y`. If no such combination is found after checking all valid `x`, it prints 'NO'. The function does not return any value; it only prints the result.

