#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and S is a string of length N consisting only of the characters `(` and `)`.
def func():
    N = input()
    ss = raw_input()
    s = ss.split('()')
    while len(s) > 1:
        s = ''.join(s)
        
        print(s)
        
        s = s.split('()')
        
    #State of the program after the loop has been executed: `s` is a list consisting of the substrings created by repeatedly splitting the original string `S` at each occurrence of '()' until no more splits are possible, and the length of `s` is 1 or less, indicating that no further splits can be made.
    a = ''
    b = ''
    s = s[0]
    N = len(s)
    for i in range(N):
        if s[i] == '(':
            a += ')'
        
        if s[i] == ')':
            b += '('
        
    #State of the program after the  for loop has been executed: `s` is the first element of the list, `a` is equal to the number of opening parentheses in `s` concatenated with `)` for each of them, and `b` is equal to the number of closing parentheses in `s` concatenated with `(` for each of them.
    print(b + ss + a)
#Overall this is what the function does:The function accepts a positive integer `N` and a string `S` of length `N` consisting of characters `(` and `)`. It repeatedly removes pairs of `()` from the string until no more pairs can be removed. Afterward, it counts the number of unbalanced parentheses in `S`, appending the appropriate number of closing parentheses `)` to the left and opening parentheses `(` to the right of the original string `S`. The final output is a string that represents the original string with balanced parentheses added, but it does not validate whether the original sequence of parentheses was valid or not.

