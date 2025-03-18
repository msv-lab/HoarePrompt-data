#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, there are two integers n and m such that 1 <= n, m <= 100.
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
        
    #State: After executing the loop for all `t` test cases, the program will have printed 'Yes' or 'No' for each pair of integers `n` and `m` based on the given conditions. The state of `t` remains unchanged, and no other variables from the initial state are affected.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m` and prints 'Yes' or 'No' based on specific conditions. The conditions are: print 'Yes' if `n` equals `m`, if `m` is exactly one less than `n`, or if both `n` and `m` are either even or odd. Otherwise, it prints 'No'. The function does not modify `t` or any other input variables beyond using them to determine the output for each test case.

