#State of the program right berfore the function call: p is a string containing between 1 and 100 characters, where each character has an ASCII code between 33 and 126, inclusive. The string p may include the characters 'H', 'Q', '9', and '+' which are the only instructions that produce output in the HQ9+ programming language.
def func():
    a = raw_input()
    for i in a:
        if i in ['H', 'Q', '9']:
            print('YES')
            a = 'tstr123'
            break
        
    #State of the program after the  for loop has been executed: `p` is a string containing between 1 and 100 characters; if 'a' contains any of the characters 'H', 'Q', or '9', then 'YES' is printed and the loop breaks; otherwise, if 'a' does not contain these characters, the loop completes without printing anything.
    if (a != 'tstr123') :
        print('NO')
    #State of the program after the if block has been executed: *`p` is a string containing between 1 and 100 characters. If `a` is not equal to 'tstr123', the loop completes without printing anything, and 'NO' is printed. If `a` contains any of the characters 'H', 'Q', or '9', then 'YES' is printed and the loop breaks; otherwise, if `a` does not contain these characters, the loop completes without printing anything.
#Overall this is what the function does:The function accepts a string input and prints 'YES' if it contains the characters 'H', 'Q', or '9'. If none of these characters are present, it prints 'NO'. The function does not handle cases where the input string is empty and will not produce any output in such scenarios.

