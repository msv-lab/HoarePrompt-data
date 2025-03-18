#State of the program right berfore the function call: n is a positive integer representing the length of the string, and a is a list of non-negative integers of length n, where each element a_i represents the number of previous indices with the same character as the current index in the string.
def func_1(n, a):
    s = ''
    char_count = [0] * 26
    for i in range(n):
        for j in range(26):
            if char_count[j] == a[i]:
                s += chr(j + ord('a'))
                char_count[j] += 1
                break
        
    #State: Output State: `s` is a string consisting of lowercase English letters where each letter appears a number of times equal to its corresponding value in `a`. `char_count` is a list of 26 integers where each integer is incremented by the count of its corresponding letter in `s`.
    return s
    #The program returns the string `s` which consists of lowercase English letters where each letter appears a number of times equal to its corresponding value in `a`, and `char_count` is a list of 26 integers where each integer is incremented by the count of its corresponding letter in `s`
#Overall this is what the function does:The function accepts two parameters: `n`, a positive integer representing the length of the string, and `a`, a list of non-negative integers of length `n` where each element `a_i` represents the number of previous indices with the same character as the current index in the string. After processing, it returns a string `s` consisting of lowercase English letters, where each letter appears a number of times equal to its corresponding value in `a`, and a list `char_count` of 26 integers where each integer is incremented by the count of its corresponding letter in `s`.

