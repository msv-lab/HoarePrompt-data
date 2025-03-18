#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if (n >= m) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: 'No'
    #State: t is a positive integer such that 1 ≤ t ≤ 100, n is an input integer, m is an input integer. If n is greater than or equal to m, no change is made to n. If n is less than m, n is set to a value less than m.
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers \( n \) and \( m \). It checks if \( n \) is greater than or equal to \( m \). If true, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value but prints the result directly.

