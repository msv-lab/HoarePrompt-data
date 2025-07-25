#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 10^6, representing the length of the string s, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: _ is a placeholder, `t` is an integer where 1 ≤ t ≤ 10^4, `a` is an input integer, `s` is a new input string, `x` is the number of times 'map' appears in the new `s`, `y` is the number of times 'pie' appears in the new `s`. This state repeats for each of the `t` test cases, with `a` and `s` being re-initialized for each iteration. After all iterations, the loop has printed the sum of occurrences of 'map' and 'pie' for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case involves reading an integer `a` (though it is not used in the function) and a string `s`. The function counts the number of occurrences of the substrings 'map' and 'pie' within `s` and prints the sum of these counts. After processing all test cases, the function has printed the sum of occurrences of 'map' and 'pie' for each test case. The function does not return any value.

