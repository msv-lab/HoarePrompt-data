#State of the program right berfore the function call: n is a positive integer representing the length of the string, and a is a list of non-negative integers of length n, where each element a_i (0 <= a_i < n) represents the number of previous indices with the same character in the string.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: Output State: `char_count` is a list of 26 integers, each increased by the corresponding value in the list `a`. The string `s` contains characters from 'a' to 'z' based on the values in `a`, with each character appearing a number of times equal to its corresponding value in `a`.
    return s
    #The program returns a string `s` containing characters from 'a' to 'z', where each character appears a number of times equal to its corresponding value in the list `a`.
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer representing the length of the string, and `a`, a list of non-negative integers of length `n`. It constructs a string `s` containing characters from 'a' to 'z', where each character appears a number of times equal to its corresponding value in the list `a`. After executing the function, the program returns the string `s`.

