#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 100, and S is a string of length N consisting only of the characters `(` and `)`.
def func():
    N = input()
    ss = raw_input()
    s = ss.split('()')
    while len(s) > 1:
        s = ''.join(s)
        
        print(s)
        
        s = s.split('()')
        
    #State of the program after the loop has been executed: `N` is an input string; `S` is a string that has been reduced to a form with no remaining occurrences of `()`; `s` is a list containing the final substrings derived from the repeated splitting of the original string `S`.
    a = ''
    b = ''
    s = s[0]
    N = len(s)
    for i in range(N):
        if s[i] == '(':
            a += ')'
        
        if s[i] == ')':
            b += '('
        
    #State of the program after the  for loop has been executed: `a` is equal to the number of '(' in `s` represented as `')'`, `b` is equal to the number of ')' in `s` represented as `'('`, `N` is the length of `s`, `s` contains the final substrings derived from `S`.
    print(b + ss + a)
#Overall this is what the function does:The function accepts no parameters and reads an integer N and a string S of length N consisting of the characters `(` and `)`. It reduces S by repeatedly removing adjacent pairs of `()` until no more pairs can be removed. Then, it counts the number of unmatched `(` and `)` in the resulting string and constructs a new string that consists of the unmatched `)` followed by the original input string S, followed by the unmatched `(`. The final output is printed but not returned, and the function does not handle potential edge cases related to invalid input.

