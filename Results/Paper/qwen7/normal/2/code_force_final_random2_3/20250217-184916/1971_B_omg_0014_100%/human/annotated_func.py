#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, s is a string consisting of lowercase English letters with a length of at most 10.
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
        
    #State: The loop has executed all its iterations, with `t` remaining an integer such that 1 ≤ t ≤ 1000, `n` being the original input integer greater than 0, and `i` being the last iteration index (n-1). For each iteration `i` from 0 to n-1, there is a corresponding input string `s_i`, a set `a_i` containing unique characters from `s_i`, and two strings `b_i` and `c_i` where `b_i` is the sorted version of `s_i` and `c_i` is the sorted version of `s_i` in descending order. If the size of `a_i` is 1, then `c_i` remains unchanged; otherwise, `c_i` is the sorted version of `s_i` in descending order.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `t` and a string `s`. For each test case, it checks if the input string `s` contains more than one unique character. If `s` consists of a single unique character, it prints 'NO'. Otherwise, it prints 'YES' and then outputs either the lexicographically smallest permutation of `s` or the lexicographically largest permutation of `s`, depending on which permutation matches the original string `s`.

