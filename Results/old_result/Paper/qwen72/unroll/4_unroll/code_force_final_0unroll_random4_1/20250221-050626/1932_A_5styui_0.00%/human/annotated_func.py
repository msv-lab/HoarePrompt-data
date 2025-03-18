#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 1000) representing the number of test cases, and a list of tuples where each tuple contains an integer n (1 ≤ n ≤ 50) and a string of n characters ('.', '@', '*') representing the path. The first character of each string is always '.'.
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
        
    #State: `t` is an integer between 1 and 1000, `a` is an input integer, the list of tuples is unchanged, `s` is 0.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, representing the number of test cases. For each test case, it reads an integer `n` and a string of `n` characters (which must start with a '.' and can contain '.', '@', or '*'). The function counts the number of '@' characters in the string until it encounters a '*' character, at which point it stops counting and moves to the next test case. After processing all test cases, the function prints the count of '@' characters for each test case and resets the count to 0 for the next test case. The function does not return any value; it only prints the results. The input parameters and the list of tuples are not directly used in the function, and the function does not modify any external state beyond the printed output.

