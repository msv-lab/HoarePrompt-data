#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 2 ≤ n ≤ 50; the second line of each test case contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1, indicating whether the i-th cell is free (0) or contains a chip (1); in each test case, at least one cell contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: t is an integer between 0 and 1 inclusive, `n` is the input integer from the user, `arr` is the final string input from the user after all iterations, `x` is the index of the first occurrence of '1' in `arr`, or -1 if '1' is not found, `y` is the index of the last occurrence of '1' in the reversed `arr`, `z` is a substring of `arr` starting from index `x` and ending just before the index `n - y` after all iterations have completed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t`, followed by an integer `n` and a string `arr` consisting of `n` characters, each being '0' or '1'. It then finds the indices of the first and last '1' in `arr`. Using these indices, it extracts a substring `z` from `arr`. Finally, it counts and prints the number of '0's in `z`.

