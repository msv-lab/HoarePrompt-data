#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func():
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        
        if n == m:
            print('Yes')
        elif m > n:
            print('No')
        elif m == n - 1:
            print('Yes')
        elif m % 2 == 0 and n % 2 == 0:
            print('Yes')
        elif m % 2 != 0 and n % 2 != 0:
            print('Yes')
        else:
            print('No')
        
    #State: t is an integer between 1 and 100 inclusive, i is 99 (since the loop runs t times), n is the first integer from the input split, m is the second integer from the input split, and the values of n and m remain unchanged regardless of the conditions checked within the loop.
#Overall this is what the function does:The function processes a series of test cases, each defined by two positive integers \( n \) and \( m \). For each test case, it checks specific conditions relating \( n \) and \( m \) and prints 'Yes' or 'No' based on whether these conditions are met. After processing all test cases, the function does not return any value.

