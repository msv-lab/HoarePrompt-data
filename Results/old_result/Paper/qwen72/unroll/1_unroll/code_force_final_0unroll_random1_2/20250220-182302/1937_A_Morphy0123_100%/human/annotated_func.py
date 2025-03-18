#State of the program right berfore the function call: The function does not take any input parameters, but based on the problem description, it is implied that the function should be called with a parameter n, where n is an integer such that 1 ≤ n ≤ 10^9.
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
        
    #State: The loop will print the largest power of 2 less than or equal to each input `n` for `n_cases` iterations. The variable `n_cases` will remain unchanged, and the variable `n` will be the last input value processed by the loop. The variable `power` will be the exponent of the largest power of 2 less than or equal to the last input `n`.
#Overall this is what the function does:The function reads an integer `n_cases` from the input, indicating the number of test cases. For each test case, it reads another integer `n` (1 ≤ n ≤ 10^9) and prints the largest power of 2 less than or equal to `n`. After processing all test cases, the function does not return any value. The variable `n_cases` remains unchanged, and the variable `n` will be the last input value processed. The variable `power` will be the exponent of the largest power of 2 less than or equal to the last input `n`.

