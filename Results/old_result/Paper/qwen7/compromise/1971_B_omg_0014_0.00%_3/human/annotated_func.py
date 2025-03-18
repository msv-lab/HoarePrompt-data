#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: The output will consist of 'YES' or 'NO' for each iteration based on whether the length of the set of characters in the input string `s` is 2 or not. If the length is not 2, it prints 'YES' followed by either the lexicographically sorted string or its reverse, depending on which comes first. If the length is 2, it directly prints 'NO'. The exact strings printed depend on the inputs provided during each iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` (number of test cases) and a string `s` (of length at most 10 consisting of lowercase English letters). For each test case, it checks if the number of unique characters in `s` is 2. If true, it prints 'NO'. Otherwise, it prints 'YES' followed by either the lexicographically sorted version or the reverse sorted version of `s`, whichever comes first.

