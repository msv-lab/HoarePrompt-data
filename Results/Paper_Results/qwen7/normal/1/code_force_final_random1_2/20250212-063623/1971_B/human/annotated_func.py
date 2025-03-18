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
        
    #State: The loop has executed all its iterations, with `t` being a positive integer such that \(1 \leq t \leq 1000\), `n` being the total number of iterations the loop was set to run, `i` being equal to `n - 1` (since the loop runs from `0` to `n-1`), `s` being the last input string provided, `a` being a set containing the unique characters from `s`, and `b` and `c` being strings representing the sorted and reverse-sorted versions of `s`, respectively.
#Overall this is what the function does:The function processes a series of test cases, each consisting of a positive integer `t` followed by `t` strings `s`. For each string `s`, it checks if the string contains exactly two unique characters. If so, it prints 'NO'. Otherwise, it prints 'YES' and then either the lexicographically smallest or the largest permutation of `s`, depending on which is equal to `s`. After processing all test cases, the function concludes with no explicit return value but ensures that for each input string, the appropriate output is printed.

