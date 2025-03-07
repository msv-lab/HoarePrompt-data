#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. Each test case consists of two lines: the first line contains an integer n such that 2 <= n <= 50, and the second line contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. There is at least one 1 in each test case.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: a sequence of integers, each representing the count of 0s between the first and last 1 for each of the t input arrays.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list of `n` binary integers (0s and 1s) with at least one 1. For each test case, it calculates and prints the number of 0s between the first and last occurrence of 1 in the list.

