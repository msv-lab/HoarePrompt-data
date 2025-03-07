#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000; for each test case, n is an integer such that 2 ≤ n ≤ 50; the second line of each test case contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1, indicating whether the i-th cell is free (0) or contains a chip (1); in each test case, at least one cell contains a chip.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: t is an integer between 1 and 1000 inclusive. For each iteration i from 0 to t-1, n_i is an integer, arr_i is a string without spaces, x_i is the index of the first '1' in arr_i, y_i is the index of the first '1' from the reverse of arr_i, and z_i is a substring of arr_i from x_i to n - y_i (inclusive), where n is the length of arr_i. The value of z_i is the count of '0's in z_i.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` representing the number of test cases, followed by `t` lines, each containing an integer `n` and a binary string of length `n`. The function then finds the first and last positions of '1' in the string, extracts the substring between these positions, and counts the number of '0's in this substring. The function prints the count of '0's for each test case.

