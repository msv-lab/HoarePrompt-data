#State of the program right berfore the function call: 
def func():
    s = raw_input()
    t = raw_input()
    print['No', 'Yes'][any(t[i:] + t[:i] == s for i in range(len(t)))]
#Overall this is what the function does:The function `func` reads two strings `s` and `t` as input. It then checks if any rotation of string `t` is equal to string `s`. If there is a rotation that matches `s`, it prints 'Yes', otherwise it prints 'No'. The function does not accept any parameters and does not have a return value.

