#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
def func_1():
    n, m = map(int, input().split())
    if ((n - m) % 2 == 0 and n - m >= 0) :
        print('Yes')
        #This is printed: Yes
    else :
        print('No')
        #This is printed: No
    #State: t is a positive integer such that 1 ≤ t ≤ 100, n is an input integer, m is an input integer. If the difference between n and m is even and non-negative, the postcondition remains the same as the precondition. Otherwise, the condition (n - m) % 2 ≠ 0 or n - m < 0 holds true.
#Overall this is what the function does:The function processes a test case consisting of two positive integers \( n \) and \( m \), where \( 1 \leq n, m \leq 100 \). It checks if the difference between \( n \) and \( m \) is even and non-negative. If the condition is met, it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value but modifies the output stream by printing either 'Yes' or 'No' based on the condition.

