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
        
    #State: The loop has executed all its iterations, `n_cases` is an integer greater than 2, `i` is equal to `n_cases`, and for each iteration `i` from 0 to `n_cases-1`, the value of `power` is determined as follows:
#Overall this is what the function does:The function processes a series of test cases, each containing an integer \( n \). For each \( n \), it calculates a specific power of 2 and prints the result. If \( n \) is 1, it directly prints 1. Otherwise, it computes the smallest power of 2 that is greater than or equal to \( n \), and prints the value of that power. The function reads the number of test cases first, then for each test case, it reads \( n \) and performs the calculation and printing as described.

