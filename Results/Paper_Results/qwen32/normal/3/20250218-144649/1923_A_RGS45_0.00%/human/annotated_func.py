#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 2 <= n <= 50, and a list of n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. There is at least one 1 in the list for each test case.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: t is 0.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it takes an integer `n` and a binary string of length `n` (containing only 0s and 1s with at least one 1). It then counts and prints the number of 0s between the first and last occurrence of 1 in the string.

