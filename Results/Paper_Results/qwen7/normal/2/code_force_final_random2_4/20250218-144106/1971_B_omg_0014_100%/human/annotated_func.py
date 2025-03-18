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
        
    #State: `t` is a positive integer such that 1 ≤ t ≤ 1000, `i` is 3, `n` must be greater than 3, `a` is a set containing the unique characters of `s`, `b` is the sorted version of `s`, and `c` is a string containing the characters of `s` sorted in descending order.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `t` and a string `s`. For each test case, it checks if the string `s` contains only one unique character. If it does, it prints 'NO'. Otherwise, it prints 'YES', followed by either the lexicographically smallest permutation of `s` or its reverse, depending on which comes first alphabetically.

