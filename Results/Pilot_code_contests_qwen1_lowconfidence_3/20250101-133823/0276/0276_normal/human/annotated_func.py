#State of the program right berfore the function call: string is a non-empty string consisting of small English letters, digits, and the "<" and ">" characters. The string represents a potentially encoded message.
def func_1(string):
    return ''.join(filter(lambda x: x.isalpha(), string))
    #The program returns a string containing only the alphabetical characters from the original string, with all other characters (digits, "<", ">") removed
#Overall this is what the function does:The function `func_1` accepts a string parameter `string`, which can contain small English letters, digits, and the "<" and ">" characters. It processes the string by filtering out all non-alphabetical characters (digits and "<" and ">") and returns a new string containing only the alphabetical characters from the original string. The function effectively removes all digits and special characters from the input string, leaving only the alphabetic characters. This process ensures that the returned string consists solely of letters from the English alphabet.

#State of the program right berfore the function call: encoding is a string containing the encoded message with hearts (sequences of "<3") separating words, and word_list is a list of strings representing the words that Dima intended to send. Each word in word_list is a valid word from the input and is separated by "<3".
def func_2(encoding, word_list):
    encoding_toks = encoding.split('<3')
    message_str = ''.join(word_list)
    encoding_str = ''
    for enc in encoding_toks[1:-1]:
        enc = func_1(enc)
        
        if not enc:
            return 'no'
        
        encoding_str += enc
        
    #State of the program after the  for loop has been executed: - After all iterations of the loop, `encoding_str` will contain the concatenation of all valid `enc` values obtained from `func_1(enc)` for each iteration where `enc` is not empty.
    #   - If any `enc` is such that `func_1(enc)` returns an empty string, `encoding_str` will be updated to `encoding_str + 'no'`.
    #
    #### Summary:
    #-
    if (encoding_str == message_str) :
        return 'yes'
        #The program returns 'yes'
    else :
        return 'no'
        #The program returns 'no'
#Overall this is what the function does:The function `func_2` accepts two parameters: `encoding` and `word_list`. `encoding` is a string containing the encoded message with hearts (sequences of "<3") separating words, and `word_list` is a list of strings representing the words that Dima intended to send. The function processes the `encoding` string by splitting it into parts using the heart separator and applying the `func_1` function to each part. If any part processed by `func_1` results in an empty string, the function immediately returns 'no'. Otherwise, it reconstructs the message by concatenating the results of `func_1` calls and compares it with the original message represented by `word_list`. If the reconstructed message matches the original message, the function returns 'yes'; otherwise, it returns 'no'.

