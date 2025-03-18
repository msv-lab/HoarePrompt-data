#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, for each test case n is an integer such that 1 <= n <= 100, and s is a string of length n containing only "U" and "D".
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
        
    #State: `results` is a list of length `t` where each element is either `'yes'` or `'no'`, determined by the rules specified in the loop.
    for i in results:
        print(i)
        
    #State: all elements of the `results` list have been printed, and `results` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string `s` of length `n` containing only "U" and "D". For each test case, it determines if the number of "U" characters is greater than the number of "D" characters only when `n` is odd. If so, it outputs "yes"; otherwise, it outputs "no".

