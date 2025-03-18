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
        
    #State: `t` is an integer between 1 and 998, `_` is `t-1`, `n` is the integer input by the user in the last iteration, `arr` is the string input by the user in the last iteration, `x` is the index of the first occurrence of '1' in `arr` or -1 if '1' is not found, `y` is the index of the last occurrence of '1' in `arr` or -1 if '1' is not found, `z` is a substring from `arr[x]` to `arr[n - y - 1]` if both `x` and `n - y` are valid indices, otherwise `z` is an empty string.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer t, followed by t pairs of integers n and a string arr. For each pair, it finds the first and last positions of '1' in arr, extracts the substring between these positions, and counts the number of '0's in this substring. It then prints the count for each test case.

