#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n is an integer such that 1 ≤ n ≤ 10^9.
def func():
    n_cases = int(input())
    for i in range(n_cases):
        n = int(input())
        
        if n == 1:
            print(1)
        else:
            power = 1
            while power < log2(n):
                power += 1
            if power == n:
                print(2 ** power)
            else:
                power -= 1
                print(2 ** power)
        
    #State: Postcondition: `t` is an integer such that \(1 \leq t \leq 10^4\), `n_cases` is the total number of cases entered by the user, `i` is the last index processed by the loop (ranging from 1 to `n_cases`), `n` is the integer input from the user for the current case, and `power` is the smallest integer greater than or equal to the base-2 logarithm of `n`. If `n` equals 1, `power` is set to 4. Otherwise, if `power` equals `n`, it remains unchanged; otherwise, `power` is adjusted to be within the range `[log2(n) - 1, log2(n))`.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer \( n \). For each \( n \), it calculates the smallest integer greater than or equal to the base-2 logarithm of \( n \). If \( n \) is 1, it prints 1. Otherwise, it prints \( 2 \) raised to the calculated power. The function does not return any value but prints the results for each test case.

