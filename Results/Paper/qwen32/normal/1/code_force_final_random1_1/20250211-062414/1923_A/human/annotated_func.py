#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and the second line contains n integers a_i where each a_i is either 0 or 1. Additionally, in each test case, there is at least one a_i equal to 1.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: the count of '0's in the substring `z` from the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a list of binary integers (0s and 1s). For each test case, it calculates and prints the number of 0s between the first and last occurrence of 1 in the list.

