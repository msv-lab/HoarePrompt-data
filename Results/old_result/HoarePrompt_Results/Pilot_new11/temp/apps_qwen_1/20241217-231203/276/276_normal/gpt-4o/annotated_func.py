#State of the program right berfore the function call: s is a non-empty string consisting of '0' and '1' characters, representing a number in the golden system notation.
def func_1(s):
    q = (5 ** 0.5 + 1) / 2
    value = 0
    n = len(s)
    for i in range(n):
        if s[i] == '1':
            value += q ** (n - i - 1)
        
    #State of the program after the  for loop has been executed: ```
    #`s` is a non-empty string consisting of '0' and '1' characters, `q` is 5, `value` is the sum of 5
    return value
    #The program returns value which is equal to 5
#Overall this is what the function does:The function `func_1` accepts a string `s` consisting of '0' and '1' characters, representing a number in the golden system notation. It calculates the value of the string `s` based on the golden ratio `q`, where `q = (5

