#State of the program right berfore the function call: The function `func` is expected to be called with parameters in a context where the first parameter is a single integer `t` (1 ≤ t ≤ 10^4) representing the number of test cases, and for each test case, the first line contains an integer `n` (1 ≤ n ≤ 10^6) representing the length of the string `s`, and the next line contains the string `s` of length `n` consisting of lowercase Latin letters. The sum of `n` over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: The variable `t` remains unchanged, and the loop has printed the sum of the counts of the substrings 'map' and 'pie' for each of the `t` test cases. The variables `n`, `s`, `m`, and `p` are no longer in scope after the loop finishes executing.
#Overall this is what the function does:The function `func` processes a series of test cases. It reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n` consisting of lowercase Latin letters. It counts the occurrences of the substrings 'map' and 'pie' in `s`, removes all occurrences of 'map' from `s`, and then prints the sum of the counts of 'map' and 'pie' for each test case. After processing all test cases, the function does not return any value, and the variables `n`, `s`, `m`, and `p` are no longer in scope. The variable `t` remains unchanged.

