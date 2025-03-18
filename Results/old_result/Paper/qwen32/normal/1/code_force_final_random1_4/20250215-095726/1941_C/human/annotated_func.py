#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 10^6, and s is a string of length n consisting of lowercase Latin letters. The sum of n over all test cases does not exceed 10^6.
def func():
    for _ in range(int(input())):
        a = int(input())
        
        s = input()
        
        x = s.count('map')
        
        y = s.count('pie')
        
        print(x + y)
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4; the loop has executed exactly `t` times; for each of the `t` iterations, an integer `a` was input, followed by a string `s` of length `n` consisting of lowercase Latin letters; for each string `s`, `x` is the count of occurrences of 'map' in `s`, and `y` is the count of occurrences of 'pie' in `s`; the program has printed the sum of `x` and `y` for each iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a string `s` of length `n`. It then counts the occurrences of the substrings 'map' and 'pie' in `s` and prints the sum of these counts.

