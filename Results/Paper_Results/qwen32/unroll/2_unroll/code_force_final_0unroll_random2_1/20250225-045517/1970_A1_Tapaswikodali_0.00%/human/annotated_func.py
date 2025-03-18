#State of the program right berfore the function call: s is a non-empty string consisting only of characters "(" and ")" and is guaranteed to be a balanced parentheses sequence with its length not exceeding 500,000.
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
        
    #State: `s` is a non-empty string consisting only of characters "(" and ")" and is guaranteed to be a balanced parentheses sequence with its length not exceeding 500,000; `balance` is 0; `details` is a list of tuples (balance, -i, char) for each character in the string `s`.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s (where s is the balanced parentheses string)
#Overall this is what the function does:The function takes a non-empty string `s` consisting of balanced parentheses and prints a rearranged version of the string based on the balance and position of each parenthesis.

