#State of the program right berfore the function call: s is a non-empty string consisting only of characters "(" and ")" and is a balanced parentheses sequence with a length not exceeding 500,000.
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
        
    #State: After the loop has executed all iterations, `s` remains a non-empty string consisting only of characters "(" and ")" and is a balanced parentheses sequence with a length not exceeding 500,000. The variable `i` is the index of the last character in `s`, which is `len(s) - 1`. The variable `char` is the last character of `s`. The variable `balance` is 0 because the string `s` is a balanced parentheses sequence. The variable `details` is a list containing tuples for each character in `s`, where each tuple is in the form `(balance, -i, char)` representing the balance at that point, the negative index, and the character itself.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s (where s is a balanced parentheses sequence)
#Overall this is what the function does:The function reads a non-empty, balanced parentheses sequence from the input, processes it, and prints a transformed version of the sequence. The transformation involves maintaining a balance count of parentheses and recording details about each character. After processing, the function sorts these details and constructs a new string from the sorted data, which is then printed. The final state of the program includes the original string `s` remaining unchanged, and the printed output being a potentially reordered version of the original balanced parentheses sequence.

