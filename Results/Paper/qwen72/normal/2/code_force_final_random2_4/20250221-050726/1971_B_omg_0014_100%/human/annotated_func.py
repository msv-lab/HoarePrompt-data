#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    n = int(input())
    for i in range(n):
        s = input()
        
        a = set(s)
        
        if len(a) == 1:
            print('NO')
        else:
            print('YES')
            b = ''.join(sorted(s))
            c = ''.join(sorted(s, reverse=True))
            if b == s:
                print(c)
            else:
                print(b)
        
    #State: `t` is an integer such that 1 <= t <= 1000, `n` is the same as the initial value, `i` is `n-1`, `a` is a set containing the unique characters from the last input `s`. If the length of `a` is 1, `b` and `c` are undefined. Otherwise, `b` is a string containing the characters from the last input `s` sorted in ascending order, and `c` is a string containing the characters from the last input `s` sorted in descending order. If the last input `s` is equal to `b`, then `s` remains unchanged. Otherwise, `s` is not equal to `b`, and `s` is now the last user input.
#Overall this is what the function does:The function processes a series of test cases, where the number of test cases `t` is an integer (1 <= t <= 1000). For each test case, it reads a string `s` of length at most 10 consisting of lowercase English letters. If the string `s` contains only one unique character, it prints 'NO'. Otherwise, it prints 'YES' followed by either the string `s` sorted in descending order (if `s` is already sorted in ascending order) or the string `s` sorted in ascending order. After processing all test cases, the function does not return any value, and the final state includes the processed test cases and their respective outputs.

