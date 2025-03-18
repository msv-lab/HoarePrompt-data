#State of the program right berfore the function call: s is a non-empty string consisting only of characters "(" and ")". The string is guaranteed to be a balanced parentheses sequence with its length not exceeding 500,000.
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
        
    #State: Output State: `balance` is 0; `details` is a list containing tuples where each tuple has three elements: the first element is the balance value at each iteration, the second element is -i (where i is the index of the character in the string `s`), and the third element is the character from the string `s`. The list is constructed based on the characters in `s`, incrementing `balance` for '(' and decrementing it for ')'.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: result (where result is a string constructed by concatenating the third elements of each tuple in the sorted list `details`)
#Overall this is what the function does:The function reads a balanced parentheses string `s` from the input, processes it to maintain a balance count and store details at each step, sorts these details, and then constructs and prints a new string based on the sorted details. The final output is a string that represents the original string `s` but with characters rearranged according to their balance count and index position.

