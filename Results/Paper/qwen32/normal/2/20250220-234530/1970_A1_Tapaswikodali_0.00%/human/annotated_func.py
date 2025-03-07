#State of the program right berfore the function call: s is a non-empty string consisting only of characters "(" and ")" and represents a balanced parentheses sequence with a length not exceeding 500,000.
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
        
    #State: `s` is a non-empty string consisting only of characters "(" and ")" and represents a balanced parentheses sequence with a length not exceeding 500,000; `balance` is 0; `details` is a list containing tuples `(balance, -i, char)` for each character in `s`, where `balance` reflects the net effect of all previous parentheses up to that point, `-i` is the negative index of the character, and `char` is the character itself.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s (where s is the given balanced parentheses sequence)
#Overall this is what the function does:The function takes a non-empty string `s` consisting only of characters "(" and ")" representing a balanced parentheses sequence and prints the same sequence `s`.

