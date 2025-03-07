#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `s` is a new input string of length at most 10 consisting of lowercase English letters, `n` is the input integer, `i` is `n-1`, `a` is a set containing the unique characters from the last input string `s`, `b` is the string `s` sorted in ascending order, `c` is the string `s` sorted in descending order. If the length of `a` (the set of unique characters in `s`) is 2, the loop prints 'NO' for this iteration. Otherwise, the loop prints 'YES', and if `s` is equal to `b`, it prints `c`; otherwise, it prints `b`.
#Overall this is what the function does:The function reads an integer `n` indicating the number of test cases. For each test case, it reads a string `s` of length at most 10 consisting of lowercase English letters. It checks if the string `s` contains exactly two unique characters. If so, it prints 'NO'. Otherwise, it prints 'YES', followed by either the string `s` sorted in descending order (if `s` is already sorted in ascending order) or the string `s` sorted in ascending order. After processing all test cases, the function terminates.

