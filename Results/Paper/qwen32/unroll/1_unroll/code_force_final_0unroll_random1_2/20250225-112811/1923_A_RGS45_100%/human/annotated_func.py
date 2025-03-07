#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 2 <= n <= 50, and the second line contains n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. There is at least one a_i equal to 1 in each test case.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The output consists of `t` integers, each representing the count of '0's in the substring between the first and last '1' for each of the `t` test cases.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a string of `n` characters (each being either '0' or '1' with at least one '1' present). For each test case, it calculates and prints the number of '0's between the first and last '1' in the string.

