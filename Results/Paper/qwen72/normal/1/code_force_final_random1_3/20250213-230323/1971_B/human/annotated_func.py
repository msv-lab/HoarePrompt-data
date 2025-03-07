#State of the program right berfore the function call: t is an integer where 1 <= t <= 1000, and s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: `t` is an integer where 1 <= t <= 1000, `n` is an input integer, `i` is `n-1`, `s` is a new input string of length at most 10 consisting of lowercase English letters, `a` is a set containing the unique characters from the final `s`. If `len(a) == 2`, the set `a` contains exactly 2 unique characters. Otherwise, the number of unique characters in `a` is not equal to 2, `b` is a string formed by sorting the characters in the final `s` alphabetically, `c` is a string formed by sorting the characters in the final `s` in reverse alphabetical order. If the final `s` is already sorted in alphabetical order, then `s` is equal to `b`. Otherwise, `s` is not equal to `b`.
#Overall this is what the function does:The function reads an integer `n` indicating the number of test cases. For each test case, it reads a string `s` of lowercase English letters (up to 10 characters long). It checks if the string `s` contains exactly two unique characters. If so, it prints 'NO'. Otherwise, it prints 'YES' and then prints either the string `s` sorted in reverse alphabetical order or in alphabetical order, depending on whether `s` is already sorted in alphabetical order. After processing all test cases, the function completes without returning any value.

