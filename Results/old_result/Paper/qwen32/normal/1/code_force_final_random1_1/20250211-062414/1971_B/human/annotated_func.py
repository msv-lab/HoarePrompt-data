#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    n = int(input())
    for i in range(n):
        s = input()
        
        a = set(s)
        
        if len(a) == 2:
            print('NO')
        else:
            print('YES')
            b = ''.join(sorted(s))
            c = ''.join(sorted(s, reverse=True))
            if b == s:
                print(c)
            else:
                print(b)
        
    #State: The loop has completed all `n` iterations, with `i` equal to `n`. The variables `t` and `n` remain unchanged. The string `s` and set `a` reflect the last iteration's input but do not persist beyond the loop.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads a string `s` of lowercase English letters. It checks if the string contains exactly two unique characters. If so, it prints 'NO'. Otherwise, it prints 'YES' and then prints the lexicographically smallest or largest version of the string, depending on whether the original string is already the smallest.

