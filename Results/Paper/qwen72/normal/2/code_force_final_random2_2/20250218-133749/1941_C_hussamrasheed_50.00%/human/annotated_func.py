#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 10^6, representing the length of the string s, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: After all iterations, `t` is the same as the initial value, `i` is `t - 1`, `n` is the last input integer, `s` is the last input string with all occurrences of 'map' removed, `m` is the number of times 'map' appeared in the last `s`, and `p` is the number of times 'pie' appears in the last `s`.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. Each test case consists of an integer `n` and a string `s` of length `n`. The function counts the occurrences of the substring 'map' in `s`, removes all occurrences of 'map' from `s`, and then counts the occurrences of the substring 'pie' in the modified string. It prints the sum of these two counts for each test case. After processing all test cases, the function has no return value, but the state of the program includes the original number of test cases `t`, the last processed integer `n`, the last processed string `s` with all 'map' substrings removed, the count of 'map' in the last `s`, and the count of 'pie' in the last modified `s`.

