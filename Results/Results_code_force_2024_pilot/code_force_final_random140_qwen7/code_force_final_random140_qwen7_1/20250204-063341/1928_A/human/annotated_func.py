#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b and b % 2 != 0 or b / 2 == a and a % 2 != 0:
            print('NO')
        else:
            print('YES')
        
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4, n is an input integer, i is equal to n - 1, a and b are the last two integers entered by the user after converting them to integers.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \(a\) and \(b\). It checks specific conditions related to the parity of \(a\) and \(b\) and prints 'YES' if the conditions are not met, otherwise it prints 'NO'. The function does not return any value explicitly but prints the result for each test case.

