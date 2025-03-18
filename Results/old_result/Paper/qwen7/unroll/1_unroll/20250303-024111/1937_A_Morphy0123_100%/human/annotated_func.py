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
        
    #State: Output State: The output state will consist of a series of numbers printed based on the input values for each case. For each input `n`, if `n` is 1, it will print 1. If `n` is a power of 2, it will print the next power of 2. Otherwise, it will print the current highest power of 2 less than `n`. The number of outputs will be equal to the value of `n_cases`.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer `n` (1 ≤ n ≤ 10^9). For each `n`, if `n` is 1, it prints 1. If `n` is a power of 2, it prints the next power of 2. Otherwise, it prints the highest power of 2 less than `n`. The function reads the number of test cases from user input and repeats the above process for each test case. After processing all test cases, it concludes without returning any value.

