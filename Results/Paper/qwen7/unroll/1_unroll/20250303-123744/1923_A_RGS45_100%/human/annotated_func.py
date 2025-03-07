#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and the second line contains a list of n integers a_1, a_2, ..., a_n where each a_i is either 0 or 1. Additionally, in each test case, at least one a_i is equal to 1.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: The count of '0's between the first and last occurrence of '1' (inclusive of the '1's) for each input string in the loop, for all t inputs.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer t and a list of n binary digits (0s and 1s). For each test case, it finds the substring between the first and last occurrence of '1', inclusive, and counts the number of '0's in this substring. It then prints the count for each test case.

