#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. Each test case consists of an integer n such that 1 ≤ n ≤ 100, followed by a string s of length n containing only the characters 'U' and 'D'.
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
        
    #State: `results` is a list of `t` elements, each being either `'yes'` or `'no'` based on the conditions of each test case.
    for i in results:
        print(i)
        
    #State: `results` is a list with `t` elements, and each element is either `'yes'` or `'no'`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string of 'U' and 'D' characters. It determines if the number of 'U' characters is greater than the number of 'D' characters in strings of odd lengths, appending 'yes' to the results if true, otherwise 'no'. For even-length strings, it appends 'no'. Finally, it prints the results for each test case.

