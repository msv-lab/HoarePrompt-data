#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: For each test case, the output is the number of times the substring 'map' or 'pie' appears in the string s, but not counting the occurrences where 'mapie' appears as a substring. The state of t, n, and s after all iterations is unchanged except that each test case has been processed and its result printed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string `s` of length `n`. For each test case, it calculates and prints the number of times the substrings 'map' or 'pie' appear in `s`, excluding the occurrences where 'mapie' appears as a substring.

