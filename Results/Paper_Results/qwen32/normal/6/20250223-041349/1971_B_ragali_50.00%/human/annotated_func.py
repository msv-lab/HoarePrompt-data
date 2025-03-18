#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
def func():
    t = int(input().strip(' '))
    for i in range(t):
        s = input().strip(' ')
        
        a = set()
        
        for i in s:
            a.add(i)
        
        if len(a) > 1:
            print('YES')
            newstr = s[len(s) // 2:] + s[:len(s) // 2]
            isreverse = s[::-1]
            if newstr != s:
                print(s[len(s) // 2:] + s[:len(s) // 2])
            elif isreverse != s:
                print(isreverse)
            else:
                print(s[len(s) // 2:] + s[0:len(s) // 2])
        else:
            print('NO')
        
    #State: The loop has executed `t` times, where `t` is the initial integer input. For each of the `t` iterations, the program reads a string `s` from the input, checks if the string consists of more than one unique character, and prints 'YES' if it does. If `s` has more than one unique character, the program then checks if `s` is a palindrome. If `s` is not a palindrome, it prints the string formed by concatenating the second half of `s` with the first half. If `s` is a palindrome, it prints the reverse of `s`. If `s` consists of only one unique character, the program prints 'NO'.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string `s` of length at most 10 consisting of lowercase English letters. If the string `s` contains more than one unique character, it prints 'YES' and then prints a modified version of the string based on whether it is a palindrome or not. If the string `s` contains only one unique character, it prints 'NO'.

