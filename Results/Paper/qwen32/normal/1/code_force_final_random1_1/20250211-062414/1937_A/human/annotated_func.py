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
        
    #State: `i` is equal to `n_cases`, `t` remains unchanged, and `n_cases` remains unchanged.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and prints the largest power of 2 that is less than or equal to `n`.

