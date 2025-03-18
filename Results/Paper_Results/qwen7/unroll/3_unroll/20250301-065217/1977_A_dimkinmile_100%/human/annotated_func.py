#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 100, `n` is an input integer, `m` is an input integer. If `(n - m)` is even and greater than or equal to 0, then `(n - m)` remains unchanged. Otherwise, `(n - m)` is adjusted so that it becomes even and non-negative.
#Overall this is what the function does:The function processes two positive integers \( n \) and \( m \) (where \( 1 \leq n, m \leq 100 \)) and a positive integer \( t \) (where \( 1 \leq t \leq 100 \)). It checks if the difference \( n - m \) is even and non-negative. If true, it prints 'Yes'. Otherwise, it prints 'No'. The function does not return any value but outputs 'Yes' or 'No' based on the condition.

