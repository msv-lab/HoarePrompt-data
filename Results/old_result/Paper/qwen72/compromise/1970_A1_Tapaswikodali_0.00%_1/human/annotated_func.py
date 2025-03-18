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
        
    #State: `s` is the same non-empty string consisting only of characters "(" and ")", and it is a balanced parentheses sequence with a length not exceeding 500,000; `balance` is 0; `details` is a list containing tuples of the form (balance, -i, char) for each character in `s`, where `balance` is the balance of parentheses at that point, `-i` is the negative index of the character, and `char` is the character itself.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: [reverse of the original string `s`] (where `s` is a balanced parentheses sequence consisting only of characters "(" and ")", and the length of `s` does not exceed 500,000)
#Overall this is what the function does:The function takes no parameters and operates on a non-empty string `s` consisting only of characters "(" and ")", where `s` is a balanced parentheses sequence with a length not exceeding 500,000. It reads the string `s` from user input, processes it to maintain a balance of parentheses, and then prints the reverse of the original string `s`. The function does not return any value. After the function concludes, the original string `s` remains unchanged, and the printed output is the reversed string of `s`.

