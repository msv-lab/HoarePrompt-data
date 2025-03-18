#State of the program right berfore the function call: s is a non-empty string consisting only of characters "(" and ")", and it is a balanced parentheses sequence with its length not exceeding 500,000.
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
        
    #State: Output State: `balance` will be 0, `details` is a list containing tuples where each tuple consists of the current `balance`, the negative index `-i`, and the corresponding character `char` from the string `s`. The length of `details` will be equal to the length of `s`.
    #
    #Explanation: After the loop completes all its iterations, `balance` will return to 0 because every opening parenthesis '(' will eventually be matched with a closing parenthesis ')'. The `details` list will contain a tuple for each character in the string `s`, representing the balance at each step of the iteration, the negative index of the character, and the character itself. The exact contents of `details` depend on the content of `s`, but it will include one tuple per character in `s`.
    details.sort()
    result = ''.join(char for _, _, char in details)
    print(result)
    #This is printed: result (where result is a string formed by concatenating characters from the tuples in the sorted list details)
#Overall this is what the function does:The function accepts a string `s` consisting of balanced parentheses and processes it to form a new string `result`. This new string is constructed by rearranging the characters of `s` based on their balance value during traversal. Specifically, it sorts the characters according to their balance values and their positions in the original string, then concatenates them in the sorted order. The function prints the resulting string and does not return any value.

