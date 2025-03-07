#State of the program right berfore the function call: s is a string consisting only of characters "(" and ")". The string is guaranteed to be a non-empty balanced parentheses sequence with its length not exceeding 500,000.
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
        
    #State: Output State: `s` is a string consisting only of characters "(" and ")"; `balance` is the final balance calculated after processing the entire string `s`; `details` is a list of tuples, each containing three elements: the balance at each character position, the negative index of the character, and the character itself.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s
#Overall this is what the function does:The function processes a string `s` consisting of balanced parentheses and generates a new string based on the balance of parentheses at each position. It calculates the balance of parentheses as it iterates through the string, records this balance along with the character and its position (using negative indexing), sorts these records, and then constructs a new string from the characters in the order of their recorded balances. Finally, it prints the original string `s`.

