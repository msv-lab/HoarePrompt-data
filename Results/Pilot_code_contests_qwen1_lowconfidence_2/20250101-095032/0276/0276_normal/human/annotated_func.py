#State of the program right berfore the function call: string is a non-empty string consisting of small English letters, digits, and the signs "less" (<) and "more" (>), and it is a potentially corrupted version of a correctly encoded message where each word is prefixed and suffixed by "<3".
def func_1(string):
    return ''.join(filter(lambda x: x.isalpha(), string))
    #''.join(filter(lambda x: x.isalpha(), string)) which removes all non-alphabetic characters from the string, leaving only letters
#Overall this is what the function does:The function `func_1` accepts a single parameter `string`, which is a potentially corrupted version of a correctly encoded message where each word is prefixed and suffixed by "<3". The function removes all non-alphabetic characters from the string, leaving only letters. This includes removing digits, punctuation marks, and special characters such as "less" (<) and "more" (>). The function returns a new string consisting solely of alphabetic characters. Potential edge cases include strings that contain no alphabetic characters or strings that consist entirely of special characters and digits. In such cases, the function will return an empty string.

#State of the program right berfore the function call: encoding is a string containing Dima's encoded message, which consists of words separated by "<3". Each word is followed by "<3" except for the last word. word_list is a list of strings, where each string is a word from Dima's original message without any additional characters or encoding.
def func_2(encoding, word_list):
    encoding_toks = encoding.split('<3')
    message_str = ''.join(word_list)
    encoding_str = ''
    for enc in encoding_toks[1:-1]:
        enc = func_1(enc)
        
        if not enc:
            return 'no'
        
        encoding_str += enc
        
    #State of the program after the  for loop has been executed: `encoding_str` is the concatenation of the results of applying `func_1` to all elements of `encoding_toks` except the first and last elements, `word_list` is a list of strings, `message_str` is a string obtained by concatenating all elements of `word_list` without any separator, `encoding_toks` must have at least 3 elements, `enc` is the result of `func_1(enc)` in the final iteration.
    if (encoding_str == message_str) :
        return 'yes'
        #The program returns 'yes'
    else :
        return 'no'
        #The program returns 'no'
#Overall this is what the function does:The function `func_2` takes two parameters: `encoding`, a string representing Dima's encoded message where each word is separated by "<3", and `word_list`, a list of strings representing the original message words without any additional characters or encoding. The function processes the `encoding` string by splitting it into tokens using "<3" as the delimiter and then applies another function `func_1` to each token except the first and last ones. It constructs a new string `encoding_str` from these processed tokens. If `encoding_str` matches the `message_str` formed by concatenating all elements of `word_list`, the function returns `'yes'`; otherwise, it returns `'no'`. The function handles the case where `encoding_toks` has fewer than three elements by immediately returning `'no'`.

