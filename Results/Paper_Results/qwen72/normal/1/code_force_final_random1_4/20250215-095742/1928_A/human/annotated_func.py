#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    for i in range(int(input())):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 == 0 and b % 2 == 0:
            print('yes')
        elif (a - b == -a, a) or (b - a == -b, b):
            print('no')
        elif (a - b) % 2 > 0 or (a - b) % 2 < 0:
            print('yes')
        else:
            print('no')
        
    #State: After the loop has executed all iterations, `t` is a positive integer such that 1 ≤ t ≤ 10^4, and for each of the `t` test cases, `a` and `b` are positive integers such that 1 ≤ a, b ≤ 10^9. The variable `i` will be equal to `t - 1`. For each iteration, the values of `a` and `b` were read from the input, and based on the conditions in the loop, the program printed 'yes' or 'no' accordingly. After the loop completes, the final values of `a` and `b` will be the ones from the last iteration, but these values are not retained for further use outside the loop.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `a` and `b`. It then checks the following conditions for each pair of `a` and `b`: if both `a` and `b` are even, it prints 'yes'. If the difference between `a` and `b` is odd, it prints 'yes'. Otherwise, it prints 'no'. After processing all test cases, the function does not return any value, but the final state of the program includes the values of `a` and `b` from the last test case, though these values are not retained for further use.

