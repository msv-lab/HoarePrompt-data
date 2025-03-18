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
        
    #State: t is an integer such that 1 <= t <= 1000, s is a string of length at most 10 consisting of lowercase English letters, n is an input integer.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, indicating the number of test cases. For each test case, it reads a string `s` of lowercase English letters with a maximum length of 10. If the string `s` contains exactly two distinct characters, it prints 'NO'. If the string `s` contains more than two distinct characters, it prints 'YES' and then prints the lexicographically smallest and largest versions of the string `s`, depending on whether the sorted string `s` is equal to the original string `s`. The function does not return any value. After the function concludes, `t` remains an integer within the range 1 to 1000, and `s` is a string of lowercase English letters with a maximum length of 10.

