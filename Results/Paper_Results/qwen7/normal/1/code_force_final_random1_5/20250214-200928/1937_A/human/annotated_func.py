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
        
    #State: After all iterations of the loop have finished, `n_cases` will be 0, and `i` will be equal to the final value it took after the last iteration. The variable `power` will either be equal to `n_cases` or `power - 1`, and `n` will be an input integer. If `n` equals 1, then `power` remains unchanged. Otherwise, `power` is set to `n_cases` and `i` is set to `n_cases + 1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`. For each `n`, if `n` is 1, it prints 1. Otherwise, it calculates the smallest power of 2 that is greater than or equal to `n` and prints that power. After processing all test cases, it implicitly ends without returning any value.

