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
        
    #State: t is an integer such that 1 ≤ t ≤ 1000, i is equal to n-1, n must be greater than 0, s is the last input string provided, a is a set containing unique characters from s, b is a string that is the sorted version of s, and c is a string that is the sorted version of s but in descending order.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t` and a string `s`. For each test case, it checks if the string `s` contains more than one unique character. If `s` has only one unique character, it prints 'NO'. Otherwise, it prints 'YES' and then either the lexicographically smallest permutation of `s` or the lexicographically largest permutation of `s`, depending on whether `s` is already sorted in ascending order.

