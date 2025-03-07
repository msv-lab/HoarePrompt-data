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
        
    #State: Output State: The output state consists of the count of '0's in the substring of `arr` from the first occurrence of '1' to the character just before the last occurrence of '1' when read from right to left, for each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t (number of test cases), an integer n (length of the binary string), and a binary string representing cells where 1 indicates a cell with a chip and 0 indicates an empty cell. For each test case, the function finds the substring between the first and last occurrences of '1' (when read from left to right and right to left respectively) and counts the number of '0's in this substring. The function then prints the count of '0's for each test case.

