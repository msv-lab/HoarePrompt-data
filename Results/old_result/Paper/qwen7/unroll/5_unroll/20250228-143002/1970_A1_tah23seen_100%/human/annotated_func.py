#State of the program right berfore the function call: s is a string consisting only of characters "(" and ")", and it is a non-empty balanced parentheses sequence with its length not exceeding 500,000.
def func_1(s):
    n = len(s)
    ans = ''
    d = {}
    d[0] = 0
    for i in range(len(s)):
        if s[i] == '(':
            d[i + 1] = d[i] + 1
        else:
            d[i + 1] = d[i] - 1
        
    #State: Output State: `ans` is an empty string, `s` is a string consisting only of characters "(" and ")", `n` is the length of `s`, `d` is a dictionary where each key from 0 to n (inclusive) represents the balance of parentheses up to that index in `s`. The value at each key is the difference between the number of '(' and ')' characters from the start of the string up to that index.
    d.pop(n)
    d = sorted(d.items(), key=lambda x: (x[1], -x[0]))
    for (i, j) in d:
        ans += s[i]
        
    #State: Output State: `ans` is a string consisting of all '(' characters from the string `s`, sorted based on the balance of parentheses up to each index in descending order.
    return ans
    #The program returns a string consisting of all '(' characters from the string 's', sorted based on the balance of parentheses up to each index in descending order.
#Overall this is what the function does:The function accepts a string `s` consisting only of characters "(" and ")" forming a balanced parentheses sequence. It calculates the balance of parentheses up to each index, sorts these balances in descending order, and collects all "(" characters from `s` based on this sorted order. Finally, it returns a string containing these collected "(" characters.

