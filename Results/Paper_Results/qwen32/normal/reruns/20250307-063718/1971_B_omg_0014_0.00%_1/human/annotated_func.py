#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `s` is the string input by the user during the last iteration of the loop, `n` is the number of iterations which has been exhausted (i.e., `i` has reached `n`), and no further changes are made to `t`, `n`, or `s` after the loop ends.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string `s` of lowercase English letters. It then determines if the string has more than two distinct characters. If it does, the function outputs 'YES' followed by the lexicographically smallest or largest string, whichever is not the original string. If the string has exactly two distinct characters, it outputs 'NO'.

