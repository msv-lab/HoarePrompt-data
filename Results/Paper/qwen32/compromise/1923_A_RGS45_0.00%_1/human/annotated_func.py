#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 2 <= n <= 50, and the second line contains a list of n integers where each integer is either 0 or 1. There is at least one 1 in each test case's list.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: 
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string of `n` characters (each being either '0' or '1') with at least one '1'. It then calculates and prints the number of '0's between the first and last occurrence of '1' in the string.

