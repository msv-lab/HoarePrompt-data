#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
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
        
    #State: After the loop executes all the iterations, `t` is a positive integer such that 1 ≤ t ≤ 10^4, `a` is the first integer input, `b` is the second integer input, and `i` equals the total number of test cases (`t`). The loop processes each test case, and based on the conditions provided, it prints 'yes' or 'no'.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three positive integers: `t`, `a`, and `b`. It checks specific conditions related to the parity of `a` and `b`, and prints 'yes' or 'no' based on these conditions. The function does not return any value but prints the results for each test case.

