#State of the program right berfore the function call: The function should take two parameters, n and m, where n and m are integers such that 1 <= n, m <= 100.
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
        
    #State: The values of `n` and `m` will be the last pair of integers input by the user during the final iteration of the loop. The value of `t` remains unchanged. The loop will print 'Yes' or 'No' based on the conditions provided for each iteration.
#Overall this is what the function does:The function `func` reads an integer `t` from user input, which represents the number of test cases. For each test case, it reads two integers `n` and `m` from user input. It then checks several conditions and prints 'Yes' or 'No' based on these conditions for each test case. The conditions are: if `n` equals `m`, if `m` is greater than `n`, if `m` equals `n - 1`, if both `m` and `n` are even, or if both `m` and `n` are odd. After processing all test cases, the function does not return any value, and the final state of the program includes the last values of `n` and `m` input by the user, and the value of `t` remains unchanged.

