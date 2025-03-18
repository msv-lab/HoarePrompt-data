#State of the program right berfore the function call: s is a string consisting only of characters "(" and ")" such that s is a non-empty balanced parentheses sequence with its length not exceeding 500,000.
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
        
    #State: s is a string consisting only of characters "(" and ")" such that s is a non-empty balanced parentheses sequence with its length not exceeding 500,000, balance is 0, details is a list of tuples (balance, -i, char) for each character in s.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s (where s is a non-empty balanced parentheses sequence)
#Overall this is what the function does:The function reads a balanced parentheses string, processes it, and prints the same string.

