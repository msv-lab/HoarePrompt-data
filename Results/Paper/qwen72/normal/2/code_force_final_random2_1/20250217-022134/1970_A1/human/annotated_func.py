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
        
    #State: After all iterations of the loop, `s` remains a non-empty string consisting only of characters "(" and ")", and it should be a balanced parentheses sequence with a length not exceeding 500,000. `balance` is 0 because the sequence is balanced. `details` is a list containing tuples for each character in `s`, where each tuple is in the form `(balance, -i, char)`, with `balance` representing the current balance of parentheses, `-i` representing the negative index of the character, and `char` being the character from `s`. `i` is the last index of the string `s` (i.e., `len(s) - 1`).
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s reversed (where s is the original balanced parentheses sequence)
#Overall this is what the function does:The function reads a non-empty string `s` consisting only of characters "(" and ")", which forms a balanced parentheses sequence with a length not exceeding 500,000. It processes this string and prints the reversed version of `s`. The function does not return any value. After the function concludes, the original string `s` remains unchanged, and the reversed string is printed to the console.

