#State of the program right berfore the function call: s is a string consisting only of characters "(" and ")". The string is guaranteed to be a non-empty balanced parentheses sequence with its length not exceeding 500,000.
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
        
    #State: Output State: `s` is a string consisting only of characters "(" and ")"; `n` is the length of the string `s`; `ans` is an empty string; `d` is a list where each element represents the balance of "(" and ")" up to that index in `s`.
    d.pop(n)
    d = sorted(d.items(), key=lambda x: (x[1], -x[0]))
    for (i, j) in d:
        ans += s[i]
        
    #State: Output State: `ans` is a string containing all characters from `s` at the indices specified in the list `d`, in the order given by `d`.
    return ans
    #The program returns a string containing characters from `s` at the indices specified in the list `d`, in the order given by `d`.
#Overall this is what the function does:The function accepts a string `s` consisting only of characters "(" and ")`. It calculates the balance of "(" and ")" at each index, sorts these balances, and constructs a new string containing characters from `s` at the sorted indices. The function then returns this new string.

