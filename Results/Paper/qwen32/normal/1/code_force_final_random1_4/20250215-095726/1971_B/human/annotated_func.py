#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each of the t test cases, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: The loop has completed `n` iterations, processing each input string `s` and printing the appropriate results based on the conditions.
#Overall this is what the function does:The function processes a series of test cases, where each test case consists of a string of lowercase English letters. For each string, it determines if the string contains more than two unique characters. If it does, the function prints 'YES' followed by the lexicographically smallest or largest permutation of the string, depending on whether the original string is already the smallest permutation. If the string contains exactly two unique characters, it prints 'NO'.

