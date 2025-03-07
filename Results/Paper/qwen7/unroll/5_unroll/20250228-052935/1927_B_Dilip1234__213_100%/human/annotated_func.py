#State of the program right berfore the function call: n is a positive integer representing the length of the string, and a is a list of non-negative integers of length n, where each element a_i represents the number of previous indices with the same character as the i-th index in the string.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: Output State: `char_count` is a list of 26 integers where each integer is equal to the number of times its corresponding character ('a' to 'z') appears in the string `s`. The string `s` contains characters from 'a' to 'z' based on the values in the list `a`, and `n` is the length of the string `s`.
    return s
    #The program returns a string `s` that contains characters from 'a' to 'z' based on the values in the list `char_count`, where each integer in `char_count` represents the number of times its corresponding character appears in `s`.
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer representing the length of the string, and `a`, a list of non-negative integers of length `n` where each element `a_i` represents the number of previous indices with the same character as the `i`-th index in the string. After processing, it constructs and returns a string `s` containing characters from 'a' to 'z'. Each character in `s` appears a number of times specified by the corresponding value in `char_count`, which is derived from the input list `a`.

