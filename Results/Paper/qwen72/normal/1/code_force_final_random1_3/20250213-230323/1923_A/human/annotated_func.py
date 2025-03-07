#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, representing the number of test cases. For each test case, n is an integer such that 2 <= n <= 50, representing the number of cells. a is a list of n integers where each integer is either 0 or 1, representing whether the cell is free (0) or contains a chip (1). At least one cell contains a chip in each test case.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: _ is t-1, t is greater than or equal to 1, n is an input integer, arr is a string containing the final input with all spaces removed, x is the index of the first occurrence of '1' in the final arr or -1 if '1' is not found, y is the index of the first occurrence of '1' in the reversed string of the final arr or -1 if '1' is not found, z is the substring of the final arr starting from index x and ending at index n - y - 1.
#Overall this is what the function does:The function `func` reads a series of test cases. Each test case consists of an integer `n` (2 ≤ n ≤ 50) and a list of `n` integers (0 or 1), representing cells that are either free (0) or contain a chip (1). For each test case, the function identifies the segment of the list that starts from the first cell containing a chip to the last cell containing a chip. It then counts the number of free cells (0s) within this segment and prints this count. After processing all test cases, the function completes without returning any value.

