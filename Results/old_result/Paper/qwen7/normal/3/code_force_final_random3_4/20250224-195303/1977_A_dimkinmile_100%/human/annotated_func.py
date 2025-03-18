#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: Postcondition: `t` is a positive integer such that 1 ≤ t ≤ 100, `n` is an input integer, `m` is an input integer, and either `(n - m) % 2 == 0` and `n - m >= 0` or `(n - m) % 2 != 0` or `n - m < 0`.
#Overall this is what the function does:The function processes two integers, `n` and `m`, and checks if their difference is even and non-negative. If the condition is met, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value but modifies the output based on the input values.

