#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: For each of the `t` test cases, the program will print 'NO' if the string `s` contains exactly two distinct characters, otherwise it will print 'YES'. If 'YES' is printed, it will also print the lexicographically smallest or largest version of the string `s`, depending on whether `s` is already in lexicographically smallest order or not. The values of `t`, `n`, and the initial strings `s` remain unchanged.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a string of lowercase English letters. For each string, it checks if the string contains exactly two distinct characters. If it does, the function outputs 'NO'. Otherwise, it outputs 'YES' and then prints either the lexicographically smallest or largest version of the string, depending on whether the string is already in lexicographically smallest order.

