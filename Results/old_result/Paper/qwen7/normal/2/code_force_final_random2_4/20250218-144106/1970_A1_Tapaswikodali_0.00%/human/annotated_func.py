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
        
    #State: Output State: The final output state after the loop executes all iterations is as follows: `s` is a non-empty string consisting only of characters "(", and ")", `balance` is either 1 or -1 (it will be 1 if there is at least one more unmatched opening parenthesis than closing ones, or -1 if there is at least one more unmatched closing parenthesis than opening ones, depending on the structure of the string), `details` is a list containing tuples for each character in the string `s`. Each tuple in `details` has three elements: the current value of `balance`, the negative index `-i` of the current character in the string `s`, and the character itself. The length of `details` is equal to the length of the string `s`. The index `i` will be the index of the last character in the string `s`.
    #
    #This means that after the loop completes, `balance` will reflect whether there are more opening or closing parentheses in the string, and `details` will contain information about the balance at each step of the iteration through the string.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: "(())"
#Overall this is what the function does:The function processes a string `s` consisting only of '(' and ')' characters, ensuring it is a balanced parentheses sequence. It calculates the balance of parentheses at each position in the string and stores this information in a list of tuples. After sorting this list based on the balance values, it constructs a new string from the characters in `s` based on the sorted order and prints this new string. The final output is a string where the original characters are reordered according to their balance values during the iteration through the input string.

