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
        
    #State: t remains an integer such that 1 <= t <= 1000, s is a string of length at most 10 consisting of lowercase English letters, n is an input integer.
#Overall this is what the function does:The function `func` reads an integer `n` from the user, where `1 <= n <= 1000`. It then reads `n` strings, each of which is a string of lowercase English letters with a maximum length of 10. For each string, it checks if the string contains exactly two distinct characters. If it does, the function prints 'NO'. If the string contains more than two distinct characters, it prints 'YES' and then prints the string in sorted order. If the string is already sorted in non-decreasing order, it prints the string in reverse sorted order; otherwise, it prints the string in sorted order. The function does not return any value.

