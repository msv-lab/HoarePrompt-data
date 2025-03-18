#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: `t` is 0; `a` is the integer value provided by the user input for the last test case; `s` is the string provided by the user for the last test case; `x` is the number of non-overlapping occurrences of 'map' in the last `s`; `y` is the number of non-overlapping occurrences of 'pie' in the last `s`; `z` is the number of non-overlapping occurrences of 'mapie' in the last `s`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of an integer `n` and a string `s` of length `n`. For each test case, it calculates the number of non-overlapping occurrences of the substrings 'map' and 'pie' in `s`, and subtracts the number of non-overlapping occurrences of 'mapie'. It then prints the result for each test case.

