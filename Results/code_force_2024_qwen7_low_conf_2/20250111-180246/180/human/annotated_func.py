#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and each test case consists of three integers a, b, c such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b and b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State of the program after the  for loop has been executed: `t` is an integer value with 1 ≤ `t` ≤ 1000, `_` is the number of iterations completed (ranging from 1 to `t`), `a`, `b`, and `c` are the integers entered by the user in each iteration. If any of the conditions `a < b < c`, `a < b and b > c` are met at least once during the loop, the respective text ('STAIR', 'PEAK', or 'NONE') will be printed to the console. Otherwise, no text will be printed, and the final values of `a`, `b`, and `c` will be the last set of values entered by the user.
#Overall this is what the function does:- The function does not handle invalid inputs (e.g., non-integer values or out-of-range values for `a`, `b`, and `c`). If invalid inputs are provided, the function may raise an exception.
- The function assumes that valid test cases will always be provided. If `t` is less than 1 or greater than 1000, the function still processes the input but may raise an exception due to invalid input handling.
- The function does not store or return any intermediate results. All results are printed directly to the console.

