#State of the program right berfore the function call: The function should take an integer t (1 ≤ t ≤ 100) representing the number of test cases, and for each test case, an integer n (3 ≤ n ≤ 78) representing the encoded word.
def func():
    alphabet = string.ascii_lowercase
    for i in range(int(input())):
        n = int(input())
        
        word = ''
        
        if n > 52:
            word += alphabet[n - 53] + 'zz'
        elif n > 27:
            word += 'a' + alphabet[n - 28] + 'z'
        elif n == 27:
            word = 'aay'
        else:
            word += 'aa' + alphabet[n - 3]
        
        print(word)
        
    #State: `t` is greater than 0, `i` is `t - 1`, and `n` is an input integer for the last iteration. If `n` > 52, `word` is the string formed by concatenating the character at index `n - 53` in the `alphabet` string with 'zz'. If `n` > 27 and `n` <= 52, `word` is the string 'a' followed by the character at index `n - 28` in the `alphabet` string followed by 'z'. If `n` is 27, `word` is 'aay'. If `n` < 27, `word` is 'aa' followed by the character at index `n - 3` in the string 'abcdefghijklmnopqrstuvwxyz'.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `t` (1 ≤ t ≤ 100) from the input, representing the number of test cases. For each test case, it reads another integer `n` (3 ≤ n ≤ 78) from the input, decodes `n` into a string `word` based on specific rules, and prints the decoded string. The rules for decoding are as follows: if `n` > 52, `word` is the character at index `n - 53` in the lowercase English alphabet concatenated with 'zz'; if `n` > 27 and `n` ≤ 52, `word` is 'a' followed by the character at index `n - 28` in the alphabet and then 'z'; if `n` is 27, `word` is 'aay'; if `n` < 27, `word` is 'aa' followed by the character at index `n - 3` in the alphabet. After processing all test cases, the function does not return any value.

