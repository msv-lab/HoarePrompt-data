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
        
    #State: Output State: `s` is a non-empty balanced parentheses sequence consisting only of characters "(" and ")"; `balance` is 0; `details` is a list of tuples where each tuple contains three elements: the current value of `balance`, the negative index of the character in `s`, and the character itself. The list is constructed such that for every opening parenthesis "(", `balance` increases by 1, and for every closing parenthesis ")", `balance` decreases by 1.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: s (where s is the original balanced parentheses sequence)
#Overall this is what the function does:The function processes a given balanced parentheses sequence `s` and constructs a new sequence based on the balance of parentheses at each position. It then sorts these positions and reconstructs the original sequence based on the sorted positions, finally printing the original sequence `s`.

