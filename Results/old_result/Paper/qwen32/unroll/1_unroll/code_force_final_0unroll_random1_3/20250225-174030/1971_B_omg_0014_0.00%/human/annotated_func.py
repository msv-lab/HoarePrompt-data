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
        
    #State: t is an integer such that 1 ≤ t ≤ 1000, n is the same integer as the initial input, and s is the last string input during the loop.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads a string `s` of length at most 10 consisting of lowercase English letters. It then prints 'NO' if the string contains exactly two distinct characters, otherwise it prints 'YES' and then prints the lexicographically smaller of the string and its reverse if the string is not already in lexicographically smallest order.

