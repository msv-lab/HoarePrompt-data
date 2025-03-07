#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 100, and s is a string of length n containing only the characters "U" and "D".
def func():
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if arr.count('U') % 2 == 1:
            results.append('yes')
        else:
            results.append('no')
        
    #State: `results` is a list of length `t` containing 'yes' or 'no' based on whether the count of 'U' in each string `s` is odd or even respectively.
    for i in results:
        print(i)
        
    #State: `results` is a list of length `t` containing 'yes' or 'no' based on whether the count of 'U' in each string `s` is odd or even respectively.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` containing only 'U' and 'D'. It then determines if the count of 'U' in the string `s` is odd, appending 'yes' to the results if it is, and 'no' if it is not. Finally, it prints 'yes' or 'no' for each test case based on this condition.

