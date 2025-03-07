#State of the program right berfore the function call: The function accepts no arguments but reads input from standard input. The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4) representing the number of test cases. Each of the next t lines contains a single integer n (1 ≤ n ≤ 10^9) representing the length of the array a.
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
        
    #State: - After processing all test cases, the only variables that have changed are `i` (the loop counter) and `n` (the current test case value).
    #   - The variable `power` is recalculated for each test case and does not persist beyond the current iteration.
    #   - The variable `n_cases` remains unchanged after the loop completes.
    #
    #The final state of the variables after the loop has finished executing all iterations is:
    #
    #- `i` will be equal to `n_cases` (since the loop runs from `0` to `n_cases - 1`).
    #- `n` will be the value of the last test case processed.
    #- `power` will be undefined or the value from the last iteration, but it is not relevant to the output state.
    #
    #The output state is described by the printed values for each test case, which are determined by the logic inside the loop.
    #
    #Output State:
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer `n`. For each `n`, it prints the largest power of 2 that is less than or equal to `n`.

