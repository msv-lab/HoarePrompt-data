#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and each string s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `n` is an integer greater than or equal to 0, `i` is equal to `n`, and for each iteration `i` from 0 to `n-1`, `s` was an input string of length at most 10 consisting of lowercase English letters. For each `s`, `a` was a set containing the unique characters from `s`. If `len(a) == 2`, then `a` contained exactly 2 unique characters, and 'NO' was printed. Otherwise, `a` contained a number of unique characters not equal to 2, `b` was a sorted string of `s`, and `c` was a string containing the characters of `s` sorted in descending order. If `b` (the sorted version of `s`) was equal to `s`, then `s` was already sorted in ascending order, and `c` was printed. Otherwise, `b` was printed.
#Overall this is what the function does:The function reads an integer `n` indicating the number of test cases, followed by `n` strings `s` of lowercase English letters, each of length at most 10. For each string `s`, it checks if the string contains exactly two unique characters. If so, it prints 'NO'. Otherwise, it prints 'YES', followed by either the string sorted in descending order (if the original string was already sorted in ascending order) or the string sorted in ascending order. The function does not return any value; its primary action is to process the input and print the results.

