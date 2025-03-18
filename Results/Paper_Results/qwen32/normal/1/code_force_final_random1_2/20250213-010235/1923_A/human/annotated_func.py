#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and the second line contains a list of n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. In each test case, there is at least one a_i equal to 1.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The loop has terminated after processing `t` test cases. The variables `n`, `arr`, `x`, `y`, and `z` reflect the state of the last test case processed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of binary integers (0s and 1s). For each test case, it calculates the number of 0s between the first and last occurrence of the integer 1 in the list and prints this count.

