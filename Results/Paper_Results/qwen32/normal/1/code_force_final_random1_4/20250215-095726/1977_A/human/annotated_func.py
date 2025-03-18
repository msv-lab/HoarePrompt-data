#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, and for each of the t test cases, there are two integers n and m such that 1 ≤ n, m ≤ 100.
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
        
    #State: `t` is an input integer such that 1 ≤ `t` ≤ 100, `i` is `t - 1`, and for each of the `t` test cases, the program has printed 'Yes' or 'No' based on the conditions provided in the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m` and prints 'Yes' or 'No' based on specific conditions related to the parity and values of `n` and `m`.

