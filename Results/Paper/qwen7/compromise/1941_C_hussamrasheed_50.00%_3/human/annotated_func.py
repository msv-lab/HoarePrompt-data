#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 10^6, and the string s consists of lowercase Latin letters with a total length sum not exceeding 10^6.
def func():
    t = int(input())
    for i in range(t):
        n = int(input())
        
        s = input()
        
        m = s.count('map')
        
        s = s.replace('map', '')
        
        p = s.count('pie')
        
        print(m + p)
        
    #State: Output State: The value of `t` integers, each representing the sum of the counts of 'map' and 'pie' in the corresponding string `s` after replacing all occurrences of 'map' with an empty string.
#Overall this is what the function does:The function processes a series of test cases, each containing a positive integer `t` and a string `s`. For each test case, it counts the occurrences of the substring 'map' in `s`, removes all instances of 'map' from `s`, counts the occurrences of the substring 'pie' in the modified `s`, and prints the sum of these two counts for each test case. After processing all test cases, it outputs `t` integers, each representing the sum of counts of 'map' and 'pie' for the corresponding input string `s`.

