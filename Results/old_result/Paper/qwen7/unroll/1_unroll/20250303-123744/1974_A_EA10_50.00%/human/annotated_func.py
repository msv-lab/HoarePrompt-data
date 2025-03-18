#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are non-negative integers such that 0 ≤ x, y ≤ 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: Output State: The value of `z` after all iterations of the loop have executed, based on the input values provided within the loop. Specifically, for each iteration where `i` ranges from `0` to `a-1`, the value of `z` is calculated using the formula `(y + 1) // 2` and adjusted if `m < a`. The final value of `z` printed after the loop completes is the result.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer \( t \) and pairs of non-negative integers \( x \) and \( y \). For each test case, it calculates a value \( z \) based on the formula \((y + 1) // 2\) and adjusts it if another condition is met. After processing all test cases, it prints the final value of \( z \) for each case.

