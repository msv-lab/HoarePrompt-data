#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000. For each test case, n is an integer such that 2 <= n <= 50, and a list of n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. At least one a_i is 1 in each test case.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = str(input(''))
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: `t` is an integer such that `t` is 0, `n` is the last input integer provided by the user, `arr` is the last string input provided by the user, `x` is the index of the first occurrence of '1' in `arr` or -1 if '1' is not found, `y` is the index of the first occurrence of '1' in the reversed string `arr` or -1 if '1' is not found, `z` is `arr[x:n - y]` if `x` is not -1, otherwise `z` is an empty string.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a string of `n` characters (each character is either '0' or '1'). For each test case, it calculates the number of '0's between the first and last occurrence of '1' in the string and prints this count.

