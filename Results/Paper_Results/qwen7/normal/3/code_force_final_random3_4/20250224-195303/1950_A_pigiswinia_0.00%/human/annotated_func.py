#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIRS')
        elif a < b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State: The loop has executed all its iterations, with `t` being the total number of iterations specified initially. The variables `a`, `b`, and `c` have been updated according to the conditions within the loop for each iteration. If `a < b < c` was true for any iteration, 'STAIRS' was printed for that iteration; if `a < b > c` was true, 'PEAK' was printed; otherwise, 'NONE' was printed. The variable `i` is now equal to `t - 1`, as the loop runs from `i` in the range `0` to `t-1`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases, followed by `t` sets of three integers `a`, `b`, and `c`. For each set, it checks if `a < b < c` or `a < b > c`. If the first condition is met, it prints 'STAIRS'; if the second condition is met, it prints 'PEAK'; otherwise, it prints 'NONE'. After processing all test cases, the function does not return any value.

