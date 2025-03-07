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
        
    #State: Output State: The output state consists of 'yes' or 'no' printed for each test case based on the conditions provided in the loop. For each test case, if both `a` and `b` are even, it prints 'yes'. If the difference between `a` and `b` is equal to `-a` or `-b`, it prints 'no'. If the difference between `a` and `b` is odd, it prints 'yes'. Otherwise, it prints 'no'.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \(a\) and \(b\). For each test case, it checks specific conditions related to the parity of \(a\) and \(b\) and their difference. If both \(a\) and \(b\) are even, it prints 'yes'. If the difference between \(a\) and \(b\) is equal to \(-a\) or \(-b\), it prints 'no'. If the difference between \(a\) and \(b\) is odd, it prints 'yes'. Otherwise, it prints 'no'. After processing all test cases, the function concludes with no explicit return value, but the output consists of 'yes' or 'no' for each test case.

