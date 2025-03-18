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
        
    #State: The variable `t` will be equal to the number of iterations the loop has executed, which is the initial value of `t`. For each iteration, `n` will be an input integer, `arr` will be a string input from the user, `x` will be the index of the first occurrence of '1' in `arr` (or -1 if '1' is not found), `y` will be the index of the last occurrence of '1' in `arr` (or -1 if '1' is not found), and `z` will be a substring of `arr` starting from index `x` and ending at index `n - y - 1`. After all iterations, the final values of `n`, `arr`, `x`, `y`, and `z` will depend on the inputs provided during each iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a binary string \( arr \). It finds the indices of the first and last '1' in the string \( arr \), extracts a substring between these indices, and counts the number of '0's in this substring. The function prints the count of '0's for each test case and does not return any value.

