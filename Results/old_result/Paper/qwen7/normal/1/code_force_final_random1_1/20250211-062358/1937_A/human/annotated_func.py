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
        
    #State: `t` is an integer such that \(1 \leq t \leq 10^4\), `n_cases` is an input integer, `i` is the total number of cases processed (equal to `n_cases`), `n` is the last input integer processed, and `power` is the final value determined based on the last `n` processed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`. For each `n`, if `n` is 1, it prints 1. Otherwise, it calculates the smallest power of 2 that is greater than or equal to `n` and prints that value. After processing all test cases, the function does not return any value.

