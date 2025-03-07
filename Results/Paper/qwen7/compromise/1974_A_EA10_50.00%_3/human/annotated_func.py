#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, x and y are integers such that 0 ≤ x, y ≤ 99.
def func():
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        
        z = (y + 1) // 2
        
        m = 15 * z - y * 4
        
        if m < a:
            z = z + (x - m + 15 - 1) // 15
        
        print(z)
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `a` is an integer after all loop iterations, `z` is the final value calculated for each iteration of the loop based on the input values `x` and `y`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers: t, x, and y. For each test case, it calculates a value z based on x and y, ensuring z meets certain conditions relative to t. It then prints the final value of z for each test case. After processing all test cases, it outputs the calculated values of z for each case.

