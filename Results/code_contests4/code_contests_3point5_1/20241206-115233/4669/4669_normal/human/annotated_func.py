#State of the program right berfore the function call: **
def func():
    N = input()
    ss = raw_input()
    s = ss.split('()')
    while len(s) > 1:
        s = ''.join(s)
        
        print(s)
        
        s = s.split('()')
        
    #State of the program after the loop has been executed: N is assigned the user input value, ss is assigned the user input value as a string, s is an empty list
    a = ''
    b = ''
    s = s[0]
    N = len(s)
    for i in range(N):
        if s[i] == '(':
            a += ')'
        
        if s[i] == ')':
            b += '('
        
    #State of the program after the  for loop has been executed: N is greater than 0. The list s may have been modified. Variables a and b are lists that contain parentheses corresponding to the changes made in the loop.
    print(b + ss + a)
#Overall this is what the function does:The function reads user input for N and ss, splits ss by '()', then modifies the string based on the parentheses encountered in a loop. Finally, it prints the modified string with additional characters. The function does not accept any parameters and solely operates on the user input.

