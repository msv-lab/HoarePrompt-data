#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: t test cases have been processed, where for each test case, the number of occurrences of the substring 'map' followed by the number of occurrences of the substring 'pie' in the modified string (after removing all occurrences of 'map') have been printed. The variables `n`, `s`, `m`, and `p` are no longer in their initial state and their final values depend on the last test case processed. The variable `t` remains unchanged as it represents the number of test cases.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of a string `s` of length `n`. For each test case, it counts the number of occurrences of the substring 'map' in `s`, removes all occurrences of 'map' from `s`, and then counts the number of occurrences of the substring 'pie' in the modified string. It prints the sum of these two counts for each test case.

