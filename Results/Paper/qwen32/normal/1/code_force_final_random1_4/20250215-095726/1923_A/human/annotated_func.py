#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n is an integer such that 2 ≤ n ≤ 50, and a is a list of n integers where each element a_i is either 0 or 1. Additionally, in each test case, there is at least one element a_i equal to 1.
def func():
    t = int(input(''))
    for _ in range(t):
        n = int(input(''))
        
        arr = ''.join(input('').split())
        
        x = arr.find('1')
        
        y = arr[::-1].find('1')
        
        z = arr[x:n - y]
        
        print(z.count('0'))
        
    #State: t is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of binary digits (0s and 1s). For each test case, it calculates and prints the number of 0s between the first and last occurrence of the digit 1 in the list.

