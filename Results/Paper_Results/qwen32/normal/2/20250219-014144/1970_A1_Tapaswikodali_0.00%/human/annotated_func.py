#State of the program right berfore the function call: s is a string consisting only of characters "(" and ")" and is guaranteed to be a non-empty balanced parentheses sequence with its length not exceeding 500,000.
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
        
    #State: `balance` is 0; `details` is a list of tuples `(balance, -i, char)` for each character in `s`.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: result (where result is the concatenation of the `char` elements from the `details` list, sorted by `-i` and then by `char`)
#Overall this is what the function does:The function takes a string `s` consisting of balanced parentheses and prints a new string formed by sorting the characters based on their positions and types, resulting in a specific rearrangement of the parentheses.

