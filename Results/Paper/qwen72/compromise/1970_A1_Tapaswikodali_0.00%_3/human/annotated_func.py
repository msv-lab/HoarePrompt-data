#State of the program right berfore the function call: s is a non-empty string consisting only of characters "(" and ")", and it is a balanced parentheses sequence with a length not exceeding 500,000.
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
        
    #State: `balance` is 0, `details` is a list containing tuples of the form `(balance, -i, char)` for each character in the string `s`, where `balance` is the current balance of parentheses, `i` is the index of the character in the string, and `char` is the character at that index.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s (where s is the original string from which the `details` list was created)
#Overall this is what the function does:The function `func` reads a non-empty balanced parentheses string `s` from the user input, processes it to generate a sorted list of tuples representing the balance of parentheses, negative index, and character at each position, and then prints the original string `s` in the order of the sorted list. The function does not return any value.

