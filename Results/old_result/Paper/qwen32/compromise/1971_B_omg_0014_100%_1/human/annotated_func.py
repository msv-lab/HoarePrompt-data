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
        
    #State: The output state consists of printed results for each iteration of the loop, with each result being either 'NO' or 'YES' followed by the sorted or reverse sorted string `s` if 'YES' was printed. The variables `t` and `n` remain unchanged.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string of lowercase English letters. For each string, it determines if the string contains more than one unique character. If it does, the function outputs 'YES' followed by the lexicographically smallest or largest version of the string, depending on whether the string is already in lexicographically smallest order. If the string contains only one unique character, it outputs 'NO'.

