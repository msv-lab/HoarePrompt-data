#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 2 <= n <= 50, and the second line contains a list of n integers a_i where each a_i is either 0 or 1. There is at least one 1 in each test case's list.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The output state consists of `t` lines, each containing the count of '0's in the sub-string between the first and last '1' for each test case. The variables `t`, `n`, `arr`, `x`, `y`, and `z` do not retain their values after the loop completes.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list of `n` binary integers (each being either 0 or 1, with at least one 1 in each list). For each test case, it calculates and prints the count of '0's in the sub-string between the first and last '1' in the list.

