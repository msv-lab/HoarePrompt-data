#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 10^4), the number of test cases. Each of the following t lines contains a single integer n (1 ≤ n ≤ 10^9), representing the length of the array a.
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
        
    #State: `n_cases` is an integer representing the number of test cases, where 1 ≤ `n_cases` ≤ 10^4; `i` is equal to `n_cases` after all iterations have completed; for each of the `n_cases` iterations, the program has read an integer `n` from the input, and printed `2
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a single integer `n`. For each test case, it calculates and prints the largest power of 2 that is less than or equal to `n`.

