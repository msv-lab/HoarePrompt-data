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
        
    #State: T is a positive integer such that 1 ≤ T ≤ 1000, i is equal to T, a and b are integers from the input. The values of a and b do not change throughout the loop executions unless they meet specific conditions inside the loop. Specifically, if a equals b, a is set to b; if a is even, a is halved; if a is odd, i is set to 1; if b equals 1, b remains 1; if a is greater than b, a remains unchanged; if a is less than or equal to b, a is set to 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \(a\) and \(b\). For each test case, it determines whether "Alice" or "Bob" wins based on specific conditions involving \(a\) and \(b\), and prints the winner for each case. The function does not return any value but prints the result for each test case.

