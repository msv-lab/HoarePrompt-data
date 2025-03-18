#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, each test case consists of an integer n such that 1 ≤ n ≤ 10^6, and a string s of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: For each test case, the number of occurrences of the substring 'map' plus the number of occurrences of the substring 'pie' in the string `s` after all 'map' occurrences have been removed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n`. It then counts the occurrences of the substring 'map' in `s`, removes all occurrences of 'map' from `s`, and counts the occurrences of the substring 'pie' in the modified string. Finally, it prints the sum of these two counts for each test case.

