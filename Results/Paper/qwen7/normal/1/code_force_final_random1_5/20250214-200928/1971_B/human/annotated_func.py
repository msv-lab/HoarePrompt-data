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
        
    #State: `t` is a positive integer such that 1 ≤ t ≤ 1000, `n` is an input integer greater than 0, `i` is equal to `n-1`, `s` is the last input string entered by the user, `a` is a set containing unique characters from `s`, `b` is a sorted string of `s`, and `c` is the sorted string of `s` in descending order.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a positive integer `n` followed by `n` strings `s`. For each string `s`, it checks if the number of unique characters is exactly 2. If so, it prints 'NO'. Otherwise, it prints 'YES' and then either the lexicographically smallest permutation of `s` or its reverse, depending on which comes first alphabetically.

