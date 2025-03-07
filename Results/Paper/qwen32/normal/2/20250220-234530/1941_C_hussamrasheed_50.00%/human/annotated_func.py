#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: `t` is an input integer such that 1 ≤ t ≤ 10^4; All test cases have been processed; `i` is equal to `t`, indicating that the loop has completed all iterations; No more input values for `n` or `s` are read; The final results for each test case (sum of `m` and `p`) have been printed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n`. It counts the occurrences of the substring 'map' in `s`, removes all occurrences of 'map' from `s`, and then counts the occurrences of the substring 'pie' in the modified string. Finally, it prints the sum of these two counts for each test case.

