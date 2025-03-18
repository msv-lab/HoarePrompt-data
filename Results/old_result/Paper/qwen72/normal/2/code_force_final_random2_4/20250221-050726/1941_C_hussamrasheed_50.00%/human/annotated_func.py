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
        
    #State: `t` is an input integer where 1 ≤ t ≤ 10^4, `i` is `t-1`, `n` is an input integer, `s` is the final input string with all occurrences of 'map' removed, `m` is the number of times 'map' appeared in the original `s` for the last test case, `p` is the number of times 'pie' appears in the final `s`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n`. It then counts the occurrences of the substring 'map' in `s`, removes all instances of 'map' from `s`, and counts the occurrences of the substring 'pie' in the modified string. Finally, it prints the sum of the counts of 'map' and 'pie' for each test case. After processing all test cases, the function has no return value, but the state includes `t` (the number of test cases), `i` (the index of the last test case processed, which is `t-1`), `n` (the length of the last input string), `s` (the last input string with all occurrences of 'map' removed), `m` (the count of 'map' in the original last input string), and `p` (the count of 'pie' in the modified last input string).

