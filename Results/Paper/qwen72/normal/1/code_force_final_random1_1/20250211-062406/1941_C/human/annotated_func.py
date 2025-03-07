#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `_` is `t - 1`, `a` is the last input integer where 1 ≤ a, `s` is the last input string, `x` is the number of times 'map' appears in the last `s`, `y` is the number of times 'pie' appears in the last `s`.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case consists of an integer `n` and a string `s` of length `n` containing lowercase Latin letters. For each test case, the function counts the occurrences of the substrings 'map' and 'pie' within `s` and prints the sum of these counts. After processing all test cases, the function has printed the sum of occurrences for each test case, and the final state of the program includes the total number of test cases processed, the last input integer `a`, the last input string `s`, and the counts of 'map' and 'pie' in the last `s`.

