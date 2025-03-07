#State of the program right berfore the function call: t is an integer such that 1 <= t <= 1000, and for each of the t test cases, s is a string of length at most 10 consisting of lowercase English letters.
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
        
    #State: `t` is an integer such that 1 <= t <= 1000, `n` is the number of iterations the loop has completed, `i` is `n-1`, and for each iteration, `s` was a string input by the user. For each `s`, `a` was a set containing unique characters from `s`. If the length of `a` was 1, the program printed 'NO'. If the length of `a` was greater than 1, the program printed 'YES', and then it printed either the sorted version of `s` in ascending order or in descending order, depending on whether `s` was already sorted in ascending order.
#Overall this is what the function does:The function reads an integer `n` indicating the number of test cases, where `1 <= n <= 1000`. For each test case, it reads a string `s` of length at most 10 consisting of lowercase English letters. It checks if all characters in `s` are the same. If so, it prints 'NO'. Otherwise, it prints 'YES' followed by the lexicographically smallest or largest permutation of `s`, depending on whether `s` is already in ascending order. The function does not return any value; it only prints the results to the console. After processing all test cases, the function completes, and the program state reflects the number of test cases processed and the output printed for each case.

