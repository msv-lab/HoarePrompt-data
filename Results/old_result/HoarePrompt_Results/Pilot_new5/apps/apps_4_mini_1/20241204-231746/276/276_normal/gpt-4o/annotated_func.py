#State of the program right berfore the function call: s is a non-empty string consisting of '0' and '1' characters, and the length of s does not exceed 100,000.
def func_1(s):
    q = (5 ** 0.5 + 1) / 2
    value = 0
    n = len(s)
    for i in range(n):
        if s[i] == '1':
            value += q ** (n - i - 1)
        
    #State of the program after the  for loop has been executed: `s` is a non-empty string consisting of '0' and '1' characters with length `n` between 1 and 100,000; `q` is approximately `1.618033988749895`; `value` is the sum of `q` raised to the power of `(n - i - 1)` for each index `i` where `s[i]` is '1', and `value` is 0 if there are no '1's in `s`.
    return value
    #The program returns the sum of q raised to the power of (n - i - 1) for each index i where s[i] is '1', and value is 0 if there are no '1's in s.
#Overall this is what the function does:The function accepts a non-empty string `s` consisting of '0' and '1' characters and calculates a value based on the Fibonacci constant `q` (approximately 1.618) raised to the power of `(n - i - 1)` for each index `i` where `s[i]` is '1'. The function returns the computed sum, which will be 0 if there are no '1's in `s`.

