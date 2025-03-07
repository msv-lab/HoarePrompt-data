#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, a and b are integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: The loop has processed all `t` test cases and printed 'yes' or 'no' for each pair of integers `(a, b)` based on the given conditions.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `a` and `b` and prints 'yes' or 'no' based on specific conditions related to the parity of `a` and `b` and their difference.

