#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100, for each test case n is an integer such that 1 ≤ n ≤ 100, and s is a string of length n consisting only of the characters "U" and "D".
def func():
    t = int(input())
    results = []
    for i in range(t):
        n = int(input())
        
        arr = input()
        
        if n % 2 == 0:
            results.append('no')
        elif arr.count('U') > arr.count('D'):
            results.append('yes')
        else:
            results.append('no')
        
    #State: `results` is a list of length `t` where each element is either `'yes'` or `'no'`, determined by the conditions of each test case.
    for i in results:
        print(i)
        
    #State: `results` is a list of length `t` where `t` is at least 1, and each element is either `'yes'` or `'no'`. The loop has printed each element of `results` exactly once.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a string `s` of length `n` containing only 'U' and 'D'. For each test case, it checks if the length of the string `n` is odd and if the count of 'U' in the string is greater than the count of 'D'. If both conditions are met, it outputs 'yes'; otherwise, it outputs 'no'.

