#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            power = 1
            n = log2(n)
            while power < n:
                power += 1
            if power == n:
                print(2 ** power)
            else:
                power -= 1
                print(2 ** power)
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 10^4, `n_cases` is the number of test cases processed, each `n` is an integer input for which the program calculates either `n` itself if it's 1, or the highest power of 2 less than or equal to `n` if `n` is not 1.
#Overall this is what the function does:The function processes a specified number of test cases, where each test case involves an integer \( n \) (such that \( 1 \leq n \leq 10^9 \)). For each \( n \), if \( n = 1 \), it prints 1. Otherwise, it calculates and prints the highest power of 2 that is less than or equal to \( n \). The function implicitly accepts the number of test cases as input and does not return any value, instead printing the results for each test case.

