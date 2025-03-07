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
        
    #State: `t` is an integer such that 1 ≤ t ≤ 1000, `n` is the number of iterations, `i` is equal to `n`, `s` is the last string processed, `a` is the set of unique characters from the last string `s`, `b` is the last string `s` sorted in ascending order, and `c` is the last string `s` sorted in descending order.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a string of lowercase English letters. For each string, it checks if the string contains exactly two unique characters. If it does, it outputs 'NO'. Otherwise, it outputs 'YES' and then prints the lexicographically smallest or largest version of the string, depending on whether the original string is already in lexicographically smallest order.

