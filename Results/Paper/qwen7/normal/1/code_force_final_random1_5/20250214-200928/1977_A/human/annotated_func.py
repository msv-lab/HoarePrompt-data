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
        
    #State: t is an integer between 1 and 100 inclusive, i is t-1, n and m are the last input integers from the final split. If n equals m, no changes are made to n and m. If m is greater than n, no changes are made to n and m. If m equals n - 1, no changes are made to n and m. In all other cases, no changes are made to n and m.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \(n\) and \(m\). For each test case, it checks the relationship between \(n\) and \(m\) and prints 'Yes' or 'No' based on specific conditions. After processing all test cases, the function does not return any value but prints the results for each test case.

