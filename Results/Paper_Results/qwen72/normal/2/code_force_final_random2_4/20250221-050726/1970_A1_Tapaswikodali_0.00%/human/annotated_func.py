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
        
    #State: After the loop executes all iterations, `s` remains a non-empty string consisting only of characters "(" and ")", and it should be a balanced parentheses sequence with a length not exceeding 500,000. The variable `i` is the index of the last character in `s`, which is `len(s) - 1`. The variable `char` is the last character in `s`. The variable `balance` is 0 because the parentheses sequence is balanced. The variable `details` is a list containing tuples for each character in `s`, where each tuple is in the form `(balance, -i, char)`, representing the balance after processing the character at position `i`, the negative index `-i`, and the character itself.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: - Given that `s` is a string of balanced parentheses, the `balance` will always return to 0 at the end of the string.
    #   - The sorting criteria ensure that the characters are rearranged in a way that maintains the balance but may change the order of matching parentheses pairs.
    #
    #Since the exact content of `s` is not provided, we cannot determine the exact string `result` will contain. However, based on the sorting criteria, the `result` string will be a valid string of balanced parentheses, potentially in a different order from the original `s`.
    #
    #Output:
#Overall this is what the function does:The function reads a non-empty string `s` consisting only of characters "(" and ")", which forms a balanced parentheses sequence with a length not exceeding 500,000. It processes this string to maintain a balance count and records details about each character. After processing, it sorts these details and constructs a new string `result` that is also a valid balanced parentheses sequence, potentially in a different order from the original `s`. The function then prints this new string `result`. The final state of the program is that the original string `s` remains unchanged, and the new string `result` is printed to the console.

