#State of the program right berfore the function call: The function should take two parameters: an integer n (1 ≤ n ≤ 50) representing the length of the path, and a string s of n characters where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The first cell is guaranteed to be empty.
def func():
    a = int(input())
    s = 0
    for i in range(a):
        d = int(input())
        
        b = input()
        
        for j in range(len(b)):
            if b[j] == '@':
                s = s + 1
            elif b[j] == '*':
                if b[:]:
                    break
                elif b[j + 1] == '*':
                    break
        
        print(s)
        
        s = 0
        
    #State: `n` is an integer between 1 and 50, `a` is equal to or greater than the number of iterations, `i` is `a - 1`, `d` is an input integer, `b` is a new input string, `j` is `len(b)`, and `s` is 0.
#Overall this is what the function does:The function reads an integer `a` from the user, representing the number of paths to process. For each path, it reads an integer `d` (which is not used in the function) and a string `b` of `d` characters, where '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. The function counts the number of coins ('@') in the string `b` until it encounters a thorn ('*'). If a thorn is encountered, the counting stops, and the number of coins collected so far is printed. After processing each path, the coin count is reset to 0. The function does not return any value.

