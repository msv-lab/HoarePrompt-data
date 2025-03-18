#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer `n` (2 ≤ n ≤ 50) representing the number of cells in the ribbon, and a list of integers `a` of length `n` where each element is either 0 (free cell) or 1 (cell with a chip). Additionally, at least one cell in each test case contains a chip. The function should be able to process a list of such test cases, where the number of test cases `t` is an integer (1 ≤ t ≤ 1000).
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: `_` is `t - 1`, `t` must be greater than 0, `n` is the last input integer, `arr` is the last input string, `x` is the index of the first occurrence of '1' in `arr` or -1 if '1' is not found, `y` is the index of the first occurrence of '1' in the reversed `arr` or -1 if '1' is not found, `z` is the substring of `arr` from index `x` to index `n - y - 1` (inclusive).
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case consists of an integer `n` (2 ≤ n ≤ 50) representing the number of cells in a ribbon, and a string `arr` of length `n` where each character is either '0' (free cell) or '1' (cell with a chip). The function outputs the number of free cells ('0') between the first and last chip ('1') in each ribbon, inclusive. The function does not return any value; it prints the result for each test case. After the function concludes, the state of the program is such that all test cases have been processed, and the results have been printed to the console.

