#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 100, and S is a string of length N consisting only of the characters '(' and ')'.
def func():
    N = input()
    ss = raw_input()
    s = ss.split('()')
    while len(s) > 1:
        s = ''.join(s)
        
        print(s)
        
        s = s.split('()')
        
    #State of the program after the loop has been executed: `N` is a string representation of an integer in the range 1 to 100; `S` remains unchanged; `s` is now a list that has been repeatedly split by '()' until no further splitting is possible, resulting in a final list of substrings.
    a = ''
    b = ''
    s = s[0]
    N = len(s)
    for i in range(N):
        if s[i] == '(':
            a += ')'
        
        if s[i] == ')':
            b += '('
        
    #State of the program after the  for loop has been executed: `N` is greater than or equal to 0, `S` remains unchanged, `s` is the first element of the split list, `a` is the string of closing parentheses generated from the opening parentheses in `s`, `b` is the string of opening parentheses generated from the closing parentheses in `s`.
    print(b + ss + a)
#Overall this is what the function does:The function accepts an integer N (1 ≤ N ≤ 100) and a string S of length N consisting only of '(' and ')'. It processes S by repeatedly removing pairs of '()' until no more can be removed. After that, it counts the remaining unmatched parentheses in S, constructing two new strings: one consisting of closing parentheses for every opening parenthesis and another consisting of opening parentheses for every closing parenthesis found in S. Finally, it prints the concatenation of the opening parentheses, the original string S, and the closing parentheses. The function does not return any value; instead, it directly prints the result.

