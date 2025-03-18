#State of the program right berfore the function call: s is a non-empty string consisting only of characters "(" and ")" and s is a balanced parentheses sequence with its length not exceeding 500,000.
def func():
    s = input()
    balance = 0
    details = []
    for (i, char) in enumerate(s):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        details.append((balance, -i, char))
        
    #State: `balance` is the net count of `'('` minus the count of `')'` in the string `s`, and `details` is a list of tuples `(balance, -i, char)` for each character in `s`.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: result (where result is a string composed of characters from the input string `s` sorted by the tuple `(balance, -i, char)`)
#Overall this is what the function does:The function accepts a balanced parentheses string `s` and prints a new string formed by sorting the characters of `s` based on a tuple `(balance, -i, char)`, where `balance` is the net count of `'('` minus `')'` up to the character, `-i` is the negative index of the character, and `char` is the character itself.

