#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        
        if a == b:
            print('Bob')
        elif a == 1:
            print('Alice')
        elif b == 1:
            print('Bob')
        elif a % 2 == 1:
            print('Bob')
        elif a % 2 == 0 and b % 2 == 1:
            print('Alice')
        elif a > b:
            print('Bob')
        else:
            print('Alice')
        
    #State: T is a positive integer such that 1 ≤ T ≤ 1000, i is 999, a and b are the first and second input integers respectively after 999 iterations of the loop. In all cases, a and b retain their original values.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it determines whether "Alice" or "Bob" should win based on specific conditions related to \(a\) and \(b\). After processing all test cases, it prints the winner for each case.

