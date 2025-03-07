#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        z = s.count('mapie')
        
        print(x + y - z)
        
    #State: The loop has executed `t` times, and for each iteration `i` (from 1 to `t`), the value of `x + y - z` for the input string `s_i` has been printed, where `x` is the number of non-overlapping occurrences of 'map' in `s_i`, `y` is the number of non-overlapping occurrences of 'pie' in `s_i`, and `z` is the number of non-overlapping occurrences of 'mapie' in `s_i`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a string `s` of length `n`. For each test case, it calculates the number of non-overlapping occurrences of the substrings 'map' and 'pie' in `s`, subtracts the number of non-overlapping occurrences of the substring 'mapie', and prints the result.

