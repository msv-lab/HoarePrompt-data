#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `s` is the last input string, `n` is the number of iterations.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases, then for each test case, it reads a string `s`. It checks if all characters in the string are the same. If they are, it prints 'NO'. Otherwise, it prints 'YES' and then prints the lexicographically smallest string that can be formed from `s` if `s` is not already sorted; otherwise, it prints the lexicographically largest string.

