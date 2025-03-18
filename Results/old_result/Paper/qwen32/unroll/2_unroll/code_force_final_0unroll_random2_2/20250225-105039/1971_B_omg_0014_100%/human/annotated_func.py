#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: the values of `t`, `n`, and the initial state of `s` remain unchanged. The output consists of printed lines for each test case based on the conditions described in the loop.
#Overall this is what the function does:The function reads an integer `n` representing the number of test cases. For each test case, it reads a string `s` and prints 'NO' if all characters in `s` are the same, otherwise it prints 'YES' and then prints the lexicographically smallest string if `s` is not already sorted, or the lexicographically largest string if `s` is sorted.

