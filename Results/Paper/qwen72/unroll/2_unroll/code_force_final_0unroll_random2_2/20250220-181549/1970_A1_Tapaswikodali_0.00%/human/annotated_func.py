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
        
    #State: `s` is the same non-empty string consisting only of characters "(" and ")", and it is a balanced parentheses sequence with a length not exceeding 500,000. `balance` is 0. `details` is a list containing tuples, each with the current balance, the negative index, and the character at that index, for every character in the string `s`.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s (where s is a balanced parentheses sequence of length not exceeding 500,000)
#Overall this is what the function does:The function reads a non-empty string `s` consisting only of balanced parentheses with a maximum length of 500,000. It processes the string to create a list of tuples containing the current balance, the negative index, and the character at each position. After sorting this list, it constructs a new string from the characters in the sorted list and prints this new string. The function does not return any value.

