#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: The output state will consist of multiple lines of 'YES' or 'NO', followed by either the reverse sorted string or the sorted string of the input provided in each iteration of the loop. The exact content depends on the input provided for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` (where 1 ≤ t ≤ 1000) and a string `s` (consisting of lowercase English letters with a length of at most 10). For each test case, it checks if the number of unique characters in `s` is exactly 2. If true, it prints 'NO'. Otherwise, it prints 'YES' and then outputs either the lexicographically sorted string or its reverse, depending on which comes first alphabetically.

