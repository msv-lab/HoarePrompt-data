#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each of the t test cases, n is an integer such that 1 ≤ n ≤ 10^9.
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
        
    #State: After processing all `t` test cases, the program will have printed a series of integers corresponding to the results of each test case. Each printed integer is either 1 (if `n` was 1) or the largest power of 2 less than or equal to `n` (if `n` was greater than 1).
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n`. For each test case, it prints `1` if `n` is `1`, otherwise, it prints the largest power of 2 that is less than or equal to `n`.

