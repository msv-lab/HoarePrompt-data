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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `s` is a new input string of length at most 10 consisting of lowercase English letters, `n` is the original input integer, `i` is `n-1`, `a` is a set containing the unique characters from the last input string `s`. If `len(a) == 1`, the set `a` contains exactly one unique character. If `len(a) > 1`, `b` is a string containing the characters of the last input string `s` sorted in ascending order, and `c` is a string containing the characters of the last input string `s` sorted in descending order. If the last input string `s` is already sorted in ascending order (`b == s`), then `s` remains unchanged. Otherwise, `s` is not equal to `b`, and `b` is now a string containing the characters of `s` sorted in ascending order.
#Overall this is what the function does:The function `func` processes a series of up to 1000 test cases, where each test case involves a string `s` of lowercase English letters with a maximum length of 10. For each test case, the function checks if the string `s` contains more than one unique character. If the string contains only one unique character, it prints 'NO'. If the string contains more than one unique character, it prints 'YES' followed by either the string `s` sorted in descending order (if `s` is already sorted in ascending order) or the string `s` sorted in ascending order (if `s` is not already sorted in ascending order). After processing all test cases, the function completes, and the final state includes the printed results for each test case.

