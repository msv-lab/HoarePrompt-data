#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: Output State: The output state will consist of multiple lines of text, each line being either 'YES' followed by either the lexicographically smallest string or its reverse, or 'NO'. The number of these lines will be equal to the value of `n`. For each iteration `i` from `0` to `n-1`, the program reads a string `s` from input. If the string `s` contains all unique characters, it prints 'NO'. Otherwise, it prints 'YES' followed by either the lexicographically smallest permutation of `s` or its reverse, whichever comes first when sorted normally.
#Overall this is what the function does:The function processes `n` test cases, where `n` is read from input. For each test case, it reads a string `s` and checks if all characters in `s` are unique. If they are, it prints 'NO'. Otherwise, it prints 'YES' followed by either the lexicographically smallest permutation of `s` or its reverse, whichever comes first when sorted normally. The function does not return any value but outputs the results for each test case.

