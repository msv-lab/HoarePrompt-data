#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: t is an integer such that t = 0, a is the last integer value read from the user input, s is the last string value read from the user input, x is the number of times 'map' appears in the last s, y is the number of times 'pie' appears in the last s.
#Overall this is what the function does:The function reads multiple test cases from the user input. Each test case consists of an integer `n` and a string `s` of length `n`. For each test case, it counts the occurrences of the substrings 'map' and 'pie' in the string `s`, sums these counts, and prints the result.

