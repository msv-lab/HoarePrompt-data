#State of the program right berfore the function call: s is a non-empty string consisting only of characters "(" and ")" and is a balanced parentheses sequence with its length not exceeding 500,000.
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
        
    #State: `s` is a non-empty string consisting only of characters "(" and ")" and is a balanced parentheses sequence with its length not exceeding 500,000; `balance` is 0; `details` is a list containing tuples `(balance, -i, char)` for each character in `s`.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s
#Overall this is what the function does:The function takes a non-empty string `s` consisting only of balanced parentheses and prints a new string formed by sorting the characters based on their balance and position in the original string.

