#State of the program right berfore the function call: The input string s is a non-empty balanced parentheses sequence consisting only of characters "(" and ")", with its length not exceeding 500,000.
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
        
    #State: Output State: The final output state after the loop executes all iterations is as follows: `s` is a non-empty string consisting only of characters "(", ")", `i` is equal to the length of `s` minus 1, `balance` is either a positive or negative integer depending on whether there are more opening or closing parentheses in `s`, and `details` is a list containing as many tuples as there are characters in `s`. Each tuple in `details` has the form `(balance, -i, char)`, indicating the current balance of parentheses, the negative index of the current character, and the character itself from the original string `s`.
    #
    #This means that after the loop completes, `balance` will reflect the net difference between the number of opening and closing parentheses in the string `s`. If `balance` is positive, there are more opening parentheses than closing ones; if it's negative, there are more closing parentheses. The `details` list captures the state of the balance at each step of the iteration, providing a detailed trace of how the balance changed with each character processed.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: result (a rearranged version of s based on the balance values of its characters)
#Overall this is what the function does:The function processes a given balanced parentheses sequence and returns a rearranged version of the sequence based on the balance of parentheses at each position. Specifically, it calculates the balance of parentheses at each character position, sorts these balances, and then reconstructs the string using the original characters but ordered according to their balance values. If the balance is positive, characters with higher balance values come first, and if the balance is negative, characters with lower balance values come first.

