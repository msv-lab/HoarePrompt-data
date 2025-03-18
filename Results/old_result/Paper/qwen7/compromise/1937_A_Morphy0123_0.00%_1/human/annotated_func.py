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
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\), `n_cases` is an integer greater than 2, `i` is 2, `n` is an integer greater than or equal to 1, and `power` is set to 5 if `n == 15`, otherwise `power` is 4 if `n != 15` and `n >= 16`, or `power` is at least 3 and does not equal `n` if `n < 16`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` (where 1 ≤ n ≤ 10^9). For each test case, it calculates a power value based on `n` and prints the result. If `n` is 1, it prints 1. Otherwise, it finds the smallest power of 2 greater than or equal to `n` and prints the value of that power.

